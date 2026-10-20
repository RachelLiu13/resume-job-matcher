"""Ask Claude to compare a resume with a job post and suggest honest, tailored edits.

The model returns JSON that matches SCHEMA (structured outputs), so the report never has to parse
free text. The instructions forbid inventing experience: every suggested bullet must be a rewrite of
something already in the resume.
"""
import json

import anthropic

MODEL = "claude-opus-5-5"

SYSTEM = """You are an experienced recruiter and career coach for analytics and data roles.
Compare the candidate's resume with the job description and help the candidate tailor the resume.

Rules:
- Base every statement on the resume text. Never invent employers, projects, tools, numbers or results.
- Suggested bullets must rewrite or re-emphasize experience that is already in the resume, using the
  job's vocabulary where it is accurate. If a requirement is simply missing, list it as a gap instead.
- Be specific and concise. Score fit honestly; most real matches are between 50 and 85."""

SCHEMA = {
    "type": "object",
    "properties": {
        "fit_score": {"type": "integer", "description": "0-100 overall fit"},
        "summary": {"type": "string", "description": "2-3 sentences: overall fit and the main gap"},
        "strengths": {"type": "array", "items": {"type": "object", "properties": {
            "requirement": {"type": "string"}, "evidence": {"type": "string", "description": "where the resume shows it"}},
            "required": ["requirement", "evidence"], "additionalProperties": False}},
        "gaps": {"type": "array", "items": {"type": "object", "properties": {
            "requirement": {"type": "string"},
            "severity": {"type": "string", "enum": ["must-have", "nice-to-have"]},
            "how_to_address": {"type": "string", "description": "honest advice: a project to build, a course, or how to frame adjacent experience"}},
            "required": ["requirement", "severity", "how_to_address"], "additionalProperties": False}},
        "bullet_rewrites": {"type": "array", "items": {"type": "object", "properties": {
            "original": {"type": "string", "description": "the resume bullet, quoted"},
            "rewrite": {"type": "string"}, "why": {"type": "string"}},
            "required": ["original", "rewrite", "why"], "additionalProperties": False}},
        "interview_questions": {"type": "array", "items": {"type": "string"},
                                "description": "3 questions the interviewer is likely to probe, given the gaps"},
    },
    "required": ["fit_score", "summary", "strengths", "gaps", "bullet_rewrites", "interview_questions"],
    "additionalProperties": False,
}


def analyze(resume: str, job: str, client: anthropic.Anthropic | None = None) -> dict:
    client = client or anthropic.Anthropic()
    response = client.beta.messages.create(
        model=MODEL,
        max_tokens=16000,
        system=SYSTEM,
        output_config={"effort": "medium", "format": {"type": "json_schema", "schema": SCHEMA}},
        betas=["server-side-fallback-2026-07-01"],
        fallbacks="default",
        messages=[{"role": "user", "content": f"<resume>\n{resume}\n</resume>\n\n<job_description>\n{job}\n</job_description>"}],
    )
    if response.stop_reason == "refusal":
        raise RuntimeError("The model declined this request.")
    text = next(block.text for block in response.content if block.type == "text")
    return json.loads(text)
