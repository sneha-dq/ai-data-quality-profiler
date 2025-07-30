# 🧠 AI-Powered Data Quality Profiler and Fixer

A lightweight, local-first tool for **profiling**, **explaining**, and **suggesting fixes for data quality issues** using machine learning and large language models (LLMs).

Built with:

* 📊 `pandas` and `ydata-profiling` for deep data inspection
* 🤖 LLMs (via [Ollama](https://ollama.com)) for local, AI-generated insights
* ⚡ Designed to run fully offline using small models like `tinyllama`

---

## ✅ Features Implemented So Far

* 📅 Upload and profile any CSV file
* 📈 Generate a rich interactive HTML report
* 🧠 Use local LLM to:

  * Explain data quality issues (missing values, type mismatches, outliers, etc.)
  * Suggest intelligent data cleaning steps
* ✍️ Automatically embed AI-generated analysis into the profiling report

---

## 📂 Project Structure

```
ai-data-quality-profiler/
├── app/
│   ├── main.py                  # Driver script
│   ├── dq_profiler.py           # Profiling & reporting logic
│   └── ai_explainer.py          # LLM-based insights (via Ollama)
├── data/                        # Sample datasets (e.g., telco.csv)
├── reports/                     # HTML reports with embedded AI analysis
├── notebooks/                   # EDA or experiments (optional)
├── tests/                       # Future unit tests
├── requirements.txt
└── README.md
```

---

## 🚀 How to Run Locally

### 1. Set up the project

```bash
git clone https://github.com/your-username/ai-data-quality-profiler.git
cd ai-data-quality-profiler
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Install and start Ollama

```bash
curl -fsSL https://ollama.com/install.sh | sh
ollama run tinyllama
```

> ❗ You need \~4GB RAM. If `mistral` doesn’t fit, use `tinyllama`.

### 3. Run the profiler

```bash
python app/main.py
```

Then open the report:

```bash
xdg-open reports/profile.html
```

---

## 📊 Dataset Used

**Telco Customer Churn**
A public dataset with a mix of numerical, categorical, and messy values — ideal for data quality profiling.

Source: [Kaggle Dataset](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)

---

## 📌 What's Next

* [ ] Apply selected fix suggestions automatically
* [ ] Generate cleaned dataset with comparison
* [ ] Add Streamlit UI for upload → profile → fix workflow
* [ ] Enable custom rule-based validations (Great Expectations or similar)
* [ ] Add test coverage and CI

---

## �� License

MIT License © 2025 Sneha Shrivastav

---

## 💖 Acknowledgments

* [YData Profiling](https://github.com/ydataai/ydata-profiling)
* [Ollama](https://ollama.com/) for local LLMs
* [TinyLlama](https://huggingface.co/TinyLlama) — small but mighty!

