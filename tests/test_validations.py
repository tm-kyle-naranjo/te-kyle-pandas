import os
import pytest
from src.validations import run_all_validations
from src.tasks import clean_data as clean_data_function
import pandas as pd

current_dir = os.path.dirname(os.path.abspath(__file__))

@pytest.fixture
def clean_data():
    """Fixture for clean input data."""
    file_path = os.path.join(current_dir, '..', 'data', 'test', 'test_clean_data.csv')
    return pd.read_csv(file_path)

@pytest.fixture
def dirty_data():
    """Fixture for dirty input data."""
    file_path = os.path.join(current_dir, '..', 'data', 'test', 'test_dirty_data.csv')
    return pd.read_csv(file_path)

@pytest.fixture
def clean_output():
    """Fixture for expected clean validation output."""
    file_path = os.path.join(current_dir, '..', 'data', 'reports', 'output_validation_cleaned.csv')
    return pd.read_csv(file_path)

@pytest.fixture
def dirty_output():
    """Fixture for expected dirty validation output."""
    file_path = os.path.join(current_dir, '..', 'data', 'reports', 'output_validation_dirty.csv')
    return pd.read_csv(file_path)

@pytest.fixture
def clean_data_expected_output():
    """Fixture for expected output after cleaning clean data."""
    file_path = os.path.join(current_dir, '..', 'data', 'cleaned', 'output_cleaning.csv')
    return pd.read_csv(file_path)

def test_run_all_validations_clean(clean_data, clean_output):
    """Test validation results for clean data."""
    validation_results = run_all_validations(clean_data)
    
    assert len(validation_results) == len(clean_output)
    
    for (_, result), (_, expected) in zip(validation_results.iterrows(), clean_output.iterrows()):
        assert result['validation_type'] == expected['validation_type']
        assert result['validation_remarks'].startswith(expected['validation_remarks'][:50])

def test_run_all_validations_dirty(dirty_data, dirty_output):
    """Test validation results for dirty data."""
    validation_results = run_all_validations(dirty_data)
    
    assert len(validation_results) == len(dirty_output)
    
    for (_, result), (_, expected) in zip(validation_results.iterrows(), dirty_output.iterrows()):
        assert result['validation_type'] == expected['validation_type']
        assert result['validation_remarks'].startswith(expected['validation_remarks'][:50])

def test_clean_data_with_clean_input(clean_data, clean_data_expected_output):
    """Test cleaning function with already clean data."""
    
    cleaned_data = clean_data_function(clean_data)
    cleaned_data = cleaned_data.reset_index(drop=True)
    pd.testing.assert_frame_equal(cleaned_data, clean_data_expected_output, check_dtype=False)