# 🤖 Resume–Job Matcher

![tests](https://github.com/RachelLiu13/resume-job-matcher/actions/workflows/tests.yml/badge.svg)

Compare a resume with a job post and get an honest, specific read-out: a fit score, where the resume already
meets each requirement, the real gaps and how to close them, rewritten bullets in the job's vocabulary,
and the interview questions the gaps will invite.

**One firm rule: no invented experience.** The model may only rephrase or re-emphasize what is already in
the resume. When a requirement isn't there, it is reported as a gap — not written into a bullet.

## Example

Input: a [fictional resume](examples/sample_resume.md) and a [fictional Growth Data Analyst job post](examples/sample_job.md).
Output: [**sample_report.md**](examples/sample_report.md). Excerpt:

> **Fit score: 72/100** — a solid match on the core analyst profile … the main gaps are churn/lifetime-value
> modeling and production data work with dbt, and the experimentation experience is described too vaguely to show depth.
>
> **Before:** Helped the team test two versions of the checkout page.
> **After:** Supported an A/B test of two checkout page variants, [specify your part: e.g., defining the conversion
> metric, pulling results in SQL, testing statistical significance].
> *Fill in the bracket only with what you really did.*

## How it works

| Step | What happens |
|---|---|
| Read | `.txt`, `.md` or `.pdf` for both documents |
| Analyze | Claude (Anthropic API) with **structured outputs**: the reply must match a JSON schema, so the report never parses free text |
| Check | A transparent keyword baseline (no AI) lists skills named in the job and whether the resume mentions them — a sanity check on the model, and a fallback without an API key |
| Report | Markdown with strengths, gaps (must-have / nice-to-have), bullet rewrites and likely interview questions |

The keyword check also shows why a language model helps: it marks *A/B testing* as missing because the
resume says "test two versions of the checkout page" — the model recognizes that as A/B testing experience.

## Run it

```bash
pip install -r requirements.txt
cp .env.example .env          # add your ANTHROPIC_API_KEY
python -m resume_match my_resume.pdf job_post.txt --out report.md

python -m resume_match my_resume.pdf job_post.txt --no-llm   # keyword check only, no key needed
pytest -q
```

## Layout

```
resume_match/documents.py   read .txt / .md / .pdf
resume_match/keywords.py    no-AI skill matching with aliases
resume_match/analyze.py     Claude call, JSON schema, no-invention instructions
resume_match/report.py      Markdown report
resume_match/__main__.py    command line
examples/                   fictional resume, job post and the generated report
```

Privacy: your documents are sent to the Anthropic API only when you run the AI analysis; nothing is stored by
this tool. Keep `.env` out of version control (it is in `.gitignore`).
