---
name: excel-pmo-tracker
description: Read, update or extend the Excel PMO tracker (labs/pmo_tracker.xlsx or any .xlsx with Milestones/Risks sheets). Use when asked to add milestones or risks, re-score RPNs, add a sheet or column, or check the tracker for errors and inconsistencies.
---

# Excel PMO Tracker

The workbook is a controlled PMO record. Edit it the way you would edit a controlled document.

## Workbook conventions
- Sheets: `Read Me`, `Milestones`, `Risks`, `Dashboard`.
- **Blue text = input cells.** Only write there. **Black text = formulas.** Never overwrite them.
- Dates are real Excel dates formatted `DD-MMM-YYYY`, never text.
- Status values: Not Started, In Progress, At Risk, Delayed, Complete (drop-down list).
- RPN = Severity × Occurrence × Detection (1–10 each). Action threshold is in `Dashboard!B12`.

## Steps
1. Before editing, list what you will change (sheet, row, column, old → new) and wait for approval.
2. Edit with `openpyxl` (keeps formulas and formatting). Use pandas only for reading.
3. When adding a row, copy the formulas from the row above (Slip, RAG, RPN, Action) and
   extend every range that refers to the table (Dashboard COUNTIFS, conditional formatting).
4. Save a copy first: `labs/archive/pmo_tracker_<YYYY-MM-DD>.xlsx`. This is your audit trail.
5. Check the result: reopen the file and confirm the new rows have formulas, not typed values.
6. Run `python labs/status_report.py` and show the headlines.

## Data integrity checks (run when asked to "check" the tracker)
- Forecast date earlier than baseline with status not Complete → ask whether the baseline was re-planned
- Status Complete but forecast date in the future → flag
- Risk scores outside 1–10, blank owner, or duplicate Risk ID → flag
- Critical Path not Y/N → flag
Report each issue as a table: sheet, cell, issue, suggested fix. Do not fix anything without approval.

## Rules
- Synthetic or approved data only. Never paste real batch, patient or confidential data into the repo.
- Never use XLOOKUP/FILTER/SORT/UNIQUE: colleagues may be on older Excel. Use INDEX/MATCH and COUNTIFS.
