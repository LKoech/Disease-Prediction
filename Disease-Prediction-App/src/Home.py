import streamlit as st
import streamlit_authenticator_mongo as stauth
import os
import yaml
import time
from pymongo import MongoClient

print("Current working directory:", os.getcwd())

# Debugging: List all files in the current working directory
print("Files in the working directory:", os.listdir(os.getcwd()))

# Set page configuration
st.set_page_config(page_title="Disease Detection", page_icon="⚕️")

# Load configuration for authentication
with open('Disease-Prediction-App/config.yaml', 'r') as file:
    config = yaml.load(file, Loader=yaml.SafeLoader)

# Connect to MongoDB
uri = "mongodb+srv://seremharriet:1234@diseasedetectioncluster.s54mk.mongodb.net/?retryWrites=true&w=majority&appName=DiseaseDetectionCluster"
client = MongoClient(uri)
db = client["Appdb"]
collection = db["users"]

# Initialize the authenticator
authenticator = stauth.Authenticate(
    collection,
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days']
)

# Create a login form
name, authentication_status, username = authenticator.login('Login', 'main')

# Handle authentication status
if authentication_status:
    # If authenticated, display the app content
    with st.sidebar:
        authenticator.logout('Logout', 'sidebar', key='unique_key')

    st.title("⚕️ Disease Detection")
    st.write(f"Welcome *{name}* to the Disease Detection App!")

    # Add content, like images or other app features here
    IMAGES = [
        "static/cancer.jpg",
        "static/bloodplates.jpg",
        "static/diabetes2.jpg",
        "static/disease-detect.jpg",
        "static/heartImage.jpg",
        "static/liver.png",
        "static/thyriod.jpg",
        "static/cancer2.jpg",
        "static/heart1.jpg",
        "static/diabetes.jpg",
        "static/kidney.jpg"
    ]

    def auto_slide_images(images, interval=2):
        image_placeholder = st.empty()
        num_images = len(images)

        while True:
            for i in range(num_images):
                image_placeholder.image(images[i], use_column_width=True)
                time.sleep(interval)

    # Call the function to display images automatically
    auto_slide_images(IMAGES, interval=2)

elif authentication_status == False:
    # If login failed (invalid username or password)
    st.error('Username/password is incorrect')

elif authentication_status == None:
    # If no credentials entered
    st.warning('Please enter correct username and password')
