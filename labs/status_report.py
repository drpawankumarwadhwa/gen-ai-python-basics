"""Weekly PMO status report from the Excel tracker (or the CSV).

Usage:  python labs/status_report.py [labs/pmo_tracker.xlsx]
Output: reports/status_<YYYY-MM-DD>.md

The RAG rule is the same as the Excel formulas and the pmo-status-report skill.
Inputs are read and recomputed here, so the script never relies on cached
Excel values (and never edits the workbook).
"""
import sys
from datetime import date
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
RAG_ORDER = {"Red": 0, "Amber": 1, "Green": 2}


def load(path: Path) -> tuple[pd.DataFrame, pd.DataFrame | None]:
    if path.suffix == ".csv":
        ms = pd.read_csv(path, parse_dates=["baseline_date", "forecast_date"])
        return ms, None
    ms = pd.read_excel(path, sheet_name="Milestones", usecols="A:H")
    ms.columns = ["project", "workstream", "milestone", "owner",
                  "baseline_date", "forecast_date", "status", "critical_path"]
    rk = pd.read_excel(path, sheet_name="Risks", usecols="A:G,J:K")
    rk.columns = ["id", "project", "risk", "category", "s", "o", "d", "owner", "mitigation"]
    return ms, rk


def rag(row) -> str:
    if row.status == "Complete":
        return "Green"
    if row.status == "Delayed" or (row.critical_path == "Y" and row.slip_days > 30):
        return "Red"
    if row.status == "At Risk" or 8 <= row.slip_days <= 30:
        return "Amber"
    return "Green"


def main():
    src = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "labs" / "pmo_tracker.xlsx"
    ms, rk = load(src)
    ms["slip_days"] = (ms.forecast_date - ms.baseline_date).dt.days
    ms["rag"] = ms.apply(rag, axis=1)
    ms["rag_rank"] = ms.rag.map(RAG_ORDER)

    today = date.today()
    out = [f"# Portfolio Status Report",
           f"**As of:** {today:%d-%b-%Y} · **Source:** `{src.relative_to(ROOT)}` (synthetic data)", ""]

    out += ["## Headlines", ""]
    for proj, g in ms.groupby("project"):
        cp = g[g.critical_path == "Y"]
        proj_rag = cp.sort_values("rag_rank").rag.iloc[0] if len(cp) else "Green"
        driver = g.sort_values(["rag_rank", "slip_days"], ascending=[True, False]).iloc[0]
        label = "Biggest driver" if driver.critical_path == "Y" else "Watch item (off critical path)"
        out.append(f"- **{proj}: {proj_rag}.** {label}: {driver.milestone} "
                   f"({driver.owner}, {driver.slip_days:+d} days, {driver.status})")
    out.append("")

    out += ["## Milestones", "", "| Project | Milestone | Owner | CP | Slip (days) | RAG |",
            "|---|---|---|---|---|---|"]
    view = ms.sort_values(["critical_path", "slip_days"], ascending=[False, False])
    for r in view.itertuples():
        out.append(f"| {r.project} | {r.milestone} | {r.owner} | {r.critical_path} | {r.slip_days} | {r.rag} |")
    out.append("")

    reg = ms[(ms.workstream == "Regulatory") & (ms.slip_days > 0)]
    out += ["## Regulatory impact", ""]
    out += [f"- {r.project}: **{r.milestone}** forecast {r.forecast_date:%d-%b-%Y} "
            f"({r.slip_days} days late). Check the filing timeline and the market supply plan."
            for r in reg.itertuples()] or ["- No regulatory milestones slipping."]
    out.append("")

    if rk is not None:
        rk["rpn"] = rk.s * rk.o * rk.d
        top = rk.sort_values("rpn", ascending=False).head(3)
        out += ["## Top 3 risks (by RPN = S × O × D)", "",
                "| ID | Project | Risk | RPN | Mitigation | Decision needed |", "|---|---|---|---|---|---|"]
        for r in top.itertuples():
            out.append(f"| {r.id} | {r.project} | {r.risk} | {r.rpn} | {r.mitigation} | "
                       f"Approve mitigation and owner ({r.owner}) |")
        out.append("")

    report = ROOT / "reports" / f"status_{today:%Y-%m-%d}.md"
    report.parent.mkdir(exist_ok=True)
    report.write_text("\n".join(out), encoding="utf-8")
    print("\n".join(out))
    print(f"\nSaved: {report.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
