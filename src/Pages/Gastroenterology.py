import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(
    page_title="Gastroenterology Disease Detection",
    page_icon="💊"
)

# Function to load models safely
def load_model(model_path):
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"The model file was not found at {model_path}")
    try:
        with open(model_path, 'rb') as model_file:
            return pickle.load(model_file)
    except Exception as e:
        raise RuntimeError(f"Failed to load the model from {model_path}. Error: {e}")

# Get the working directory of the main.py
working_dir = os.path.dirname(os.path.abspath(__file__))

# Path to the saved Crohn's disease model
crohn_disease_model_path = os.path.join(working_dir, '..', 'Models', 'crohn_disease_model.sav')

# Load the Crohn's disease model
try:
    crohn_disease_model = load_model(crohn_disease_model_path)
except Exception as e:
    st.error(f"Error loading Crohn's Disease model: {e}")
    st.stop()

# Display function for Gastroenterology section
def display():
    st.title("Gastroenterology")
    st.write("This section covers various aspects of gastroenterology, focusing on the diagnosis and detection of related diseases.")

# Run the display function for Gastroenterology
display()

# Create a button for Crohn's Disease Prediction
if st.button("Crohn's Disease Prediction"):
    st.session_state.current_page = "Crohn's Disease Prediction"

# Display the selected page's content
current_page = st.session_state.current_page
if current_page == "Crohn's Disease Prediction":
    st.title("Crohn's Disease Prediction using ML")

    # Organize input fields into columns
    col1, col2, col3 = st.columns(3)

    with col1:
        sample = st.text_input('Sample')
        PCDAI = st.text_input('PCDAI')
        Erysipelotrichaceae = st.text_input('Erysipelotrichaceae')
        Pasteurellaceae = st.text_input('Pasteurellaceae')
        Veillonellaceae = st.text_input('Veillonellaceae')
        Verrucomicrobiaceae = st.text_input('Verrucomicrobiaceae')

    with col2:
        subject = st.text_input('Subject')
        race = st.text_input('Race')
        Neisseriaceae = st.text_input('Neisseriaceae')
        Bifidobacteriaceae = st.text_input('Bifidobacteriaceae')
        Enterobacteriaceae = st.text_input('Enterobacteriaceae')
        Gemellaceae = st.text_input('Gemellaceae')

    with col3:
        AB_exposure = st.text_input('AB Exposure (1 = yes; 0 = no)')
        sample_location = st.text_input('Sample Location')
        Clostridiales = st.text_input('Clostridiales')
        Fusobacteriaceae = st.text_input('Fusobacteriaceae')
        Micrococcaceae = st.text_input('Micrococcaceae')
        Coriobacteriaceae = st.text_input('Coriobacteriaceae')
        Bacteroidales = st.text_input('Bacteroidales')

    crohns_diagnosis = ''

    if st.button('Crohn\'s Disease Test Result'):
        user_input = [
            sample, subject, AB_exposure, PCDAI, race, sample_location,
            Erysipelotrichaceae, Neisseriaceae, Clostridiales, Pasteurellaceae,
            Bifidobacteriaceae, Fusobacteriaceae, Veillonellaceae, Enterobacteriaceae,
            Micrococcaceae, Verrucomicrobiaceae, Gemellaceae, Coriobacteriaceae, Bacteroidales
        ]

        try:
            # Convert inputs to float where possible, otherwise handle binary inputs
            user_input = [float(x) if x.replace('.', '', 1).isdigit() else (1 if x.lower() in ['yes', '1'] else 0) for x in user_input]
            crohns_prediction = crohn_disease_model.predict([user_input])

            # Interpret prediction
            if crohns_prediction[0] == 1:
                crohns_diagnosis = 'This person is at risk of Crohn\'s Disease'
            else:
                crohns_diagnosis = 'This person is not at risk of Crohn\'s Disease'
        except ValueError:
            crohns_diagnosis = 'Please enter valid numerical values.'

    # Display the diagnosis result
    st.success(crohns_diagnosis)


