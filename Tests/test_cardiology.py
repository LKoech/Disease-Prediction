import os
import pytest
from src.Pages.Cardiology import load_model

# Mock path to a model file
mock_model_path = "tests/mock_model.sav"

# Create a mock model file before running tests
@pytest.fixture(scope="module", autouse=True)
def create_mock_model_file():
    with open(mock_model_path, "wb") as f:
        import pickle
        pickle.dump({"model": "test_model"}, f)  # Create a mock model
    yield
    # Remove the file after testing
    os.remove(mock_model_path)

def test_load_model_success():
    """Test successful model loading."""
    model = load_model(mock_model_path)
    assert "model" in model
    assert model["model"] == "test_model"

def test_load_model_file_not_found():
    """Test loading a model from a non-existent path."""
    with pytest.raises(FileNotFoundError):
        load_model("non_existent_path.sav")

def test_load_model_corrupted_file():
    """Test loading a corrupted model file."""
    corrupted_path = "tests/corrupted_model.sav"
    with open(corrupted_path, "wb") as f:
        f.write(b"Not a valid pickle file")
    with pytest.raises(RuntimeError):
        load_model(corrupted_path)
    os.remove(corrupted_path)
