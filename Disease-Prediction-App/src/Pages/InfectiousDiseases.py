import os
import pickle
import streamlit as st
import lightgbm as lgb

# Set page configuration
st.set_page_config(
    page_title="Infectious Disease Detection",
    page_icon="🦠"
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

# Path to the saved model
hepatitis_c_model_path = os.path.join(working_dir, '..', 'Models', 'hepatitis_c_model.sav')

# Load the model
try:
    hepatitis_c_model = load_model(hepatitis_c_model_path)
except Exception as e:
    st.error(f"Error loading models: {e}")
    st.stop()

def display():
    st.title("Infectious Diseases")
    st.write("This section covers various aspects of Infectious Diseases and their detection.")

    st.title('Hepatitis C Prediction using ML')

    # Organize input fields into columns
    col1, col2, col3 = st.columns(3)

    with col1:
        category = st.text_input('Category')
        alb = st.text_input('ALB')
        ast = st.text_input('AST')
        chol = st.text_input('CHOL')
        prot = st.text_input('PROT')

    with col2:
        age = st.text_input('Age')
        alp = st.text_input('ALP')
        bil = st.text_input('BIL')
        crea = st.text_input('CREA')

    with col3:
        sex = st.text_input('Sex (M/F)')
        alt = st.text_input('ALT')
        che = st.text_input('CHE')
        ggt = st.text_input('GGT')

    hep_c_diagnosis = ''

    if st.button('Hepatitis C Test Result'):
        user_input = [
            category, age, sex, alb, alp, alt, ast, bil, che, chol,
            crea, ggt, prot
        ]
        try:
            # Convert inputs to appropriate types
            user_input = [float(x) if x.replace('.', '', 1).isdigit() else (1 if x.upper() == 'M' else 0) for x in user_input]
            hep_c_prediction = hepatitis_c_model.predict([user_input])

            if hep_c_prediction[0] == 1:
                hep_c_diagnosis = 'This person is at risk of Hepatitis C'
            else:
                hep_c_diagnosis = 'This person is not at risk of Hepatitis C'
        except ValueError:
            hep_c_diagnosis = 'Please enter valid numerical values.'

    st.success(hep_c_diagnosis)

# Run the display function
display()
