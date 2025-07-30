from dq_profiler import load_data, profile_data, extract_summary_for_llm, append_ai_analysis_to_report
from ai_explainer import explain_data_quality_issues, suggest_data_fixes

df = load_data("data/telco.csv")
report_path = profile_data(df)

summary = extract_summary_for_llm(df)
explanation = explain_data_quality_issues(summary)
fix_suggestions = suggest_data_fixes(summary)

append_ai_analysis_to_report(report_path, explanation, fix_suggestions)

print("\n✅ Updated report with AI analysis:")
print(report_path)
