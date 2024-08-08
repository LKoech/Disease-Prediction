import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

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

# Paths to the saved models
lung_cancer_model_path = os.path.join(working_dir, '..', 'Models', 'lung_cancer_model.sav')
prostate_cancer_model_path = os.path.join(working_dir, '..', 'Models', 'prostate_cancer_model.sav')

# Load the models
try:
    lung_cancer_model = load_model(lung_cancer_model_path)
    prostate_cancer_model = load_model(prostate_cancer_model_path)
except Exception as e:
    st.error(f"Error loading models: {e}")
    st.stop()

def display():
    st.title("Oncology")
    st.write("This section covers various aspects of Oncology diseases and their detection.")

    # Sidebar for navigation
    with st.sidebar:
        selected = option_menu(
            menu_title='Disease Prediction System',
            options=['Lung Cancer Prediction', 'Prostate Cancer Prediction'],
            icons=['lungs', 'droplet'],
            menu_icon='hospital-fill',
            default_index=0
        )

    def get_user_inputs(input_labels):
        inputs = []
        num_columns = 3  # Number of columns you want
        columns = st.columns(num_columns)
        for i, label in enumerate(input_labels):
            inputs.append(columns[i % num_columns].text_input(label))
        return inputs

    # Lung Cancer Prediction Page
    if selected == 'Lung Cancer Prediction':
        st.header('Lung Cancer Prediction using ML')

        lung_cancer_labels = [
            'Index', 'Patient ID', 'Age', 'Gender (M/F)', 'Air Pollution', 'Alcohol Use',
            'Dust Allergy', 'Occupational Hazards', 'Genetic Risk', 'Chronic Lung Disease',
            'Balanced Diet', 'Obesity', 'Smoking', 'Passive Smoker', 'Chest Pain',
            'Coughing of Blood', 'Fatigue', 'Weight Loss', 'Shortness of Breath',
            'Wheezing', 'Swallowing Difficulty', 'Clubbing of Finger Nails',
            'Frequent Cold', 'Dry Cough', 'Snoring', 'Level'
        ]

        user_input = get_user_inputs(lung_cancer_labels)

        lung_cancer_diagnosis = ''

        if st.button('Lung Cancer Test Result'):
            try:
                user_input = [float(x) if x.replace('.', '', 1).isdigit() else (1 if x.upper() == 'M' else 0) for x in user_input]
                lung_cancer_prediction = lung_cancer_model.predict([user_input])

                if lung_cancer_prediction[0] == 0:
                    lung_cancer_diagnosis = 'The patient is likely to have a Low level of cancer'
                elif lung_cancer_prediction[0] == 1:
                    lung_cancer_diagnosis = 'The patient is likely to have a Medium level of cancer'
                else:
                    lung_cancer_diagnosis = 'The patient is likely to have a High level of cancer'
            except ValueError:
                lung_cancer_diagnosis = 'Please enter valid numerical values.'

        st.success(lung_cancer_diagnosis)

    # Prostate Cancer Prediction Page
    elif selected == 'Prostate Cancer Prediction':
        st.header('Prostate Cancer Prediction using ML')

        prostate_cancer_labels = [
            'Radius', 'Texture', 'Perimeter', 'Area',
            'Smoothness', 'Compactness', 'Symmetry', 'Fractal Dimension'
        ]

        user_input = get_user_inputs(prostate_cancer_labels)

        prostate_cancer_diagnosis = ''

        if st.button('Prostate Cancer Test Result'):
            try:
                user_input = [float(x) if x.replace('.', '', 1).isdigit() else 0 for x in user_input]
                prostate_cancer_prediction = prostate_cancer_model.predict([user_input])

                if prostate_cancer_prediction[0] == 1:
                    prostate_cancer_diagnosis = 'The patient is likely to have Prostate Cancer'
                else:
                    prostate_cancer_diagnosis = 'The patient is not likely to have Prostate Cancer'
            except ValueError:
                prostate_cancer_diagnosis = 'Please enter valid numerical values.'

        st.success(prostate_cancer_diagnosis)

