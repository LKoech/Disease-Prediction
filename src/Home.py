import streamlit as st
import importlib

# Set page configuration
st.set_page_config(
    page_title="Disease Detection",
    page_icon="⚕️"
)

st.title("⚕️ Disease Detection")
st.write("Welcome to the Disease Detection App! Here we use our Machine Learning models to assist in identifying the presence of various diseases.")

# Define the data
data = [
    {"header": "Cardiology", "module": "Pages.Cardiology"},
    {"header": "Endocrinology", "module": "Pages.Endocrinology"},
    {"header": "Gastroenterology", "module": "Pages.Gastroenterology"},
    {"header": "Oncology", "module": "Pages.Oncology"},
    {"header": "Infectious Diseases", "module": "Pages.InfectiousDiseases"}
]

# CSS for styling the cards
st.markdown("""
    <style>
    .card {
        width: 100%;
        padding-bottom: 100%;
        margin: 1.5%;
        background-color: lightblue;
        border-radius: 8px;
        position: relative;
        text-align: center;
        cursor: pointer;
        overflow: hidden;
        transition: transform 0.2s;
    }
    .card:hover {
        transform: scale(1.05);
    }
    .card-text {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
        width: 90%;
        padding: 0 5px;
        color: black;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state if not already set
if 'current_page' not in st.session_state:
    st.session_state.current_page = ""

# Create the layout with cards
for i in range(0, len(data), 3):
    cols = st.columns(3)
    for col, item in zip(cols, data[i:i+3]):
        with col:
            if st.button(item['header']):
                st.session_state.current_page = item['module']

# Display the current page content
current_page = st.session_state.current_page
if current_page:
    st.write(f"Loading page: {current_page.split('.')[-1]}")
    try:
        module = importlib.import_module(current_page)
        module.display()
    except ModuleNotFoundError:
        st.error(f"Module for {current_page.split('.')[-1]} not found.")
else:
    st.write("Select a page from the cards above.")
