import streamlit as st
import streamlit_authenticator_mongo as stauth
import yaml
import os
from pymongo import MongoClient

# Set page configuration
st.set_page_config(page_title="Disease Detection", page_icon="⚕️")

# Load configuration for authentication
config_path = os.path.join('src', 'config.yaml')
if not os.path.exists(config_path):
    st.error("Configuration file not found!")
    st.stop()

with open(config_path) as file:
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
    # If authenticated, set a session state variable
    st.session_state['authenticated'] = True

    # Sidebar for navigation
    with st.sidebar:
        authenticator.logout('Logout', 'sidebar', key='unique_key')
        page = st.radio("Navigate", ["Home", "About", "Contact"])

    # Display content based on selected page
    if page == "Home":
        st.title("⚕️ Disease Detection")
        st.write(f"Welcome, *{name}*, to the Disease Detection App!")
        # Add more content for the home page
        st.write("This is the home page.")

    elif page == "About":
        st.title("About Us")
        st.write("This app helps detect diseases using AI/ML models.")

    elif page == "Contact":
        st.title("Contact Us")
        st.write("Reach out to us at support@diseasedetection.com")

elif authentication_status == False:
    st.error('Username/password is incorrect')

elif authentication_status == None:
    st.warning('Please enter your username and password')
