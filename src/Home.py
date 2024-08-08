import streamlit as st
import streamlit_authenticator_mongo as stauth
import yaml
import time
from pymongo import MongoClient

# Set page configuration
st.set_page_config(
    page_title="Disease Detection",
    page_icon="⚕️"
)

# Load configuration for authentication
with open('config.yaml') as file:
    config = yaml.load(file, Loader=yaml.SafeLoader)

# Connect to MongoDB
uri = "your-uri"
client = MongoClient(uri)
db = client["your-db-name"]  # Use your actual database name
collection = db["your-collection-name"]  # Use your actual collection name

# Initialize the authenticator
authenticator = stauth.Authenticate(
    collection,
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days']
)

# Create a login form
name, authentication_status, username = authenticator.login('Login', 'main')

if authentication_status:

    # Add the logout button in the sidebar
    with st.sidebar:
        authenticator.logout('Logout', 'sidebar', key='unique_key')

    st.title("⚕️ Disease Detection")
    st.write(
        f"Welcome  *{name}*  to the Disease Detection App! Here we use our Machine Learning models to assist in identifying the presence of various diseases.")

    # Images for the slideshow
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
        # Create an empty container to hold the image
        image_placeholder = st.empty()

        num_images = len(images)

        while True:
            for i in range(num_images):
                image_placeholder.image(images[i], use_column_width=True)
                time.sleep(interval)

    # Call the function to display the images automatically
    auto_slide_images(IMAGES, interval=2)

elif authentication_status == False:
    st.error('Username/password is incorrect')
elif authentication_status == None:
    st.warning('Please enter your username and password')
