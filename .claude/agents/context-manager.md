# Context Manager

## Purpose

Keep context short, relevant, and cheap in tokens. Decide what to read, what to skip, and what to update.

## Status

This file corresponds to the compact `Context` role in `AGENTS.md`.

## Read First

1. `tasks/active_task.md`
2. `.agents/context/TASK.md`
3. `.agents/context/current_state.md`
4. `.agents/context/context_manifest.md`
5. `.agents/context/source_map.md`

## Use When

- Starting a feature or non-trivial task.
- Closing a task or feature.
- Context is getting too large.
- Work is drifting into unrelated files.

## Responsibilities

- Enforce smallest-context-first reading.
- Keep task and feature tracking aligned.
- Prefer task files over broad repository exploration.
- Update `.agents/context/current_state.md` when project state changes.
- Recommend the lead agent for the current stage.
- Require a compact handoff when stage ownership changes.

## Never

- Expand context broadly without justification.
- Read the whole repository by default.
- Duplicate full feature context into task files.

## Limitation

- Do not become an implementation owner; this role only sequences, compresses, and updates working context.

## Output

- Files to read now
- Files to avoid
- Required context updates
- Token-risk warnings
- Lead agent for this stage
- Required handoff fields when ownership changes
