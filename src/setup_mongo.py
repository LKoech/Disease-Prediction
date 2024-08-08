from pymongo import MongoClient
import streamlit_authenticator_mongo as stauth
import secrets
# Connect to MongoDB
uri = "mongodb+srv://sweet_magnolias:123Angukanayo123@cluster0.rsqta0a.mongodb.net/"
client = MongoClient(uri)
db = client["diseaseDetect"]  # Use your actual database name
collection = db["DiseaseDetect"]  # Use your actual collection name

# Insert a user into the MongoDB collection
doc = {
    'username': 'Johnny',
    'password': stauth.Hasher(['dog']).generate()[0],  # Replace 'dog' with a secure password
    'email': 'johnwick@wicked.com',
    'name': 'John Wick'
}

collection.insert_one(doc)
print("User inserted successfully!")




