# Automatic_Form_Filling_System

AI Agent

### Auto Fill

## Overview
The Automatic Form Filling System is a deep learning and OCR-based solution designed to automate the admission form-filling process for universities. It allows users to upload scanned mark sheets or documents through a drag-and-drop interface, extracts structured information using OCR, and automatically populates predefined admission form fields. This reduces manual effort, minimizes errors, and accelerates the admission workflow.

## Features
-📂 Drag-and-drop document upload
-🔍 OCR-based text extraction using Google Vision API
-🧹 Preprocessing techniques: image enhancement, noise removal, text alignment
-📝 Automatic mapping of extracted data into admission form fields
-✅ Validation checks for data consistency and accuracy
-⚡ Fast performance – reduces form-filling time to under 30 seconds
-🗄️ Database integration for storing extracted information
-📅 Supports mark sheets of any academic year

## Tech Stack
-Deep Learning Frameworks: TensorFlow
-OCR Engine: Google Vision API
-AI Model: Google Gemini API (Text-to-Json)
-Frontend: HTML, CSS, JavaScript (Drag-and-Drop UI)
-Backend: Python (Flask)
-Database: MongoDB
  
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
- Interactive dashboard for student analytics

## Acknowledgments
- **Google Vision API**
- **Gemini API**
- **Flask & MongoDB Community**

## Contact
For support, contact lakshmisridhanapal@gmail.com

