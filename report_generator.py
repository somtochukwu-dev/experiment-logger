import pandas as pd

def generate_summary_report(df, output_path):
    # Create a copy to avoid modifying the original
    data = df.copy()

    # Sheet 1: Full Log (already cleaned/validated)
    full_log = data

    # Sheet 2: Summary by Technician
    tech_summary = data.groupby('technician').agg({
        'sample_id': 'nunique',
        'issue': lambda x: (x != 'OK').sum()
    }).rename(columns={
        'sample_id': 'Unique Samples Run',
        'issue': 'Issues Detected'
    }).reset_index()

    # Sheet 3: Step Frequency
    step_summary = data['step'].str.lower().value_counts().reset_index()
    step_summary.columns = ['Step', 'Occurrences']

    # Export to Excel with multiple sheets
    with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
        full_log.to_excel(writer, sheet_name='Experiment Log', index=False)
        tech_summary.to_excel(writer, sheet_name='Technician Summary', index=False)
        step_summary.to_excel(writer, sheet_name='Step Frequency', index=False)

    print("📊 Report written with: full log, technician summary, step frequency.")
