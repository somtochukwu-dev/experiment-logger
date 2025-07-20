import pandas as pd
from datetime import timedelta

# Define default step durations (in minutes)
STEP_DURATION_MAP = {
    'preparation': 60,
    'incubation': 90,
    'extraction': 45,
    'centrifuge': 30,
    'analysis': 60
}

def infer_missing_timestamps(df):
    df = df.copy()
    df['time'] = pd.to_datetime(df['time'], format='%H:%M', errors='coerce')

    # Go sample by sample
    for sample_id in df['sample_id'].unique():
        sample_df = df[df['sample_id'] == sample_id]

        for i in sample_df.index:
            if pd.isna(df.at[i, 'time']):
                prev_idx = i - 1
                # Look backwards for the last valid timestamp
                while prev_idx >= 0 and df.at[prev_idx, 'sample_id'] == sample_id:
                    prev_time = df.at[prev_idx, 'time']
                    prev_step = df.at[prev_idx, 'step'].strip().lower()

                    if pd.notna(prev_time) and prev_step in STEP_DURATION_MAP:
                        duration = STEP_DURATION_MAP.get(prev_step, 60)
                        df.at[i, 'time'] = prev_time + timedelta(minutes=duration)
                        break

    return df
