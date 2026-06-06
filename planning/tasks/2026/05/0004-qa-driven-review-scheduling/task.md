# Task

- `task_id`: `0004-qa-driven-review-scheduling`
- `title`: `Make QA schedule follow-up review tasks when needed`
- `status`: `Done`
- `related_feature`: `0001-workflow-protocol-foundation`
- `related_feature_path`: `features/0001-workflow-protocol-foundation/`
- `owner`: `Codex`
- `created_on`: `2026-05-24`
- `next_step`: `Create or point to the next active task before starting new non-trivial work.`

## Goal

Make QA the formal decision point for additional review tasks, including whether Security or Database review is needed, what depth applies, and why the follow-up review is or is not scheduled.

## Scope

- In scope:
  - `AGENTS.md`
  - `CLAUDE.md`
  - `.claude/agents/qa.md`
  - `.claude/agents/security.md`
  - `.claude/agents/database.md`
  - `tasks/_templates/task.md`
  - `tasks/_templates/qa.md`
  - `tasks/_templates/handoff.md`
  - `features/_templates/plan.md`
  - `features/_templates/qa.md`
  - Task and feature tracking updates
- Out of scope:
  - Application code
  - New automation scripts
  - External orchestration tooling

## Acceptance Criteria

- QA is defined as the decision maker for additional review scheduling.
- The protocol explains when QA should create a dedicated review task.
- Templates capture the review decision, assigned agents, depth, and rationale.
- The protocol also captures when QA decides no extra review is needed and why.

## Notes

- This task implements workflow automation through protocol and templates, not through executable tooling.
