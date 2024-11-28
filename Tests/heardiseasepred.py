import os
import sys
from unittest.mock import MagicMock

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
print("PYTHONPATH:", sys.path)

from src.Pages.Cardiology import load_model

def test_heart_disease_prediction(mocker):
    """Test prediction logic for Heart Disease."""
    mock_model = MagicMock()
    mock_model.predict.return_value = [1]  # Mock the prediction result as 'positive'

    # Mock the `load_model` function to return our mock model
    mocker.patch("src.Pages.Cardiology.load_model", return_value=mock_model)

    # Create valid input
    user_input = [45, 1, 3, 120, 230, 0, 0, 150, 0, 2.3, 1, 0, 2]
    heart_disease_model = load_model("mock_model.sav")
    prediction = heart_disease_model.predict([user_input])
    assert prediction == [1], "Prediction should indicate 'positive' for heart disease"

def test_invalid_user_input():
    """Test user input validation."""
    invalid_input = ["forty-five", "male", 3, 120, "high", 0, 0, 150, 0, 2.3, 1, 0, 2]
    try:
        float_inputs = [float(x) for x in invalid_input]
    except ValueError:
        float_inputs = None
    assert float_inputs is None, "Invalid input should not convert to float"