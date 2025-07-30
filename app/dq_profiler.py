import pandas as pd
from ydata_profiling import ProfileReport

def load_data(path):
    return pd.read_csv(path)

def profile_data(df, output_html="reports/profile.html"):
    profile = ProfileReport(df, title="Data Quality Profile", explorative=True)
    profile.to_file(output_file=output_html)
    return output_html
