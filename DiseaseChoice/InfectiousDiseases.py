import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import lightgbm as lgb


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

    # Sidebar for navigation
    with st.sidebar:
        selected = option_menu(
            menu_title='Disease Prediction System',
            options=['Hepatitis C Prediction'],
            icons=['activity'],
            menu_icon='hospital-fill',
            default_index=0
        )

    # Hepatitis C Prediction Page
    if selected == 'Hepatitis C Prediction':
        st.title('Hepatitis C Prediction using ML')

        # Organize input fields into columns
        col1, col2, col3 = st.columns(3)

        with col1:
            category = st.text_input('Category')
        with col2:
            age = st.text_input('Age')
        with col3:
            sex = st.text_input('Sex (M/F)')
        with col1:
            alb = st.text_input('ALB')
        with col2:
            alp = st.text_input('ALP')
        with col3:
            alt = st.text_input('ALT')
        with col1:
            ast = st.text_input('AST')
        with col2:
            bil = st.text_input('BIL')
        with col3:
            che = st.text_input('CHE')
        with col1:
            chol = st.text_input('CHOL')
        with col2:
            crea = st.text_input('CREA')
        with col3:
            ggt = st.text_input('GGT')
        with col1:
            prot = st.text_input('PROT')

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
