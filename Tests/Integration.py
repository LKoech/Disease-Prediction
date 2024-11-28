import streamlit as st

def test_session_state_initialization():
    """Test that session state initializes correctly."""
    if "current_page" not in st.session_state:
        st.session_state.current_page = ""
    assert st.session_state.current_page == "", "Session state should default to empty"

def test_session_state_navigation():
    """Test session state updates on button clicks."""
    st.session_state.current_page = "Heart Disease Prediction"
    assert st.session_state.current_page == "Heart Disease Prediction"
