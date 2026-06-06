# Task

- `task_id`: `0008-add-ml-and-ai-agents`
- `title`: `Add machine learning and AI integration agent specializations`
- `status`: `Done`
- `related_feature`: `0001-workflow-protocol-foundation`
- `related_feature_path`: `features/0001-workflow-protocol-foundation/`
- `owner`: `Codex`
- `created_on`: `2026-05-24`
- `parent_task`:
- `review_requested_by`:
- `review_agents`:
- `next_step`: `Create or point to the next active task before starting new non-trivial work.`

## Goal

Add a dedicated `Machine Learning` agent specialization and a separate `AI Integrations` agent for AI APIs, model integrations, prompts, and automation workflows.

## Scope

- In scope:
  - `AGENTS.md`
  - `CLAUDE.md`
  - `README.md`
  - `.claude/agents/machine-learning.md`
  - `.claude/agents/ai-integrations.md`
  - Task and feature tracking updates
- Out of scope:
  - Application code
  - External AI provider implementation
  - Changes to existing non-AI agent responsibilities beyond coordination notes

## Acceptance Criteria

- `Machine Learning` has a dedicated `.claude/agents` specialization.
- `AI Integrations` has a dedicated `.claude/agents` specialization.
- `AGENTS.md` and `CLAUDE.md` reference both roles consistently.
- `README.md` lists the new roles in the repository overview.

## Review Relationship

- `is_review_task`: `No`
- `review_scope`:
- `review_reason`:

## Notes

- The goal is to close the gap between the shared protocol and the available Claude agent files.
