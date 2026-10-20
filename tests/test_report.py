from resume_match.report import render

FAKE = {"fit_score": 72, "summary": "Good fit.", "strengths": [{"requirement": "SQL", "evidence": "3 years"}],
        "gaps": [{"requirement": "dbt", "severity": "nice-to-have", "how_to_address": "Build a small dbt project."}],
        "bullet_rewrites": [{"original": "Made reports", "rewrite": "Built weekly SQL reports", "why": "Names the tool."}],
        "interview_questions": ["How do you validate a forecast?"]}


def test_report_contains_every_section():
    md = render(FAKE, {"matched": ["SQL"], "missing": ["dbt"], "coverage": 0.5}, "resume", "job")
    for text in ["Fit score: 72/100", "## Strengths", "## Gaps", "**Before:** Made reports", "1. How do you validate", "50%"]:
        assert text in md


def test_keyword_only_report():
    md = render(None, {"matched": [], "missing": ["SQL"], "coverage": 0.0}, "r", "j")
    assert "Fit score" not in md and "Missing: SQL" in md
