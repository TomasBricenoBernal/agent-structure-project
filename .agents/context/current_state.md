# Current State

- Shared workflow protocol now includes explicit token consumption rules and activation ceilings.
- `DevOps` is defined both in the shared protocol and in `.claude/agents/devops.md`.
- Agent-specific limitation rules now reduce overlap, role drift, and unnecessary token consumption.
- Low-token execution now uses stage ownership, structured handoffs, QA by evidence, and trigger-based security review.
- QA now decides when extra review tasks should be created, which review agents must participate, and why the review was or was not scheduled.
- QA follow-up decisions are now mandatory before task closure and use an explicit trigger matrix with required rationale.
- `qa.md` is now required for non-trivial tasks, while closure blocking is reserved for missing decisions, non-negotiable triggers, and weak `other` rationale.
- Task documentation and QA review rules can now be validated locally with `scripts/validate_task_docs.py` using policy from `.agents/config/review_rules.json`.
- The shared protocol now includes dedicated Claude agent files for machine learning and AI integration work.
- `CLAUDE.md` and `AGENTS.md` are now thin indexes that import modular protocol files from `.agents/protocol/`.
- The 13 role files in `.claude/agents/*.md` are now real Claude Code subagents (frontmatter with name, description, tools, model) and the single source of truth for role behavior; `05-agent-roles.md` keeps only the role→subagent map and cross-role review governance.
- Subagent models are tiered: opus for architect/database/machine-learning/qa/security, sonnet for backend/frontend-ui/data-analytics/ai-integrations/devops, haiku for context-manager/innovation/ux-operational.
- `04-work-modes-activation.md` defines a delegation-for-token-efficiency rule: read-heavy/exploratory steps go to subagents so only conclusions return to the main thread.
- `07-database.md` and `08-feature-tracking.md` are no longer imported by default; they are listed under "On-Demand Modules" in `01-foundations.md` and read only when the task matches.
