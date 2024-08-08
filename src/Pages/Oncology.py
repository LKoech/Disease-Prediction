import os
import pickle
import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Oncology Disease Detection",
    page_icon="🩺"
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

# Display function for Oncology section
def display():
    st.title("Oncology")
    st.write("This section covers various aspects of oncology diseases and their detection.")

# Run the display function for Oncology
display()

# Create three columns for the prediction models at the top
col1, col2 = st.columns(2)

with col1:
    if st.button("Lung Cancer Prediction"):
        st.session_state.current_page = "Lung Cancer Prediction"

with col2:
    if st.button("Prostate Cancer Prediction"):
        st.session_state.current_page = "Prostate Cancer Prediction"

# Display the selected page's content below
current_page = st.session_state.current_page
if current_page:
    st.write(f"**{current_page}**")

    if current_page == "Lung Cancer Prediction":
        lung_cancer_model_path = os.path.join(working_dir, '..', 'Models', 'lung_cancer_model.sav')

        try:
            lung_cancer_model = load_model(lung_cancer_model_path)
        except Exception as e:
            st.error(f"Error loading Lung Cancer model: {e}")
            st.stop()

        # Input fields for Lung Cancer Prediction in columns
        col1, col2, col3 = st.columns(3)
        with col1:
            index = st.text_input('Index')
            gender = st.text_input('Gender (M/F)')
            dust_allergy = st.text_input('Dust Allergy')
            chronic_lung_disease = st.text_input('Chronic Lung Disease')
            obesity = st.text_input('Obesity')
            chest_pain = st.text_input('Chest Pain')
            fatigue = st.text_input('Fatigue')
            wheezing = st.text_input('Wheezing')
            snoring = st.text_input('Snoring')

        with col2:
            patient_id = st.text_input('Patient ID')
            air_pollution = st.text_input('Air Pollution')
            occupational_hazards = st.text_input('Occupational Hazards')
            genetic_risk = st.text_input('Genetic Risk')
            smoking = st.text_input('Smoking')
            coughing_of_blood = st.text_input('Coughing of Blood')
            weight_loss = st.text_input('Weight Loss')
            swallowing_difficulty = st.text_input('Swallowing Difficulty')

        with col3:
            age = st.text_input('Age')
            alcohol_use = st.text_input('Alcohol Use')
            balanced_diet = st.text_input('Balanced Diet')
            passive_smoker = st.text_input('Passive Smoker')
            shortness_of_breath = st.text_input('Shortness of Breath')
            frequent_cold = st.text_input('Frequent Cold')
            dry_cough = st.text_input('Dry Cough')
            level = st.text_input('Level')

        lung_cancer_diagnosis = ''
        if st.button('Lung Cancer Test Result'):
            user_input = [
                index, patient_id, age, gender, air_pollution, alcohol_use, dust_allergy,
                occupational_hazards, genetic_risk, chronic_lung_disease, balanced_diet,
                obesity, smoking, passive_smoker, chest_pain, coughing_of_blood, fatigue,
                weight_loss, shortness_of_breath, wheezing, swallowing_difficulty,
                frequent_cold, dry_cough, snoring, level
            ]
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

    elif current_page == "Prostate Cancer Prediction":
        prostate_cancer_model_path = os.path.join(working_dir, '..', 'Models', 'prostate_cancer_model.sav')

        try:
            prostate_cancer_model = load_model(prostate_cancer_model_path)
        except Exception as e:
            st.error(f"Error loading Prostate Cancer model: {e}")
            st.stop()

        # Input fields for Prostate Cancer Prediction in columns
        col1, col2, col3 = st.columns(3)
        with col1:
            radius = st.text_input('Radius')
            smoothness = st.text_input('Smoothness')

        with col2:
            texture = st.text_input('Texture')
            compactness = st.text_input('Compactness')

        with col3:
            perimeter = st.text_input('Perimeter')
            symmetry = st.text_input('Symmetry')

        area = st.text_input('Area')
        fractal_dimension = st.text_input('Fractal Dimension')

        prostate_cancer_diagnosis = ''
        if st.button('Prostate Cancer Test Result'):
            user_input = [
                radius, texture, perimeter, area,
                smoothness, compactness, symmetry, fractal_dimension
            ]
            try:
                user_input = [float(x) for x in user_input]
                prostate_cancer_prediction = prostate_cancer_model.predict([user_input])

                if prostate_cancer_prediction[0] == 1:
                    prostate_cancer_diagnosis = 'The patient is likely to have Prostate Cancer'
                else:
                    prostate_cancer_diagnosis = 'The patient is not likely to have Prostate Cancer'
            except ValueError:
                prostate_cancer_diagnosis = 'Please enter valid numerical values.'

        st.success(prostate_cancer_diagnosis)
else:
    st.write("Please select a prediction model by clicking one of the buttons above.")


