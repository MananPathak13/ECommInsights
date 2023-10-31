import pandas as pd

def load_data(file_path):
    """Load raw data from a CSV file."""
    return pd.read_csv(file_path)

def clean_data(df):
    """Clean and preprocess the raw data."""
    # Example: Remove missing values
    df = df.dropna()
    # Add other data cleaning steps here
    return df

def save_processed_data(df, file_path):
    """Save the processed data to a CSV file."""
    df.to_csv(file_path, index=False)
