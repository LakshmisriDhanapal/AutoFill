# AutoFill
AI Agent

### Automatic Form Filling System using Google Vision API

## Overview
This project implements an Automatic Form Filling System using Google Vision API's OCR technology. The goal is to extract text from uploaded images (e.g., marksheets, forms, or documents), convert it into JSON format, store it in MongoDB, and autofill forms based on the extracted data.

## Features
- **OCR Processing:** Extracts text from images using Google Vision API.
- **JSON Conversion:** Converts extracted text into structured JSON format using Gemini API .
- **MongoDB Storage:** Saves JSON data in a local MongoDB database.
- **Flask Web Application:** Provides a web interface for image upload and data retrieval.
- **Automatic Form Filling:** Autofills forms using stored JSON data.
- 
### Prerequisites
- Python (>=3.8)
- Google Cloud Project with Vision API enabled
- Google Cloud Service Account Key JSON
- MongoDB installed and running locally

## Usage
1. **Upload an Image:** Upload a marksheet or document containing text.
2. **Extract & Convert Data:** The system extracts text and converts it into JSON format.
3. **Store & Display Data:** The extracted JSON data is stored in MongoDB and displayed in the web interface.
4. **Autofill Forms:** Click "Autofill" to populate form fields using stored JSON data.

## Code Structure
- **app.py:** Main Flask application.
- **templates/**: HTML files for the frontend.
- **static/**: CSS and JavaScript files.
- **database.py:** Handles MongoDB connections.
- **ocr_processing.py:** Extracts text using Google Vision API.

## Model Architecture
The system follows a structured pipeline:
1. **Upload Image** → 2. **Extract Text with OCR** → 3. **Convert to JSON** → 4. **Store in MongoDB** → 5. **Autofill Forms**

## Key Components
- **Image Dimensions:** Optimized for various resolutions.
- **Database Handling:** Uses PyMongo for seamless MongoDB integration.
- **API Calls:** Uses Google Vision API for text extraction.

## Future Work
- Implement cloud-based MongoDB storage (MongoDB Atlas)
- Enhance UI for better user experience
- Add multi-document processing support


## Acknowledgments
- **Google Vision API**
- **Gemini API**
- **Flask & MongoDB Community**

## Contact
For support, contact lakshmisridhanapal@gmail.com

