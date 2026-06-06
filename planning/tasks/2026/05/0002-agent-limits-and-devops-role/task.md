# Task

- `task_id`: `0002-agent-limits-and-devops-role`
- `title`: `Refine agent limits, token strategy, and DevOps role`
- `status`: `Done`
- `related_feature`: `0001-workflow-protocol-foundation`
- `related_feature_path`: `features/0001-workflow-protocol-foundation/`
- `owner`: `Codex`
- `created_on`: `2026-05-24`
- `next_step`: `Choose the next active protocol or repository task before starting new non-trivial work.`

## Goal

Clarify how the repository should consume tokens, define an explicit DevOps role, and add hard limitations for each agent without changing the overall folder structure.

## Scope

- In scope:
  - `AGENTS.md`
  - `CLAUDE.md`
  - `.claude/agents/*.md`
  - Task and feature tracking updates related to this protocol change
- Out of scope:
  - Application code
  - Database schema
  - CI implementation details outside role definition

## Acceptance Criteria

- `AGENTS.md` and `CLAUDE.md` remain aligned.
- Every agent has an explicit limitation or boundary.
- A dedicated `DevOps` agent specialization exists.
- The shared methodology explains how work should flow with minimal token usage.

## Notes

- This is a protocol and documentation change only.
