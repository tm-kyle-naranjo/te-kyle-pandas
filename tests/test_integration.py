import os
import pytest
import pandas as pd
from src.validations import run_all_validations
from src.tasks import clean_data

current_dir = os.path.dirname(os.path.abspath(__file__))

@pytest.fixture
def test_data():
    """
    Fixture to load test data from CSV file.
    """
    file_path = os.path.join(current_dir, '..', 'data', 'test', 'test_clean_data.csv')
    return pd.read_csv(file_path)

@pytest.fixture
def expected_validation_output():
    """
    Fixture to load expected validation output from CSV file.
    """
    file_path = os.path.join(current_dir, '..', 'data', 'reports', 'output_validation_cleaned.csv')
    return pd.read_csv(file_path)

@pytest.fixture
def expected_cleaning_output():
    """
    Fixture to load expected cleaning output from CSV file.
    """
    file_path = os.path.join(current_dir, '..', 'data', 'cleaned', 'output_cleaning.csv')
    return pd.read_csv(file_path)

def test_end_to_end_integration(test_data, expected_validation_output, expected_cleaning_output):
    """
    End-to-end integration test for data validation and cleaning process.
    """
    validation_results = run_all_validations(test_data)
    
    assert len(validation_results) == len(expected_validation_output)
    for (_, result), (_, expected) in zip(validation_results.iterrows(), expected_validation_output.iterrows()):
        assert result['validation_type'] == expected['validation_type']
        assert result['validation_remarks'].startswith(expected['validation_remarks'][:50])

    cleaned_data = clean_data(test_data)
    cleaned_data = cleaned_data.reset_index(drop=True)
    pd.testing.assert_frame_equal(cleaned_data, expected_cleaning_output, check_dtype=False)