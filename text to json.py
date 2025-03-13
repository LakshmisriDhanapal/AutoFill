import google.generativeai as genai
import json

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
