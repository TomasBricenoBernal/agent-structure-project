# Task

- `task_id`: `0007-task-doc-validation-automation`
- `title`: `Add automated validation for task review documents`
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

Add a lightweight validator that checks task documentation and QA review decisions automatically, while keeping review policy editable through configuration instead of hardcoded Python logic.

## Scope

- In scope:
  - `scripts/validate_task_docs.py`
  - `.agents/config/review_rules.json`
  - `AGENTS.md`
  - `CLAUDE.md`
  - `README.md`
  - Task and feature tracking updates
- Out of scope:
  - CI integration
  - Application code
  - Rewriting existing task content beyond protocol consistency

## Acceptance Criteria

- A local validator script exists and runs without external dependencies.
- Review rules are stored in a config file, not hardcoded end-to-end in Python.
- The validator checks required `qa.md` fields, trigger rules, and review-task existence.
- The repository protocol documents how to run the validator before closing a non-trivial task.

## Review Relationship

- `is_review_task`: `No`
- `review_scope`:
- `review_reason`:

## Notes

- The validator should prefer objective checks and keep policy drift low by reading config from `.agents/config/review_rules.json`.
