import os
import pickle
import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Endocrinology Disease Detection",
    page_icon="🧬"
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

# Display function for Endocrinology section
def display():
    st.title("Endocrinology")
    st.write("This section covers various aspects of endocrinology, focusing on the detection of common endocrine disorders.")

# Run the display function for Endocrinology
display()

# Create three columns for the prediction models
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Diabetes Prediction"):
        st.session_state.current_page = "Diabetes Prediction"

with col2:
    if st.button("Liver Disease Prediction"):
        st.session_state.current_page = "Liver Disease Prediction"

with col3:
    if st.button("Hypothyroidism Prediction"):
        st.session_state.current_page = "Hypothyroidism Prediction"

# Display the selected page's content
current_page = st.session_state.current_page
if current_page:
    st.write(f"**{current_page}**")

    if current_page == "Diabetes Prediction":
        diabetes_model_path = os.path.join(working_dir, '..', 'Models', 'diabetes_model.sav')

        try:
            diabetes_model = load_model(diabetes_model_path)
        except Exception as e:
            st.error(f"Error loading Diabetes model: {e}")
            st.stop()

        # Input fields for Diabetes Prediction in columns
        col1, col2, col3 = st.columns(3)
        with col1:
            pregnancies = st.text_input('Number of Pregnancies')
            blood_pressure = st.text_input('Blood Pressure')
            bmi = st.text_input('BMI')

        with col2:
            glucose = st.text_input('Glucose Level')
            skin_thickness = st.text_input('Skin Thickness')
            diabetes_pedigree_function = st.text_input('Diabetes Pedigree Function')

        with col3:
            insulin = st.text_input('Insulin Level')
            age = st.text_input('Age')

        diabetes_diagnosis = ''
        if st.button('Diabetes Test Result'):
            user_input = [pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age]
            try:
                user_input = [float(x) for x in user_input]
                diabetes_prediction = diabetes_model.predict([user_input])
                if diabetes_prediction[0] == 1:
                    diabetes_diagnosis = 'This person is diabetic'
                else:
                    diabetes_diagnosis = 'This person is not diabetic'
            except ValueError:
                diabetes_diagnosis = 'Please enter valid numerical values.'

        st.success(diabetes_diagnosis)

    elif current_page == "Liver Disease Prediction":
        liver_disease_model_path = os.path.join(working_dir, '..', 'Models', 'liver_disease_model.sav')

        try:
            liver_disease_model = load_model(liver_disease_model_path)
        except Exception as e:
            st.error(f"Error loading Liver Disease model: {e}")
            st.stop()

        # Input fields for Liver Disease Prediction in columns
        col1, col2, col3 = st.columns(3)
        with col1:
            age = st.text_input('Age')
            bmi = st.text_input('BMI')
            physical_activity = st.text_input('Physical Activity (hours per week)')

        with col2:
            gender = st.text_input('Gender (1 = male; 0 = female)')
            alcohol_consumption = st.text_input('Alcohol Consumption (units per week)')
            diabetes = st.text_input('Diabetes (1 = yes; 0 = no)')

        with col3:
            smoking = st.text_input('Smoking (1 = yes; 0 = no)')
            genetic_risk = st.text_input('Genetic Risk (1 = yes; 0 = no)')
            liver_function_test = st.text_input('Liver Function Test (1 = abnormal; 0 = normal)')

        liver_diagnosis = ''
        if st.button('Liver Disease Test Result'):
            user_input = [age, gender, bmi, alcohol_consumption, smoking, genetic_risk, physical_activity, diabetes, liver_function_test]
            try:
                user_input = [float(x) for x in user_input]
                liver_prediction = liver_disease_model.predict([user_input])
                if liver_prediction[0] == 1:
                    liver_diagnosis = 'This person is at risk of liver disease'
                else:
                    liver_diagnosis = 'This person is not at risk of liver disease'
            except ValueError:
                liver_diagnosis = 'Please enter valid numerical values.'

        st.success(liver_diagnosis)

    elif current_page == "Hypothyroidism Prediction":
        hypothyroidism_model_path = os.path.join(working_dir, '..', 'Models', 'hypothyroidism_model.sav')

        try:
            hypothyroidism_model = load_model(hypothyroidism_model_path)
        except Exception as e:
            st.error(f"Error loading Hypothyroidism model: {e}")
            st.stop()

        # Input fields for Hypothyroidism Prediction in columns
        col1, col2, col3 = st.columns(3)
        with col1:
            age = st.text_input('Age')
            on_thyroxine = st.text_input('On Thyroxine (1 = yes; 0 = no)')
            sick = st.text_input('Sick (1 = yes; 0 = no)')

        with col2:
            sex = st.text_input('Sex (1 = male; 0 = female)')
            query_on_thyroxine = st.text_input('Query on Thyroxine (1 = yes; 0 = no)')
            pregnant = st.text_input('Pregnant (1 = yes; 0 = no)')

        with col3:
            on_antithyroid_medication = st.text_input('On Antithyroid Medication (1 = yes; 0 = no)')
            thyroid_surgery = st.text_input('Thyroid Surgery (1 = yes; 0 = no)')
            hypothyroid = st.text_input('Query Hypothyroid (1 = yes; 0 = no)')

        hypothyroidism_diagnosis = ''
        if st.button('Hypothyroidism Test Result'):
            user_input = [age, sex, on_thyroxine, query_on_thyroxine, on_antithyroid_medication, sick, pregnant, thyroid_surgery, hypothyroid]
            try:
                user_input = [float(x) if x not in ['yes', 'no'] else (1 if x == 'yes' else 0) for x in user_input]
                hypothyroidism_prediction = hypothyroidism_model.predict([user_input])
                if hypothyroidism_prediction[0] == 1:
                    hypothyroidism_diagnosis = 'This person is at risk of Hypothyroidism'
                else:
                    hypothyroidism_diagnosis = 'This person is not at risk of Hypothyroidism'
            except ValueError:
                hypothyroidism_diagnosis = 'Please enter valid numerical values.'

        st.success(hypothyroidism_diagnosis)

else:
    st.write("Please select a prediction model by clicking one of the buttons above.")
