import pandas as pd
from cleaner import clean_experiment_data
from logger import infer_missing_timestamps
from validator import check_step_sequence
from report_generator import generate_summary_report
import os

def main():
    print("🧪 Sci-Cle Lab Experiment Tracker Initialising...")

    # File paths
    raw_data_path = 'data/raw_experiment_log.csv'
    cleaned_xlsx_path = 'outputs/cleaned_experiment_log.xlsx'
    report_xlsx_path = 'outputs/experiment_summary_report.xlsx'
    cleaned_log_csv = 'logs/cleaned_log.csv'
    summary_log_xlsx = 'logs/daily_summary.xlsx'

    # Ensure output folders exist
    os.makedirs('outputs', exist_ok=True)
    os.makedirs('logs', exist_ok=True)

    # Load raw data
    print("📥 Loading raw experiment log...")
    df = pd.read_csv(raw_data_path)
    print(f"✅ Loaded {len(df)} rows.")

    # Clean data
    print("🧹 Cleaning data...")
    df_cleaned = clean_experiment_data(df)
    print("✅ Cleaning complete.")

    # Fill missing timestamps
    print("⏱️ Inferring missing timestamps...")
    df_logged = infer_missing_timestamps(df_cleaned)
    print("✅ Timestamps updated.")

    # Validate step sequence
    print("🔎 Checking step sequences...")
    df_validated = check_step_sequence(df_logged)
    print("✅ Validation complete.")

    # Save cleaned log to both outputs/ and logs/
    print("💾 Saving cleaned logs...")
    df_validated.to_excel(cleaned_xlsx_path, index=False)
    df_validated.to_csv(cleaned_log_csv, index=False)
    print(f"✅ Cleaned log saved to:\n - {cleaned_xlsx_path}\n - {cleaned_log_csv}")

    # Generate summary report to both outputs/ and logs/
    print("📊 Generating reports...")
    generate_summary_report(df_validated, report_xlsx_path)
    generate_summary_report(df_validated, summary_log_xlsx)
    print(f"✅ Summary reports saved to:\n - {report_xlsx_path}\n - {summary_log_xlsx}")

    print("🎉 Lab tracking automation complete.")

if __name__ == "__main__":
    main()

