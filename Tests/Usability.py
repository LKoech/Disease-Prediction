import streamlit as st

def test_mock_ui_inputs(mocker):
    """Test prediction based on mocked UI inputs."""
    # Mock Streamlit input functions
    mocker.patch("streamlit.text_input", side_effect=["45", "1", "2", "120", "220"])
    mocker.patch("streamlit.button", return_value=True)

    # Collect user inputs
    age = st.text_input("Age")
    sex = st.text_input("Sex")
    cp = st.text_input("Chest Pain types")
    trestbps = st.text_input("Resting Blood Pressure")
    chol = st.text_input("Serum Cholesterol in mg/dl")

    # Verify that inputs are captured correctly
    assert age == "45"
    assert sex == "1"
    assert cp == "2"
    assert trestbps == "120"
    assert chol == "220"
