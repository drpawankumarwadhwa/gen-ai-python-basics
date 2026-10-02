# CLAUDE.md — gen-ai-python-basics

Personal learning repo: Python + Generative AI basics, used as a Claude Code practice ground.

## Owner context
- Learner is a PMO Head in vaccine/pharma manufacturing (PMP, CPMAI, LSS BB), new to Python.
- Explain code in plain language and relate examples to PMO, tech transfer, QA/RA where possible.

## Layout
- `01_lesson.py`, `hello_world.py` — first Python scripts
- `docs/` — self-made HTML/DOCX study notes (Git, Python ecosystem, MLOps, AI/ML paths)
- `labs/` — hands-on exercises (all data **synthetic**)
  - `pmo_tracker.xlsx` — Excel PMO tracker (Milestones, Risks, Dashboard); rebuild with `python labs/build_pmo_tracker.py`
  - `tt_milestones.csv` — source milestones used to build the tracker
  - `status_report.py` — weekly RAG report → `reports/`
- `.claude/skills/` — project skills: `pmo-status-report`, `excel-pmo-tracker`
- `CLAUDE_CODE_ZERO_TO_HERO.md` — the learning roadmap

## Conventions
- Python 3.11+, pandas for reading tables, openpyxl for editing Excel; keep scripts small and runnable with `python <file>`.
- Write reports to `reports/` (Markdown).
- Never commit real company, batch, patient or GMP data — synthetic data only.
- Before finishing a task: run the script and show the output.
- Excel: write only to blue input cells; never overwrite formulas; archive a copy before edits.
