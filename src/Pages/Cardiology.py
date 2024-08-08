import os
import pickle
import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Cardiology Disease Detection",
    page_icon="🫀"
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

# Initialize session state if not already set
if 'current_page' not in st.session_state:
    st.session_state.current_page = ""

# Display function for Cardiology section
def display():
    st.title("Cardiology")
    st.write("This section covers various aspects of cardiology diseases and their detection.")

# Run the display function for Cardiology
display()

# Arrange buttons in columns
col1, col2 = st.columns(2)

with col1:
    if st.button("Heart Disease Prediction"):
        st.session_state.current_page = "Heart Disease Prediction"

with col2:
    if st.button("Heart Attack Prediction"):
        st.session_state.current_page = "Heart Attack Prediction"

# Display the selected page's content
current_page = st.session_state.current_page
if current_page:
    st.write(f"**{current_page}**")

    if current_page == "Heart Disease Prediction":
        # Path to the saved Heart Disease model
        heart_disease_model_path = os.path.join(working_dir, '..', 'Models', 'heart_disease_model.sav')

        # Load the Heart Disease model
        try:
            heart_disease_model = load_model(heart_disease_model_path)
        except Exception as e:
            st.error(f"Error loading Heart Disease model: {e}")
            st.stop()

        # Input fields for Heart Disease Prediction
        col1, col2, col3 = st.columns(3)
        with col1:
            age = st.text_input('Age')
            trestbps = st.text_input('Resting Blood Pressure')
            restecg = st.text_input('Resting Electrocardiographic results')
            oldpeak = st.text_input('ST depression induced by exercise')
            thal = st.text_input('Thal: 0 = normal; 1 = fixed defect; 2 = reversible defect')
        with col2:
            sex = st.text_input('Sex')
            chol = st.text_input('Serum Cholesterol in mg/dl')
            thalach = st.text_input('Maximum Heart Rate achieved')
            slope = st.text_input('Slope of the peak exercise ST segment')
        with col3:
            cp = st.text_input('Chest Pain types')
            fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
            exang = st.text_input('Exercise Induced Angina')
            ca = st.text_input('Major vessels colored by fluoroscopy')

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

    elif current_page == "Heart Attack Prediction":
        # Path to the saved Heart Attack model
        heart_attack_model_path = os.path.join(working_dir, '..', 'Models', 'heart_attack_model.sav')

        # Load the Heart Attack model
        try:
            heart_attack_model = load_model(heart_attack_model_path)
        except Exception as e:
            st.error(f"Error loading Heart Attack model: {e}")
            st.stop()

        # Input fields for Heart Attack Prediction
        col1, col2, col3 = st.columns(3)
        with col1:
            age = st.text_input('Age')
            trtbps = st.text_input('Resting Blood Pressure (in mm Hg)')
            restecg = st.text_input('Resting Electrocardiographic Results (0-2)')
            oldpeak = st.text_input('Oldpeak (ST depression induced by exercise relative to rest)')
            thall = st.text_input('Thalassemia (1 = normal; 2 = fixed defect; 3 = reversible defect)')
        with col2:
            sex = st.text_input('Sex (1 = male; 0 = female)')
            chol = st.text_input('Serum Cholesterol (in mg/dl)')
            thalachh = st.text_input('Maximum Heart Rate Achieved')
            slp = st.text_input('Slope of the Peak Exercise ST Segment (0-2)')
        with col3:
            cp = st.text_input('Chest Pain Type (0-3)')
            fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl (1 = true; 0 = false)')
            exng = st.text_input('Exercise Induced Angina (1 = yes; 0 = no)')
            caa = st.text_input('Number of Major Vessels (0-3) Colored by Fluoroscopy')

        heart_attack_diagnosis = ''
        if st.button('Heart Attack Test Result'):
            user_input = [age, sex, cp, trtbps, chol, fbs, restecg, thalachh, exng, oldpeak, slp, caa, thall]
            try:
                user_input = [float(x) for x in user_input]
                heart_prediction = heart_attack_model.predict([user_input])
                if heart_prediction[0] == 1:
                    heart_attack_diagnosis = 'This person is at risk of a heart attack'
                else:
                    heart_attack_diagnosis = 'This person is not at risk of a heart attack'
            except ValueError:
                heart_attack_diagnosis = 'Please enter valid numerical values.'

        st.success(heart_attack_diagnosis)

else:
    st.write("Please select a prediction model by clicking one of the buttons above.")
