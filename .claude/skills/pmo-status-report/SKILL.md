---
name: pmo-status-report
description: Build an executive RAG status report from a project milestone CSV (e.g. labs/tt_milestones.csv). Use when asked for a portfolio status, steering-committee update, slippage analysis, or critical-path risk summary.
---

# PMO Status Report

You are supporting a pharma/vaccine Enterprise PMO. Produce steering-committee-ready output.

## Steps
1. Load the CSV with pandas. Compute `slip_days = forecast_date - baseline_date`.
2. RAG rule per milestone:
   - **Red**: status is Delayed, or slip > 30 days on the critical path
   - **Amber**: status is At Risk, or slip 8–30 days
   - **Green**: everything else
3. Project RAG = worst RAG of its critical-path milestones.
4. Write `reports/status_<YYYY-MM-DD>.md` with:
   - One-line headline per project (RAG + biggest driver)
   - Table: milestone, owner, slip_days, RAG — sorted by slip, critical path first
   - Top 3 risks with a proposed mitigation and the decision needed from the steering committee
   - Regulatory impact: flag any slip that pushes a Regulatory milestone
5. Keep the script in `labs/status_report.py` so it is re-runnable and reviewable.

## Rules
- Never invent data. If a column is missing, stop and say so.
- Use dates as-is from the file; state the "as of" date in the report.
- Plain language: the reader is a site head, not a data scientist.
