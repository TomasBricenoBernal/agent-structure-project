# Task

- `task_id`: `0005-review-trigger-hardening`
- `title`: `Harden QA review triggers and mandatory follow-up decisions`
- `status`: `Done`
- `related_feature`: `0001-workflow-protocol-foundation`
- `related_feature_path`: `features/0001-workflow-protocol-foundation/`
- `owner`: `Codex`
- `created_on`: `2026-05-24`
- `next_step`: `Create or point to the next active task before starting new non-trivial work.`

## Goal

Reduce under-review and over-review risk by making QA follow-up decisions mandatory, adding non-negotiable triggers, and expanding the decision matrix with an `other` field that requires a valid reason.

## Scope

- In scope:
  - `AGENTS.md`
  - `CLAUDE.md`
  - `.claude/agents/qa.md`
  - `tasks/_templates/qa.md`
  - Task and feature tracking updates
- Out of scope:
  - Application code
  - External automation tooling

## Acceptance Criteria

- QA follow-up review decision is required before task closure.
- Non-negotiable review triggers are explicit.
- Proportional review depth guidance is explicit.
- The QA matrix includes `other` plus mandatory rationale.

## Notes

- This task changes protocol and templates only.
