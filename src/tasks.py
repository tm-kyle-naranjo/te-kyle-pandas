import pandas as pd
import numpy as np
from datetime import datetime
import pytz

def remove_null_values(df):
    """Remove rows with null values from the dataset."""
    return df.dropna()

def transform_dates(df):
    """Transform convertible dates into standard datetime format in English."""
    def convert_date(date_str):
        russian_months = {
            'января': 'January', 'февраля': 'February', 'марта': 'March',
            'апреля': 'April', 'мая': 'May', 'июня': 'June',
            'июля': 'July', 'августа': 'August', 'сентября': 'September',
            'октября': 'October', 'ноября': 'November', 'декабря': 'December'
        }
        for rus, eng in russian_months.items():
            if rus in date_str:
                return date_str.replace(rus, eng)
        return date_str

    # Create a copy of the DataFrame
    df_copy = df.copy()
    df_copy['timestamp'] = df_copy['timestamp'].apply(convert_date)
    return df_copy

def remove_duplicates(df):
    """Remove duplicate rows from the dataset."""
    return df.drop_duplicates()

def strip_whitespace(df):
    """Strip whitespace from string fields."""
    for col in df.select_dtypes(include=['object']):
        df[col] = df[col].str.strip()
    return df

def convert_timestamps(df):
    """Convert timestamps to a standard format and ensure they are in UTC."""
    def to_utc(ts):
        try:
            dt = pd.to_datetime(ts, utc=True)
            return dt.strftime('%Y-%m-%d %H:%M:%S UTC')
        except:
            return ts  # Return original if conversion fails

    df['timestamp'] = df['timestamp'].apply(to_utc)
    return df

def ensure_data_types(df):
    """Ensure fields adhere to the expected data types."""
    df['user'] = df['user'].astype('str')
    df['hours'] = df['hours'].astype('float32')
    df['project'] = df['project'].astype('str')
    return df

def clean_data(df):
    """Apply all cleaning steps to the dataset."""
    df_cleaned = df.copy()
    df_cleaned = remove_null_values(df_cleaned)
    df_cleaned = transform_dates(df_cleaned)
    df_cleaned = remove_duplicates(df_cleaned)
    df_cleaned = strip_whitespace(df_cleaned)
    df_cleaned = convert_timestamps(df_cleaned)
    df_cleaned = ensure_data_types(df_cleaned)
    return df_cleaned

if __name__ == "__main__":
    raw_data = pd.read_csv('raw_data.csv')
    
    cleaned_data = clean_data(raw_data)
