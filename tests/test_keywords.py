from resume_match.keywords import find_skills, keyword_match


def test_aliases_and_whole_words():
    assert find_skills("Built models in sklearn and PySpark") == {"scikit-learn", "Spark"}
    assert "R" not in find_skills("Partnered with marketing")          # 'r' inside words doesn't count
    assert "R" in find_skills("Languages: Python, R, SQL")


def test_coverage():
    m = keyword_match("Python and SQL", "Need Python, SQL and Tableau")
    assert m["matched"] == ["Python", "SQL"] and m["missing"] == ["Tableau"]
    assert m["coverage"] == 2 / 3


def test_no_skills_in_job():
    assert keyword_match("Python", "Friendly team!")["coverage"] is None
