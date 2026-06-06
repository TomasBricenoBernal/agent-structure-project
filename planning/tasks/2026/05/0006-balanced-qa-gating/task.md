# Task

- `task_id`: `0006-balanced-qa-gating`
- `title`: `Balance QA gating for non-trivial tasks`
- `status`: `Done`
- `related_feature`: `0001-workflow-protocol-foundation`
- `related_feature_path`: `features/0001-workflow-protocol-foundation/`
- `owner`: `Codex`
- `created_on`: `2026-05-24`
- `next_step`: `Create or point to the next active task before starting new non-trivial work.`

## Goal

Require `qa.md` for non-trivial tasks while keeping the blocking rules focused on missing follow-up decisions, non-negotiable triggers, and vague `other` justifications.

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

- `qa.md` is required for non-trivial tasks.
- Closure rules are explicit but proportional.
- `other_valid_reason` has a short required structure.

## Notes

- This task changes protocol and templates only.
