import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

def load_model(model_path):
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"The model file was not found at {model_path}")
    try:
        with open(model_path, 'rb') as model_file:
            return pickle.load(model_file)
    except Exception as e:
        raise RuntimeError(f"Failed to load the model from {model_path}. Error: {e}")

# Getting the working directory of the main.py
working_dir = os.path.dirname(os.path.abspath(__file__))

# Constructing the paths for the saved models
heart_disease_model_path = os.path.join(working_dir, '..', 'Models', 'heart_disease_model.sav')
heart_attack_model_path = os.path.join(working_dir, '..', 'Models', 'heart_attack_model.sav')

# Loading the saved models
try:
    heart_disease_model = load_model(heart_disease_model_path)
    heart_attack_model = load_model(heart_attack_model_path)
except Exception as e:
    st.error(f"Error loading models: {e}")
    st.stop()

def display():
    st.title("Cardiology")
    st.write("This section covers various aspects of cardiology diseases and their detection.")

    # Sidebar for navigation
    with st.sidebar:
        selected = option_menu(
            menu_title='Multiple Disease Prediction System',
            options=['Heart Disease Prediction', 'Heart Attack Prediction'],
            icons=['heart', 'activity'],
            menu_icon='hospital-fill',
            default_index=0
        )



    # Heart Disease Prediction Page
    if selected == 'Heart Disease Prediction':
        st.title('Heart Disease Prediction using ML')

        col1, col2, col3 = st.columns(3)

        with col1:
            age = st.text_input('Age')
        with col2:
            sex = st.text_input('Sex')
        with col3:
            cp = st.text_input('Chest Pain types')
        with col1:
            trestbps = st.text_input('Resting Blood Pressure')
        with col2:
            chol = st.text_input('Serum Cholesterol in mg/dl')
        with col3:
            fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
        with col1:
            restecg = st.text_input('Resting Electrocardiographic results')
        with col2:
            thalach = st.text_input('Maximum Heart Rate achieved')
        with col3:
            exang = st.text_input('Exercise Induced Angina')
        with col1:
            oldpeak = st.text_input('ST depression induced by exercise')
        with col2:
            slope = st.text_input('Slope of the peak exercise ST segment')
        with col3:
            ca = st.text_input('Major vessels colored by fluoroscopy')
        with col1:
            thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversible defect')

        heart_diagnosis = ''

        if st.button('Heart Disease Test Result'):
            user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
            try:
                user_input = [float(x) for x in user_input]
                heart_prediction = heart_disease_model.predict([user_input])
                if heart_prediction[0] == 1:
                    heart_diagnosis = 'This person has heart disease'
                else:
                    heart_diagnosis = 'This person does not have heart disease'
            except ValueError:
                heart_diagnosis = 'Please enter valid numerical values.'

        st.success(heart_diagnosis)

    # Heart Attack Prediction Page
    if selected == 'Heart Attack Prediction':
        st.title('Heart Attack Prediction using ML')

        col1, col2, col3 = st.columns(3)

        with col1:
            age = st.text_input('Age')
        with col2:
            sex = st.text_input('Sex (1 = male; 0 = female)')
        with col3:
            cp = st.text_input('Chest Pain Type (0-3)')
        with col1:
            trtbps = st.text_input('Resting Blood Pressure (in mm Hg)')
        with col2:
            chol = st.text_input('Serum Cholesterol (in mg/dl)')
        with col3:
            fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl (1 = true; 0 = false)')
        with col1:
            restecg = st.text_input('Resting Electrocardiographic Results (0-2)')
        with col2:
            thalachh = st.text_input('Maximum Heart Rate Achieved')
        with col3:
            exng = st.text_input('Exercise Induced Angina (1 = yes; 0 = no)')
        with col1:
            oldpeak = st.text_input('Oldpeak (ST depression induced by exercise relative to rest)')
        with col2:
            slp = st.text_input('Slope of the Peak Exercise ST Segment (0-2)')
        with col3:
            caa = st.text_input('Number of Major Vessels (0-3) Colored by Fluoroscopy')
        with col1:
            thall = st.text_input('Thalassemia (1 = normal; 2 = fixed defect; 3 = reversible defect)')

        heart_diagnosis = ''

        if st.button('Heart Attack Test Result'):
            user_input = [age, sex, cp, trtbps, chol, fbs, restecg, thalachh, exng, oldpeak, slp, caa, thall]
            try:
                user_input = [float(x) for x in user_input]
                heart_prediction = heart_attack_model.predict([user_input])
                if heart_prediction[0] == 1:
                    heart_diagnosis = 'This person is at risk of a heart attack'
                else:
                    heart_diagnosis = 'This person is not at risk of a heart attack'
            except ValueError:
                heart_diagnosis = 'Please enter valid numerical values.'

        st.success(heart_diagnosis)


