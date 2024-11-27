import streamlit as st
import streamlit_authenticator_mongo as stauth
import os
import yaml
import time
from pymongo import MongoClient

# Set page configuration
st.set_page_config(page_title="Disease Detection", page_icon="⚕️")

# Dynamically get the path to the config file
config_path = os.path.join(os.path.dirname(__file__), 'config.yaml')

# Load configuration for authentication
try:
    with open(config_path, 'r') as file:
        config = yaml.load(file, Loader=yaml.SafeLoader)
except FileNotFoundError:
    st.error(f"The config.yaml file was not found at the expected path: {config_path}")
    st.stop()  # Stop the app if the file is not found

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

    # Dynamically construct paths to images
    current_dir = os.path.dirname(os.path.abspath(__file__))
    IMAGES = [
        os.path.join(current_dir, "static", "cancer.jpg"),
        os.path.join(current_dir, "static", "bloodplates.jpg"),
        os.path.join(current_dir, "static", "diabetes2.jpg"),
        os.path.join(current_dir, "static", "disease-detect.jpg"),
        os.path.join(current_dir, "static", "heartImage.jpg"),
        os.path.join(current_dir, "static", "liver.png"),
        os.path.join(current_dir, "static", "thyriod.jpg"),
        os.path.join(current_dir, "static", "cancer2.jpg"),
        os.path.join(current_dir, "static", "heart1.jpg"),
        os.path.join(current_dir, "static", "diabetes.jpg"),
        os.path.join(current_dir, "static", "kidney.jpg"),
    ]

    def display_image_carousel(images, interval=2):
        """
        Function to display a carousel of images.
        """
        placeholder = st.empty()  # Create a placeholder for images
        num_images = len(images)

        for _ in range(num_images * 3):  # Loop through images multiple times
            for i in range(num_images):
                placeholder.image(images[i], use_column_width=True)
                time.sleep(interval)  # Wait for the specified interval before showing the next image

    # Call the carousel function
    display_image_carousel(IMAGES, interval=2)

elif authentication_status == False:
    # If login failed (invalid username or password)
    st.error('Username/password is incorrect')

elif authentication_status == None:
    # If no credentials entered
    st.warning('Please enter your username and password')
