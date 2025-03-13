from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
import json
import os
import google.generativeai as genai
from google.cloud import vision
from werkzeug.utils import secure_filename
import re

# Initialize Flask app
app = Flask(__name__)

# Configure upload folder
UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["ocr_database"]
collection = db["extracted_data"]

# Set up Google Vision API client
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:/Users/laksh/Downloads/ocr-model-451910-c14b246a31ed.json"
vision_client = vision.ImageAnnotatorClient()

# Configure Gemini AI
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-pro-latest")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    if "images" not in request.files:
        return jsonify({"error": "No file part"}), 400

    files = request.files.getlist("images")
    if not files or all(file.filename == "" for file in files):
        return jsonify({"error": "No files selected"}), 400

    extracted_results = []

    for file in files:
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        file.save(filepath)

        extracted_text = extract_text_from_image(filepath)

        if extracted_text:
            extracted_data = convert_text_to_json(extracted_text)

            if extracted_data:
                print("✅ Final Processed Data Before Saving:", extracted_data)

                # Ensure correct mapping of marks
                for subject in extracted_data.get("Marks Scored", []):
                    subject["Total"] = subject.get("Theory", 0) + subject.get("Practical", 0) + subject.get("Internal", 0)
                
                extracted_data["filename"] = filename  # Store filename
                inserted_doc = collection.insert_one(extracted_data)  # Store in MongoDB
                extracted_data["_id"] = str(inserted_doc.inserted_id)  # Convert ObjectId to string
                extracted_results.append(extracted_data)
            else:
                extracted_results.append({"error": f"Failed to parse text from {filename}"})
        else:
            extracted_results.append({"error": f"No text extracted from {filename}"})

    return jsonify({"message": "Images processed successfully", "data": extracted_results})

@app.route("/get_data", methods=["GET"])
def get_data():
    latest_entry = collection.find_one(sort=[("_id", -1)])  # Fetch the latest entry
    if latest_entry:
        latest_entry["_id"] = str(latest_entry["_id"])  # Convert ObjectId to string
        return jsonify(latest_entry)
    return jsonify({"error": "No data found"}), 404

# -------------------------------------
# HELPER FUNCTIONS
# -------------------------------------
def extract_text_from_image(filepath):
    try:
        with open(filepath, "rb") as image_file:
            content = image_file.read()
            image = vision.Image(content=content)
            response = vision_client.text_detection(image=image)
            texts = response.text_annotations

        extracted_text = texts[0].description if texts else None
        print("📝 Extracted OCR Text:\n", extracted_text)  # Debugging Step
        return extracted_text
    except Exception as e:
        print(f"❌ Vision API Error: {str(e)}")
        return None
def validate_marks_data(parsed_data):
    """Corrects practical marks for subjects that shouldn't have them and fixes None values."""
    for subject in parsed_data.get("Marks Scored", []):
        subject_name = subject.get("Subject", "").upper()

        # Tamil and English should not have practical marks
        if subject_name in ["TAMIL", "ENGLISH",]:
            subject["Practical"] = 0

        # Replace None values with 0 for safe calculations
        subject["Theory"] = subject.get("Theory", 0) or 0
        subject["Practical"] = subject.get("Practical", 0) or 0
        subject["Internal"] = subject.get("Internal", 0) or 0

        # Calculate total properly
        subject["Total"] = (
            subject["Theory"] + subject["Practical"] + subject["Internal"]
        )

    return parsed_data

def convert_text_to_json(text):
    prompt = f"""
    Extract the following details from the text and return **only** a valid JSON response.

    Required fields:
    - Name
    - Roll No
    - Group Code
    - Date of Birth
    - School Name
    - Board
    - Marks Scored (List of subjects with correct Theory, Practical, Internal, and Total marks)

    **Rules:**
    - Tamil and English should have Practical = 0
    - Ensure each subject has the correct breakdown
    - The Total column must be the sum of the correct values
    - Identify `Second Year` marks only and ignore `First Year` marks.

    **Text from OCR**:
    {text}

    Ensure that the output is **strictly JSON** without extra text.
    """

    try:
        response = model.generate_content(prompt, request_options={"timeout": 240})
        raw_response = response.text.strip()

        print("🔥 RAW GEMINI RESPONSE:", raw_response)  # Debugging Step

        json_data = extract_json_from_text(raw_response)

        if json_data:
            json_data = validate_marks_data(json_data)  # ✅ Apply validation fixes

        return json_data if json_data else None

    except Exception as e:
        print(f"❌ Gemini AI Error: {e}")
    
    return None

def extract_json_from_text(text):
    try:
        json_match = re.search(r'\{.*\}', text, re.DOTALL)
        if json_match:
            return json.loads(json_match.group())
        return None
    except json.JSONDecodeError as e:
        print(f"❌ JSON Decode Error: {e}")
        return None

# -------------------------------------
# RUN FLASK APP
# -------------------------------------
if __name__ == "__main__":
    app.run(debug=True)
