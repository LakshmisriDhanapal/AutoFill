import os
from google.cloud import vision
from google.cloud.vision_v1 import types

# Set Google Cloud credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:/Users/laksh/Downloads/ocr-model-451910-c14b246a31ed.json"

def extract_text_from_image(image_path):
    """Extracts text from an image using Google Vision API"""
    client = vision.ImageAnnotatorClient()
    with open(image_path, "rb") as image_file:
        content = image_file.read()
    
    image = types.Image(content=content)
    response = client.text_detection(image=image)
    texts = response.text_annotations
    extracted_text = texts[0].description if texts else ""
    
    print(f"Extracted text from {image_path}:\n", extracted_text, "\n" + "-"*50)
    
    return extracted_text

def save_text_to_file(text, output_file):
    """Saves the extracted text to a text file"""
    try:
        with open(output_file, "w", encoding="utf-8") as text_file:
            text_file.write(text)
        print(f"Extracted text successfully saved to {output_file}")
    except Exception as e:
        print(f"Error writing to text file: {e}")

def process_images_in_folder(folder_path, output_folder):
    """Processes all images in a folder and saves extracted text to text files"""
    if not os.path.exists(folder_path):
        print("Error: Folder not found!")
        return

    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    image_files = [f for f in os.listdir(folder_path) if f.lower().endswith((".png", ".jpg", ".jpeg"))]

    if not image_files:
        print("No images found in the folder!")
        return

    for image_file in image_files:
        image_path = os.path.join(folder_path, image_file)
        extracted_text = extract_text_from_image(image_path)
        
        # Save the extracted text to a text file
        output_file = os.path.join(output_folder, f"{os.path.splitext(image_file)[0]}.txt")
        save_text_to_file(extracted_text, output_file)

# Folder containing images
folder_path = "C:/Users/laksh/OneDrive/Desktop/AutoFill/image"
# Folder to save extracted text files
output_folder = "C:/Users/laksh/OneDrive/Desktop/AutoFill/text_output"
process_images_in_folder(folder_path, output_folder)