---
name: pmo-status-report
description: Build an executive RAG status report from the Excel PMO tracker (labs/pmo_tracker.xlsx) or a milestone CSV. Use when asked for a portfolio status, steering-committee update, slippage analysis, or critical-path risk summary.
---

# PMO Status Report

You are supporting a pharma/vaccine Enterprise PMO. Produce steering-committee-ready output.

## Steps
1. Run `python labs/status_report.py [file]` (defaults to `labs/pmo_tracker.xlsx`). If you need new logic, change that script; don't write a one-off.
   It computes `slip_days = forecast_date - baseline_date`.
2. RAG rule per milestone (identical to the Excel formulas):
   - **Green**: status is Complete
   - **Red**: status is Delayed, or slip > 30 days on the critical path
   - **Amber**: status is At Risk, or slip 8–30 days
   - **Green**: everything else
   - Off-critical-path Reds don't change project RAG; list them as watch items
3. Project RAG = worst RAG of its critical-path milestones.
4. Write `reports/status_<YYYY-MM-DD>.md` with:
   - One-line headline per project (RAG + biggest driver)
   - Table: milestone, owner, slip_days, RAG — sorted by slip, critical path first
   - Top 3 risks with a proposed mitigation and the decision needed from the steering committee
   - Regulatory impact: flag any slip that pushes a Regulatory milestone
5. Show the headlines in chat and say where the report was saved.

## Rules
- Never invent data. If a column is missing, stop and say so.
- Use dates as-is from the file; state the "as of" date in the report.
- Plain language: the reader is a site head, not a data scientist.
