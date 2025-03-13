# import google.generativeai as genai
# import os
# import json

# genai.configure(api_key="AIzaSyA9V_py5ak0lmNziGdvLd7qsWpc2pwDH6I")

# model = genai.GenerativeModel("gemini-1-pro")
# models = genai.list_models()
# for model in models:
#     print(model.name)

# def convert_text_to_json(extracted_text):
#     """Converts extracted text to structured JSON using Gemini API"""
#     model = genai.GenerativeModel("gemini-pro")

#     # Prompt Gemini to convert text into structured JSON format
#     prompt = f"Convert the following text into a well-structured JSON format:\n\n{extracted_text}"
    
#     response = model.generate_content(prompt)

#     return response.text  # Returns JSON response as a string

# def save_json_to_file(json_data, output_file):
#     """Saves JSON data to a file"""
#     try:
#         with open(output_file, "w", encoding="utf-8") as json_file:
#             json.dump(json_data, json_file, indent=4, ensure_ascii=False)
#         print(f"JSON data successfully saved to {output_file}")
#     except Exception as e:
#         print(f"Error writing to JSON file: {e}")

# # Example usage
# extracted_text = "Name: John Doe\nAge: 30\nCity: New York"  # Replace with OCR output
# json_output = convert_text_to_json(extracted_text)

# # Save to file
# json_filename = "output.json"
# save_json_to_file(json_output, json_filename)

import google.generativeai as genai
import json

# Configure the API
genai.configure(api_key="AIzaSyA9V_py5ak0lmNziGdvLd7qsWpc2pwDH6I")

# Load the model
model = genai.GenerativeModel("gemini-1.5-pro-latest")

# Read the file content with proper encoding and error handling
file_path = "C:/Users/laksh/OneDrive/Desktop/AutoFill/text_output/12TH MARKSHEET-03062024102441420.txt"
with open(file_path, "r", encoding="utf-8", errors="ignore") as file:
    extracted_text = file.read()

# Prompt with explicit instructions for JSON formatting
prompt = f"""
Convert the following text into a valid JSON format.
Ensure that the response is strictly valid JSON without any extra text or explanations.

Text:
{extracted_text}
"""

# Generate response
response = model.generate_content(prompt, request_options={"timeout": 240})

# Extract response text
json_output = response.text.strip()

# Ensure the response is valid JSON
try:
    json_data = json.loads(json_output)  # Convert string to JSON
except json.JSONDecodeError:
    print("❌ Error: The response is not valid JSON. Attempting to fix it...")

    # Try to extract valid JSON from response (if Gemini adds unwanted text)
    json_start = json_output.find("{")  # Find first occurrence of '{'
    json_end = json_output.rfind("}")   # Find last occurrence of '}'

    if json_start != -1 and json_end != -1:
        json_fixed = json_output[json_start : json_end + 1]  # Extract only JSON part
        try:
            json_data = json.loads(json_fixed)  # Try loading it again
            print("✅ JSON was fixed successfully!")
        except json.JSONDecodeError:
            print("❌ Error: Unable to extract valid JSON. Please check the AI response.")
            exit()
    else:
        print("❌ Error: No valid JSON structure found.")
        exit()

# Pretty-print JSON output
formatted_json = json.dumps(json_data, indent=4, ensure_ascii=False)

# Save JSON to a file
output_file_path = "C:/Users/laksh/OneDrive/Desktop/AutoFill/json_output.json"
with open(output_file_path, "w", encoding="utf-8") as json_file:
    json_file.write(formatted_json)

print("✅ JSON has been successfully saved to:", output_file_path)
