import pandas as pd

def clean_experiment_data(df):
    # Standardize column names
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

    # Convert timestamps
    df['time'] = pd.to_datetime(df['time'], format='%H:%M', errors='coerce').dt.time

    
    # Drop rows with completely missing timestamp or sample ID
    df = df.dropna(subset=['time', 'sample_id'])

    # Forward fill missing technician or step name
    df['technician'] = df['technician'].fillna(method='ffill')
    df['step'] = df['step'].fillna(method='ffill')

    # Normalize text fields (e.g., case & spacing)
    df['technician'] = df['technician'].str.strip().str.title()
    df['step'] = df['step'].str.strip().str.lower()

    # Sort data for easier tracking
    df = df.sort_values(by=['sample_id', 'time']).reset_index(drop=True)

    return df
