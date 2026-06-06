## Project Purpose

This repository serves as a reusable base for agent-assisted software work across different project types.

Priorities:

- Correctness.
- Maintainability.
- Clarity.
- Reusability.
- Security.
- Low token usage.

---

## Core Instruction

Do not inspect the whole repository by default.

Use the smallest context required for the task.

Read these first:

1. `tasks/active_task.md`
2. `.agents/context/TASK.md`
3. `.agents/context/current_state.md`

Then read these if present (they are created on demand, not by default):

- `.agents/context/context_manifest.md`
- `.agents/context/source_map.md`
- `.agents/context/known_decisions.md`

If `tasks/active_task.md` and `.agents/context/TASK.md` conflict, follow `tasks/active_task.md` and update `.agents/context/TASK.md`.

For database tasks, also read `.agents/context/database_map.md` if present.

Then read only files related to the active task.

If a required task or feature file does not exist, create it using the repository conventions.

---

## On-Demand Modules

Not imported by default to keep the always-on protocol small. Read with the Read
tool only when the task matches:

- `.agents/protocol/07-database.md` — any task that changes schema, migrations, persistence, relationships, or important queries.
- `.agents/protocol/08-feature-tracking.md` — when creating or updating a feature folder under `features/`.

---

## Create-On-Demand Rule

Do not create documentation files just because they exist in the convention.

Create a file only when:

- The current task needs it.
- The information will be reused.
- The file helps reduce future context.
- The feature is becoming hard to track.

If a required file does not exist, create it using the standard template.

---

