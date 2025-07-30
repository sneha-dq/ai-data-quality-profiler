import pandas as pd
from ydata_profiling import ProfileReport
from bs4 import BeautifulSoup

def load_data(path):
    return pd.read_csv(path)

def profile_data(df, output_html="reports/profile.html"):
    profile = ProfileReport(df, title="Data Quality Profile", explorative=True)
    profile.to_file(output_file=output_html)
    return output_html

def extract_summary_for_llm(df: pd.DataFrame) -> str:
    summary = []
    for col in df.columns:
        nulls = df[col].isnull().sum()
        dtype = df[col].dtype
        unique_vals = df[col].nunique()
        summary.append(f"Column: {col}, Type: {dtype}, Missing: {nulls}, Unique: {unique_vals}")
    return "\n".join(summary)

def append_ai_analysis_to_report(html_path, explanation, suggestions):
    with open(html_path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")

    # Create a new div for AI content
    ai_section = soup.new_tag("div")
    ai_section['style'] = "margin: 2em; padding: 1em; border: 2px solid #666; background: #f9f9f9;"
    
    explanation_html = f"<h2>🔍 AI-Generated Data Quality Analysis</h2><pre>{explanation}</pre>"
    suggestions_html = f"<h2>🛠️ AI-Suggested Fixes</h2><pre>{suggestions}</pre>"

    ai_section.append(BeautifulSoup(explanation_html + suggestions_html, "html.parser"))

    # Insert it before the footer or at the end of body
    if soup.body:
        soup.body.append(ai_section)

    with open(html_path, "w", encoding="utf-8") as f:
        f.write(str(soup))