from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["ocr_database"]
collection = db["extracted_data"]

# Print all documents
for doc in collection.find():
    print(doc)
