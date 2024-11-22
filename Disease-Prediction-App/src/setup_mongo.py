from pymongo import MongoClient
import streamlit_authenticator_mongo as stauth
import os

# MongoDB URI setup
uri = f"mongodb+srv://seremharriet:1234@diseasedetectioncluster.s54mk.mongodb.net/?retryWrites=true&w=majority&appName=DiseaseDetectionCluster"

# Connect to MongoDB
client = MongoClient(uri)
db = client["Appdb"]
collection = db["users"]

def add_user():
    try:
        # Gather user details
        username = input("Enter username: ")
        password = input("Enter password: ")  # In production, use secure password input (e.g., getpass.getpass)
        email = input("Enter email: ")
        name = input("Enter full name: ")

        # Hash the password
        hashed_password = stauth.Hasher([password]).generate()[0]

        # Create the document
        doc = {
            'username': username,
            'password': hashed_password,
            'email': email,
            'name': name
        }

        # Insert into MongoDB
        collection.insert_one(doc)
        print(f"User '{username}' inserted successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function to add users
add_user()



