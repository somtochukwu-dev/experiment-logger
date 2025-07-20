🧪 Sci-Cle Lab Experiment Logger
A Python automation tool for tracking, cleaning, validating, and reporting biological lab experiments. It processes raw experiment logs, fills in missing timestamps, checks step sequences, and generates multi-sheet Excel reports for daily summaries and full experiment logs.

🚀 Features
✅ Clean raw experiment logs
✅ Infer missing timestamps based on prior steps
✅ Validate step sequences (detect missing or out-of-order steps)
✅ Generate multi-sheet Excel reports:

Full cleaned log

Technician performance summary

Step frequency breakdown

✅ Save cleaned logs and reports in multiple folders (outputs/ and logs/)

🗂 Project Structure
 
experiment-logger/
├── data/
│   └── raw_experiment_log.csv          # Raw experiment data
├── outputs/
│   ├── cleaned_experiment_log.xlsx     # Cleaned, validated log
│   └── experiment_summary_report.xlsx  # Multi-sheet summary report
├── logs/
│   ├── cleaned_log.csv
│   └── daily_summary.xlsx
├── cleaner.py                          # Data cleaning functions
├── logger.py                           # Timestamp inference logic
├── validator.py                        # Step sequence validation
├── report_generator.py                  # Excel report creation
├── main.py                             # Orchestrates the automation workflow
├── requirements.txt                    # Python dependencies
└── README.md                           # Project documentation
⚙️ Installation
1️⃣ Clone this repository

git clone https://github.com/yourusername/experiment-logger.git
cd experiment-logger
2️⃣ Install dependencies

pip install -r requirements.txt
3️⃣ Prepare your raw data

Place your experiment log as data/raw_experiment_log.csv.

🧑‍🔬 Usage
Run the main automation pipeline:

python main.py
✅ Cleaned logs and reports will be saved in both outputs/ and logs/.

📊 Example Outputs
Cleaned Log: outputs/cleaned_experiment_log.xlsx

Technician Summary: Technician-level breakdown of samples processed and issues flagged.

Step Frequency: Counts how often each step occurs across all experiments.

📦 Dependencies
pandas

openpyxl

pyyaml

Install all with:

pip install -r requirements.txt

👨‍💻 Author
Somtochukwu O

License
This project is licensed for educational and portfolio purposes. Contact for commercial use.
