# Task

- `task_id`: `0003-token-efficiency-model`
- `title`: `Add a practical token-efficiency model to the workflow protocol`
- `status`: `Done`
- `related_feature`: `0001-workflow-protocol-foundation`
- `related_feature_path`: `features/0001-workflow-protocol-foundation/`
- `owner`: `Codex`
- `created_on`: `2026-05-24`
- `next_step`: `Create or point to the next active task before starting new non-trivial work.`

## Goal

Add a concrete model for reducing token usage while preserving quality, then encode the key operating rules in the shared workflow files.

## Scope

- In scope:
  - `AGENTS.md`
  - `CLAUDE.md`
  - `.claude/agents/context-manager.md`
  - `.claude/agents/qa.md`
  - `.claude/agents/security.md`
  - `tasks/_templates/handoff.md`
  - `tasks/_templates/qa.md`
  - Task and feature tracking updates
- Out of scope:
  - Application code
  - New runtime tooling
  - New persistence or CI implementation

## Acceptance Criteria

- Shared protocol includes a prioritized token-efficiency model.
- Stage ownership and structured handoffs are explicit.
- QA is optimized around diff, acceptance criteria, and nearby regression risk.
- Security is explicitly trigger-based rather than default.

## Notes

- This task applies the agreed protocol changes without changing app behavior.
