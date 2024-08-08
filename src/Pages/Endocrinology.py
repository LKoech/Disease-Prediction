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
diabetes_model_path = os.path.join(working_dir, '..', 'Models', 'diabetes_model.sav')
liver_disease_model_path = os.path.join(working_dir, '..', 'Models', 'liver_disease_model.sav')
hypothyroidism_model_path = os.path.join(working_dir, '..', 'Models', 'hypothyroidism_model.sav')

# Load the models
try:
    diabetes_model = load_model(diabetes_model_path)
    liver_disease_model = load_model(liver_disease_model_path)
    hypothyroidism_model = load_model(hypothyroidism_model_path)
except Exception as e:
    st.error(f"Error loading models: {e}")
    st.stop()

def display():
    st.title("Endocrinology")
    st.write("This section covers various aspects of endocrinology, focusing on the detection of common endocrine disorders.")

    # Sidebar for navigation
    with st.sidebar:
        selected = option_menu(
            menu_title='Multiple Disease Prediction System',
            options=['Diabetes Prediction', 'Liver Disease Prediction', 'Hypothyroidism Prediction'],
            icons=['activity', 'droplet', 'activity'],
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

    def handle_prediction(model, user_input, result_message):
        try:
            user_input = [float(x) if x not in ['yes', 'no'] else (1 if x == 'yes' else 0) for x in user_input]
            prediction = model.predict([user_input])
            if prediction[0] == 1:
                return f"This person {result_message}"
            else:
                return f"This person does not {result_message}"
        except ValueError:
            return 'Please enter valid numerical values.'

    # Diabetes Prediction Page
    if selected == 'Diabetes Prediction':
        st.title('Diabetes Prediction using ML')

        diabetes_labels = [
            'Number of Pregnancies', 'Glucose Level', 'Blood Pressure value',
            'Skin Thickness value', 'Insulin Level', 'BMI value',
            'Diabetes Pedigree Function value', 'Age of the Person'
        ]

        user_input = get_user_inputs(diabetes_labels)

        if st.button('Diabetes Test Result'):
            diagnosis = handle_prediction(diabetes_model, user_input, 'is diabetic')
            st.success(diagnosis)

    # Liver Disease Prediction Page
    if selected == 'Liver Disease Prediction':
        st.title('Liver Disease Prediction using ML')

        liver_labels = [
            'Age', 'Gender (1 = male; 0 = female)', 'BMI',
            'Alcohol Consumption (units per week)', 'Smoking (1 = yes; 0 = no)',
            'Genetic Risk (1 = yes; 0 = no)', 'Physical Activity (hours per week)',
            'Diabetes (1 = yes; 0 = no)', 'Hypertension (1 = yes; 0 = no)',
            'Liver Function Test (1 = abnormal; 0 = normal)'
        ]

        user_input = get_user_inputs(liver_labels)

        if st.button('Liver Disease Test Result'):
            diagnosis = handle_prediction(liver_disease_model, user_input, 'is at risk of liver disease')
            st.success(diagnosis)

    # Hypothyroidism Prediction Page
    if selected == 'Hypothyroidism Prediction':
        st.title('Hypothyroidism Prediction using ML')

        hypothyroidism_labels = [
            'Age', 'Sex (1 = male; 0 = female)', 'On Thyroxine (1 = yes; 0 = no)',
            'Query on Thyroxine (1 = yes; 0 = no)', 'On Antithyroid Medication (1 = yes; 0 = no)',
            'Sick (1 = yes; 0 = no)', 'Pregnant (1 = yes; 0 = no)',
            'Thyroid Surgery (1 = yes; 0 = no)', 'I131 Treatment (1 = yes; 0 = no)',
            'Query Hypothyroid (1 = yes; 0 = no)', 'Query Hyperthyroid (1 = yes; 0 = no)',
            'Lithium (1 = yes; 0 = no)', 'Goitre (1 = yes; 0 = no)',
            'Tumor (1 = yes; 0 = no)', 'Hypopituitary (1 = yes; 0 = no)',
            'Psych (1 = yes; 0 = no)', 'TSH Measured (1 = yes; 0 = no)',
            'TSH', 'T3 Measured (1 = yes; 0 = no)', 'T3', 'TT4 Measured (1 = yes; 0 = no)',
            'TT4', 'T4U Measured (1 = yes; 0 = no)', 'T4U', 'FTI Measured (1 = yes; 0 = no)',
            'FTI', 'TBG Measured (1 = yes; 0 = no)', 'TBG', 'Referral Source'
        ]

        user_input = get_user_inputs(hypothyroidism_labels)

        if st.button('Hypothyroidism Test Result'):
            diagnosis = handle_prediction(hypothyroidism_model, user_input, 'is at risk of Hypothyroidism')
            st.success(diagnosis)

