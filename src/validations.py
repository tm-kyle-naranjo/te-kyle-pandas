import pandas as pd
from datetime import datetime

def validate_columns(df):
    """
    Validate the presence and correctness of columns in the DataFrame.
    """
    required_columns = ['user', 'hours', 'project', 'timestamp']
    if set(required_columns).issubset(df.columns):
        return True, "All required columns are present and properly named"
    else:
        missing_columns = set(required_columns) - set(df.columns)
        return False, f"Missing columns: {', '.join(missing_columns)}"

def validate_hours(df):
    """
    Validate the 'hours' column to ensure it contains valid hour values.
    """
    def is_valid_hour(value):
        if pd.isna(value):
            return False
        try:
            float_value = float(value)
            return 0 < float_value <= 24  # Adjust range as needed
        except ValueError:
            return False

    valid_hours = df['hours'].apply(is_valid_hour)
    invalid_rows = df[~valid_hours].index.tolist()

    if not invalid_rows:
        return True, "All 'hours' values are valid"
    else:
        return False, f"Invalid 'hours' values in rows: {invalid_rows}"

def validate_timestamp(df):
    """
    Validate the 'timestamp' column to ensure it contains valid date-time values.
    """
    def check_timestamp(ts):
        if not isinstance(ts, str):
            return False, f"Invalid type: {type(ts).__name__}"
        
        formats = [
            '%Y-%m-%d %H:%M:%S UTC',
            '%m/%d/%Y %I:%M %p',
            '%d %B %Y %H:%M',
            '%Y-%m-%d %H:%M:%S.%f UTC'
        ]
        
        for fmt in formats:
            try:
                datetime.strptime(ts, fmt)
                return True, "Valid"
            except ValueError:
                continue
        
        russian_months = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 
                          'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
        
        if any(month in ts for month in russian_months):
            return False, "Convertible if changed to English"
        
        return False, "Not convertible"

    results = df['timestamp'].apply(check_timestamp)
    invalid_timestamps = df[~results.apply(lambda x: x[0])]
    
    if invalid_timestamps.empty:
        return True, "All timestamps are in a standard date time format or convertible"
    else:
        invalid_rows = invalid_timestamps.index.tolist()
        conversion_status = [f"Row {idx}: {status[1]}" for idx, status in zip(invalid_rows, results[invalid_timestamps.index])]
        return False, f"Invalid timestamps: {conversion_status}"

def check_null_values(df):
    """
    Validate the presence of null values in the DataFrame.
    """
    null_rows = df[df.isnull().any(axis=1)]
    if null_rows.empty:
        return True, "No missing or null values found"
    else:
        invalid_rows = null_rows.index.tolist()
        return False, f"Missing or null values found in rows: {invalid_rows}"

def run_all_validations(df):
    """
    Run all validation checks on the DataFrame.
    """
    validation_results = []

    column_check = validate_columns(df)
    validation_results.append({"validation_type": "Column Presence", "validation_remarks": column_check[1]})

    hours_check = validate_hours(df)
    validation_results.append({"validation_type": "Hours Validation", "validation_remarks": hours_check[1]})

    timestamp_check = validate_timestamp(df)
    validation_results.append({"validation_type": "Timestamp Format", "validation_remarks": timestamp_check[1]})

    null_check = check_null_values(df)
    validation_results.append({"validation_type": "Null Values Check", "validation_remarks": null_check[1]})

    return pd.DataFrame(validation_results)
