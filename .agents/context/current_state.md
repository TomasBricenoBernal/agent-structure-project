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
