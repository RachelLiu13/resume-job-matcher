"""Command line:

    python -m resume_match RESUME JOB [--out report.md] [--no-llm]
"""
import argparse
from pathlib import Path

from dotenv import load_dotenv

from .documents import read_text
from .keywords import keyword_match
from .report import render


def main(argv=None):
    p = argparse.ArgumentParser(description="Compare a resume with a job description.")
    p.add_argument("resume", help=".txt, .md or .pdf")
    p.add_argument("job", help=".txt, .md or .pdf")
    p.add_argument("--out", help="write the Markdown report here (default: print it)")
    p.add_argument("--no-llm", action="store_true", help="keyword check only; no API call")
    args = p.parse_args(argv)

    load_dotenv()
    resume, job = read_text(args.resume), read_text(args.job)
    analysis = None
    if not args.no_llm:
        from .analyze import analyze
        analysis = analyze(resume, job)
    report = render(analysis, keyword_match(resume, job), Path(args.resume).stem, Path(args.job).stem)
    if args.out:
        Path(args.out).write_text(report, encoding="utf-8")
        print(f"Report written to {args.out}")
    else:
        print(report)


if __name__ == "__main__":
    main()
