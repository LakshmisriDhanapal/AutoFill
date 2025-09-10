from pymongo import MongoClient

client = MongoClient("mongodb/")
db = client["ocr_database"]
collection = db["extracted_data"]

# Print all documents
for doc in collection.find():
    print(doc)

