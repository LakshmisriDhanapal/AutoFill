from pymongo import MongoClient
import json

# Replace <username>, <password>, and <clustername> with your actual credentials
client = MongoClient("mongodb+srv")

# Connect to the database and collection
db = client["form_data"]
collection = db["extracted_data"]

# Example JSON data (Replace this with actual extracted JSON)
extracted_json ={
    "Board": "STATE BOARD OF SCHOOL EXAMINATIONS, TAMILNADU",
    "BoardTamil": "அரசுத் தேர்வுகள் துறை, சென்னை 600 006.",
    "BoardEnglish": "DEPARTMENT OF GOVERNMENT EXAMINATIONS, CHENNAI - 600 006.",
    "Examination": "HIGHER SECONDARY SECOND YEAR EXAMINATION",
    "ExaminationTamil": "மேல்நிலைப் பள்ளிக் கல்வி இரண்டாமாண்டு பொதுத்தேர்வு",
    "Statement": "STATEMENT OF MARKS",
    "StatementTamil": "மதிப்பெண் பட்டியல்",
    "Authority": "ISSUED UNDER THE AUTHORITY OF THE GOVERNMENT OF TAMILNADU",
    "AuthorityTamil": "தமிழ்நாடு அரசின் அதிகாரத்திற்கு உட்பட்டு வழங்கப்படுகிறது",
    "CandidateName": "********",
    "CandidateNameTamil": "*********",
    "Session": "*********",
    "SessionTamil": "*********",
    "RollNumber": ******,
    "DateOfBirth": "**/**/****",
    "PermanentRegistrationNumber": *****************,
    "TMRCodeAndDate": "*************",
    "EMISID": ***********,
    "MediumOfInstruction": "ENGLISH",
    "GroupCode": "2503(GENERAL)",
    "SchoolName": "************************************************",
    "SchoolNameTamil": "********************************************",
    "FirstYear": {
        "Subjects": [
            {
                "Subject": "TAMIL",
                "Theory": 84,
                "Practical": 10,
                "Internal": 10,
                "Total": 94,
                "Result": "P",
                "RollSessionYear": "*************"
            },
            {
                "Subject": "ENGLISH",
                "Theory": 82,
                "Practical": 10,
                "Internal": 10,
                "Total": 92,
                "Result": "P",
                "RollSessionYear": "***************"
            },
            {
                "Subject": "PHYSICS",
                "Theory": 60,
                "Practical": 20,
                "Internal": 10,
                "Total": 90,
                "Result": "P",
                "RollSessionYear": "*****************"
            },
            {
                "Subject": "CHEMISTRY",
                "Theory": 65,
                "Practical": 20,
                "Internal": 10,
                "Total": 95,
                "Result": "P",
                "RollSessionYear": "***********"
            },
            {
                "Subject": "BIOLOGY",
                "Theory": 64,
                "Practical": 20,
                "Internal": 10,
                "Total": 94,
                "Result": "P",
                "RollSessionYear": "***************"
            },
            {
                "Subject": "MATHEMATICS",
                "Theory": 78,
                "Practical": 10,
                "Internal": 10,
                "Total": 88,
                "Result": "P",
                "RollSessionYear": "*****************"
            }
        ],
        "TotalMarks": 553,
        "Result": "PASS"
    },

    "Note": "This is a Computer Generated Statement of Marks. The Candidates who have passed all the subjects in Higher Secondary First year and Second year Examinations are eligible for Higher Educations. The genuineness of Statement of Marks may be verified in the website https:\\apply1.tndge.org\\verify",
    "NoteTamil": "இம்மதிப்பெண் பட்டியல் கணினி மூலம் தயார் செய்யப்பட்டுள்ளது. மேல்நிலை முதலாமாண்டு மற்றும் இரண்டாமாண்டு பொதுத்தேர்வுகளில் அனைத்துப் பாடங்களிலும் தேர்ச்சி பெற்றவர்களே உயர்கல்விக்குத் தகுதியானவர் ஆவார். பட்டியலின் உண்மைத் தன்மையை பின்வரும் இணையதளத்தில் அறிந்து கொள்ளலாம். https:\\apply1.tndge.org\\verifiy",
    "CandidateSignature": "***********",
    "PrincipalSignature": "***********",
    "Principal": "************************************************",
    "MemberSecretary": "******************************************",
    "BoardTamilEnd": "மாநில பள்ளித் தேர்வுகள் குழுமம் தமிழ்நாடு"
}

# Insert JSON data into MongoDB
collection.insert_one(extracted_json)

print("Data successfully stored in MongoDB!")
