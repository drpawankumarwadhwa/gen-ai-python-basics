# Claude Code: Zero to Hero
### A 6-week plan for an AI-enabled PMO leader

**Goal:** go from "installed it" to "my PMO runs AI agents that produce governed, auditable outputs" and turn that into a career signal you can show people.
**Time needed:** about 4 hrs/week (3 × 60-min labs + 1 × 60-min reflection/LinkedIn).
**Practice repo:** this one (`gen-ai-python-basics`). Lab data: `labs/tt_milestones.csv` (synthetic).

---

## The maturity ladder

| Level | Name | You can… | Proof of competence |
|---|---|---|---|
| 0 | Installed | Launch `claude`, ask questions about a repo | Screenshot of first session |
| 1 | Operator | Edit files, run code, commit with Git via chat | 3 commits made through Claude |
| 2 | Configurator | CLAUDE.md, permissions, model choice | CLAUDE.md that changes Claude's behaviour |
| 3 | Integrator | MCP servers (GitHub, Drive, Jira/monday) + Skills | A skill that produces a repeatable PMO report |
| 4 | Automator | Hooks, subagents, headless `claude -p`, GitHub Actions | A scheduled or PR-triggered workflow |
| 5 | Leader | Governance, ROI, scaling to a team | One-page AI SOP + ROI case for leadership |

> The "30-minute setup" infographic covers **Levels 0–3 at awareness depth**. Real fluency comes from building things, which is what weeks 1–6 below are for.

---

## Week 1: Levels 0–1 · Install, first session, Git
| Step | Command / prompt | Why it matters |
|---|---|---|
| Install (Win) | `irm https://claude.ai/install.ps1 \| iex` | Native installer, auto-updates |
| Install (Mac/Linux) | `curl -fsSL https://claude.ai/install.sh \| bash` | |
| Verify | `claude --version` | |
| Launch | `cd gen-ai-python-basics` → `claude` | Claude only sees the folder you start in |
| Orient | *"What does this project do? Explain like I'm a PMO head new to Python."* | Read-only exploration first |
| Help | `/help`, type `/` to list commands | |
| Resume | `claude -c` (continue last), `claude -r` (pick a session) | Work in multi-day sprints |

**Lab 1.1:** *"Fix hello_world.py so it prints a labelled sum, run it, show me the output."*
**Lab 1.2:** *"What files have I changed? Commit them with a clear message."*
✅ **Exit criteria:** you understand the loop **ask → plan → edit → run → review diff → commit**.

## Week 2: Level 2 · Make Claude yours
| Control | How | PMO analogy |
|---|---|---|
| **CLAUDE.md** | `/init`, then edit (see this repo's `CLAUDE.md`) | The project charter: standing context loaded every session |
| **Permission modes** | `Shift+Tab` cycles: default → accept-edits → plan mode | Approval matrix / delegation of authority |
| **Permissions** | `/permissions` allow `Bash(python:*)`, deny `Bash(rm:*)` | Segregation of duties |
| **Model** | `/model`: use the strongest model for design and tricky bugs, a faster one for routine edits | Senior SME vs analyst allocation |
| **Plan mode** | Shift+Tab to *plan* before big changes | Design review before execution (a stage gate) |

**Lab 2.1:** *"Using labs/tt_milestones.csv, compute slip days per milestone and list critical-path items slipping >30 days."* Use **plan mode** first and approve the plan.
**Lab 2.2:** Add a rule to CLAUDE.md (e.g. "always output dates as DD-MMM-YYYY"), rerun, and confirm the behaviour changed.
✅ **Exit:** you can steer Claude through standing instructions instead of re-prompting every time.

## Week 3: Level 3 · Skills (reusable SOPs for AI)
A **Skill** is a folder with a `SKILL.md`: name, description, and steps. Claude loads it automatically when the description matches the task. Treat it as an SOP the AI follows.

- Example already in this repo: `.claude/skills/pmo-status-report/SKILL.md`
- **Lab 3.1:** *"Generate this week's status report."* Watch the skill trigger, then review `reports/`.
- **Lab 3.2:** Write your own skill, e.g. `risk-register-review` (scores RPN = S×O×D like a pFMEA and flags RPN > 100) or `change-control-impact` (CC → affected docs, validation, filing category).
- `/plugin` lets you browse the marketplace for pre-built skill bundles.

✅ **Exit:** two skills that give the same quality output every time, no matter who runs them.

## Week 4: Level 3 · MCP: connect your tools
MCP (Model Context Protocol) servers let Claude read and act in other systems.
```
claude mcp add --transport http <name> <server-url>
claude mcp list        # look for ✓ Connected
/mcp                   # authenticate inside a session
```
| Connect | PMO use case |
|---|---|
| GitHub | Version-controlled PMO artefacts with audit trail |
| monday.com / Jira | Pull live milestones, then run status-report skill |
| Google Drive / M365 | Read SOP/charter drafts, draft steering-committee packs |
| PubMed / ClinicalTrials.gov | Competitive intel for portfolio prioritisation |

**Lab 4.1:** Connect one board (monday/Jira) and run *"Pull open milestones and produce the RAG report."*
✅ **Exit:** live data → governed report with no copy-paste.

## Week 5: Level 4 · Automate
| Feature | What | Example |
|---|---|---|
| **Subagents** (`.claude/agents/*.md`) | Specialist reviewers with their own context | "QA reviewer" checks every report against ALCOA+ wording |
| **Hooks** (`settings.json`) | Shell commands that run on events (e.g. after an edit) | Auto-run `python -m pytest` after each edit |
| **Headless** | `claude -p "generate status report" ` | Run from Windows Task Scheduler every Monday 7 am |
| **GitHub Actions** | `/install-github-app` → `@claude` in PRs/issues | Team requests a report by opening an issue |

**Lab 5.1:** Schedule the weekly status report headlessly.
✅ **Exit:** a report that arrives every week without you prompting.

## Week 6: Level 5 · Lead: governance, ROI, career leverage
**Governance checklist (GxP-aware)**
- [ ] Synthetic or de-identified data only, until IT/QA approve the tool
- [ ] Human review before any output enters a GMP record (Claude drafts; a person approves)
- [ ] Use a risk-based approach (FDA CSA / GAMP 5 2nd ed.): reports for decision support are low-risk, anything that touches a GxP record is high-risk
- [ ] Version control = audit trail (who, what, when) supports Part 11 / Annex 11 thinking
- [ ] Permission deny-list for destructive commands; no secrets in repos

**ROI template** (fill in with your own numbers)
| Activity | Hrs/week before | After | Saved/yr (×48 wks) |
|---|---|---|---|
| Weekly portfolio RAG pack | 6 | 1 | 240 h |
| CC impact assessments (draft) | 5 | 2 | 144 h |
| Steering-committee minutes & actions | 3 | 0.5 | 120 h |
| **Total** | | | **~500 h ≈ 0.25 FTE of a senior PM** |

**Career outputs**
1. A public GitHub repo (this one) showing skills, CLAUDE.md, and an automated report, built on synthetic data.
2. A LinkedIn post series: "6 weeks to an AI-enabled PMO", one post per level, each with a screenshot.
3. A one-page "AI in the PMO" SOP + ROI case to put in front of your site head. This is the strongest signal for a Portfolio Director or Enterprise PMO role.

---

## Prompting habits that work
1. **Describe the finished result, not the fix:** "a one-page RAG report a site head can read in 2 minutes".
2. **Break big work into numbered steps** and approve each step.
3. **Say "run it and show me the output before you stop"** so Claude verifies its own work.
4. **Review the diff before you say Yes,** the same way you'd review a deviation before closing it.
5. **When the output is wrong, fix the cause:** update CLAUDE.md or the skill so the mistake doesn't come back.
