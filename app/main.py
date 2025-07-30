# app/main.py

from dq_profiler import load_data, profile_data

df = load_data("data/telco.csv")
report_path = profile_data(df)
print(f"Data quality report generated: {report_path}")
