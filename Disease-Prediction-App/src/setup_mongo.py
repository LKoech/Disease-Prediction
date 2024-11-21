from pymongo import MongoClient
import streamlit_authenticator_mongo as stauth
import os

# Fetch MongoDB credentials from environment variables (recommended for security)
username = os.getenv('MONGO_USER')
password = os.getenv('MONGO_PASSWORD')
cluster_uri = os.getenv('MONGO_CLUSTER_URI')  # e.g., "cluster0.mongodb.net"

# MongoDB URI for the cluster
uri = f"mongodb+srv://seremharriet:1234@diseasedetectioncluster.s54mk.mongodb.net/?retryWrites=true&w=majority&appName=DiseaseDetectionCluster"

# Connect to MongoDB
client = MongoClient(uri)
db = client["Appdb"]  # Use your actual database name
collection = db["users"]  # Use your actual collection name

# Insert a user into the MongoDB collection
doc = {
    'username': 'Johnny',
    'password': stauth.Hasher(['dog']).generate()[0],  # Replace 'dog' with a secure password
    'email': 'johnwick@wicked.com',
    'name': 'John Wick'
}

collection.insert_one(doc)
print("User inserted successfully!")





