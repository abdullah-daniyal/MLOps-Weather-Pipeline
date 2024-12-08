import os
import pandas as pd
import pytest
from preprocess_data import preprocess

@pytest.fixture
def setup_test_data(tmp_path):
    # Create a temporary raw_data.csv for testing
    data = {
        "Temperature": [25.0, 30.0],
        "Humidity": [50.0, 60.0],
        "Wind Speed": [10.0, 12.0]
    }
    df = pd.DataFrame(data)
    raw_data_path = tmp_path / "raw_data.csv"
    df.to_csv(raw_data_path, index=False)
    # Change working directory to tmp_path for the duration of the test
    os.chdir(tmp_path)
    yield str(raw_data_path)
    # Cleanup handled by tmp_path

def test_preprocess(setup_test_data):
    # Run preprocess
    preprocess()

    assert os.path.exists("data/processed_data.csv"), "Processed data file not created"

    processed_df = pd.read_csv("data/processed_data.csv")
    # Check shape and if columns exist
    assert processed_df.shape == (2, 3), "Processed data shape mismatch"
    assert all(col in processed_df.columns for col in ["Temperature", "Humidity", "Wind Speed"])

    # Check normalization (mean approx 0)
    assert abs(processed_df["Temperature"].mean()) < 1e-6, "Temperature not normalized properly"
    assert abs(processed_df["Humidity"].mean()) < 1e-6, "Humidity not normalized properly"
    assert abs(processed_df["Wind Speed"].mean()) < 1e-6, "Wind Speed not normalized properly"