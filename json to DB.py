from pymongo import MongoClient
import json

# Replace <username>, <password>, and <clustername> with your actual credentials
client = MongoClient("mongodb+srv://<lakshmisrid>:<5Kp35jeL31L4fMZ6>@<mongoCluster>.mongodb.net/?retryWrites=true&w=majority")

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
    "CandidateName": "ABINAYA R",
    "CandidateNameTamil": "அபிநயா ரா",
    "Session": "MAR 2024",
    "SessionTamil": "மார்ச் 2024",
    "RollNumber": 6411466,
    "DateOfBirth": "11/11/2006",
    "PermanentRegistrationNumber": 2313411263,
    "TMRCodeAndDate": "M1382324/06.05.2024",
    "EMISID": 2008898629,
    "MediumOfInstruction": "ENGLISH",
    "GroupCode": "2503(GENERAL)",
    "SchoolName": "GOKILAMBAL MATRIC HR SEC SCHOOL KUZHAVADAIYAN",
    "SchoolNameTamil": "கோகிலாம்பாள் மெட்ரிக்குலேஷன் மேனிலைப்பள்ளி",
    "FirstYear": {
        "Subjects": [
            {
                "Subject": "TAMIL",
                "Theory": 84,
                "Practical": 10,
                "Internal": 10,
                "Total": 94,
                "Result": "P",
                "RollSessionYear": "3411263 / MAR / 2023"
            },
            {
                "Subject": "ENGLISH",
                "Theory": 82,
                "Practical": 10,
                "Internal": 10,
                "Total": 92,
                "Result": "P",
                "RollSessionYear": "3411263 / MAR / 2023"
            },
            {
                "Subject": "PHYSICS",
                "Theory": 60,
                "Practical": 20,
                "Internal": 10,
                "Total": 90,
                "Result": "P",
                "RollSessionYear": "3411263/MAR/2023"
            },
            {
                "Subject": "CHEMISTRY",
                "Theory": 65,
                "Practical": 20,
                "Internal": 10,
                "Total": 95,
                "Result": "P",
                "RollSessionYear": "3411263/MAR/2023"
            },
            {
                "Subject": "BIOLOGY",
                "Theory": 64,
                "Practical": 20,
                "Internal": 10,
                "Total": 94,
                "Result": "P",
                "RollSessionYear": "3411263 / MAR / 2023"
            },
            {
                "Subject": "MATHEMATICS",
                "Theory": 78,
                "Practical": 10,
                "Internal": 10,
                "Total": 88,
                "Result": "P",
                "RollSessionYear": "3411263 / MAR / 2023"
            }
        ],
        "TotalMarks": 553,
        "Result": "PASS"
    },
    "SecondYear": {
        "Subjects": [
            {
                "Subject": "TAMIL",
                "Theory": 87,
                "Practical": 10,
                "Internal": 10,
                "Total": 97,
                "Result": "P",
                "RollSessionYear": "6411466 / MAR / 2024"
            },
            {
                "Subject": "ENGLISH",
                "Theory": 89,
                "Practical": 10,
                "Internal": 10,
                "Total": 99,
                "Result": "P",
                "RollSessionYear": "6411466/MAR/2024"
            },
            {
                "Subject": "PHYSICS",
                "Theory": 70,
                "Practical": 20,
                "Internal": 10,
                "Total": 100,
                "Result": "P",
                "RollSessionYear": "6411466 / MAR / 2024"
            },
            {
                "Subject": "CHEMISTRY",
                "Theory": 70,
                "Practical": 20,
                "Internal": 10,
                "Total": 100,
                "Result": "P",
                "RollSessionYear": "6411466/MAR/2024"
            },
            {
                "Subject": "BIOLOGY",
                "Theory": 70,
                "Practical": 20,
                "Internal": 10,
                "Total": 100,
                "Result": "P",
                "RollSessionYear": "6411466/MAR/2024"
            },
            {
                "Subject": "MATHEMATICS",
                "Theory": 89,
                "Practical": 10,
                "Internal": 10,
                "Total": 99,
                "Result": "P",
                "RollSessionYear": "6411466/MAR/2024"
            }
        ],
        "TotalMarks": 595,
        "Result": "PASS"
    },
    "Note": "This is a Computer Generated Statement of Marks. The Candidates who have passed all the subjects in Higher Secondary First year and Second year Examinations are eligible for Higher Educations. The genuineness of Statement of Marks may be verified in the website https:\\apply1.tndge.org\\verify",
    "NoteTamil": "இம்மதிப்பெண் பட்டியல் கணினி மூலம் தயார் செய்யப்பட்டுள்ளது. மேல்நிலை முதலாமாண்டு மற்றும் இரண்டாமாண்டு பொதுத்தேர்வுகளில் அனைத்துப் பாடங்களிலும் தேர்ச்சி பெற்றவர்களே உயர்கல்விக்குத் தகுதியானவர் ஆவார். பட்டியலின் உண்மைத் தன்மையை பின்வரும் இணையதளத்தில் அறிந்து கொள்ளலாம். https:\\apply1.tndge.org\\verifiy",
    "CandidateSignature": "R. Abinaya",
    "PrincipalSignature": "K.SELVAKUMAR",
    "Principal": "Gokilambal Matriculation Hr.Sec.School, NH-45C, KUZHAVATAYAN",
    "MemberSecretary": "MEMBER SECRETARY (HR.SEC)",
    "BoardTamilEnd": "மாநில பள்ளித் தேர்வுகள் குழுமம் தமிழ்நாடு"
}

# Insert JSON data into MongoDB
collection.insert_one(extracted_json)

print("Data successfully stored in MongoDB!")
