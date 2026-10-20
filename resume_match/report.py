"""Render the analysis as a Markdown report."""


def render(analysis: dict | None, keywords: dict, resume_name: str, job_name: str) -> str:
    lines = [f"# Resume match: {resume_name} → {job_name}", ""]
    if analysis:
        lines += [f"**Fit score: {analysis['fit_score']}/100**", "", analysis["summary"], "", "## Strengths", ""]
        lines += [f"- **{s['requirement']}** — {s['evidence']}" for s in analysis["strengths"]]
        lines += ["", "## Gaps", ""]
        lines += [f"- **{g['requirement']}** ({g['severity']}) — {g['how_to_address']}" for g in analysis["gaps"]]
        lines += ["", "## Suggested bullet rewrites", ""]
        for b in analysis["bullet_rewrites"]:
            lines += [f"> **Before:** {b['original']}", ">", f"> **After:** {b['rewrite']}", "", f"_{b['why']}_", ""]
        lines += ["## Likely interview questions", ""]
        lines += [f"{i}. {q}" for i, q in enumerate(analysis["interview_questions"], 1)]
        lines += [""]
    cov = keywords["coverage"]
    lines += ["## Keyword check (no AI)", "",
              f"Skills named in the job that also appear in the resume: **{'n/a' if cov is None else f'{cov:.0%}'}**", "",
              f"- Matched: {', '.join(keywords['matched']) or '—'}",
              f"- Missing: {', '.join(keywords['missing']) or '—'}", ""]
    return "\n".join(lines)
