"""A transparent, no-API baseline: which known skills appear in the job but not the resume?

Matching is whole-word and case-insensitive, with a few aliases (e.g. 'sklearn' counts as
'scikit-learn'). It is deliberately simple - it can't judge depth of experience - so the LLM analysis
is the main read-out and this is the sanity check.
"""
import re

SKILLS = {
    "Python": [], "R": [], "SQL": [], "Excel": [], "Tableau": [], "Power BI": ["powerbi"],
    "pandas": [], "NumPy": [], "scikit-learn": ["sklearn"], "XGBoost": [], "PyTorch": [], "TensorFlow": [],
    "Spark": ["pyspark"], "Snowflake": [], "dbt": [], "Airflow": [], "AWS": [], "GCP": ["google cloud"],
    "Azure": [], "Git": ["github"], "Docker": [], "Streamlit": [],
    "A/B testing": ["ab testing", "a/b tests", "experimentation"], "forecasting": ["time series", "time-series"],
    "regression": [], "machine learning": ["ml"], "statistics": ["statistical"], "causal inference": [],
    "LLM": ["llms", "large language model", "large language models", "generative ai", "genai"],
    "prompt engineering": [], "data visualization": ["dashboards", "dashboard"], "ETL": ["data pipelines", "data pipeline"],
    "stakeholder management": ["stakeholders", "cross-functional"], "product analytics": [], "marketing analytics": [],
    "supply chain": ["inventory"], "financial modeling": ["financial models"],
}


def _pattern(term: str) -> re.Pattern:
    return re.compile(r"(?<![\w/+-])" + re.escape(term.lower()) + r"(?![\w/+-])")


def find_skills(text: str) -> set[str]:
    low = text.lower()
    return {skill for skill, aliases in SKILLS.items()
            if any(_pattern(t).search(low) for t in [skill, *aliases])}


def keyword_match(resume: str, job: str) -> dict:
    wanted, have = find_skills(job), find_skills(resume)
    matched, missing = sorted(wanted & have), sorted(wanted - have)
    return {"matched": matched, "missing": missing,
            "coverage": len(matched) / len(wanted) if wanted else None}
