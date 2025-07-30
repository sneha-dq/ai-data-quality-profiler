# app/ai_explainer.py

import ollama

def explain_data_quality_issues(summary_text: str) -> str:
    prompt = f"""You are a data quality expert. Given the following summary of a dataset, explain possible data quality issues you detect. Be specific and concise.

Summary:
{summary_text}

Answer:"""

    response = ollama.chat(
        model='tinyllama',
        messages=[{"role": "user", "content": prompt}]
    )

    return response['message']['content']

def suggest_data_fixes(summary_text: str) -> str:
    prompt = f"""You are a data cleaning assistant. Based on the following data summary, suggest concrete ways to fix data quality issues. Mention which columns need fixing and how (e.g., fill missing with median, drop rows, convert types, etc).

Summary:
{summary_text}

Fix Suggestions:"""
    response = ollama.chat(
        model='tinyllama',
        messages=[{"role": "user", "content": prompt}]
    )
    return response['message']['content']