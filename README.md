# AI Workflow Protocol for Agent-Driven Projects

This repository defines a lightweight working protocol for AI-assisted software projects that need strong structure without high coordination overhead.

It is designed for teams using both Codex and Claude in the same codebase.

The goal is to keep work correct, reviewable, and cheap in tokens.

## What This Repository Provides

- a shared repository protocol for Codex and Claude
- task and feature tracking conventions
- review gates with `QA` and risk-based `Security`
- role-specific agent definitions for Claude
- minimal templates for repeatable execution
- reusable repository documentation structure

## Core Principles

- Use the smallest context required.
- Do not inspect the whole repository by default.
- Track non-trivial work at the task level.
- Group related work under features only when it adds value.
- Require `QA` before a task moves to `Done`.
- Require `Security` review only when sensitive risk triggers apply.
- Prefer simple, explicit structures over broad abstractions.

## Repository Structure

```text
.
├── AGENTS.md
├── CLAUDE.md
├── .claude/
│   └── agents/
├── .agents/
│   └── context/
├── tasks/
│   ├── active_task.md
│   ├── _templates/
│   └── YYYY/MM/{task-id}-{task-name}/
├── features/
│   ├── _templates/
│   └── {feature-id}-{feature-name}/
└── docs/
```

## Top-Level Files

- `AGENTS.md`: shared protocol for Codex-style workflows.
- `CLAUDE.md`: shared protocol for Claude, synchronized with the repository rules.
- `.claude/agents/*.md`: role-specific Claude agent instructions.

## Task Model

Tasks are the main execution unit.

Create a task folder when the work:

- affects more than one file
- belongs to a feature
- requires review or handoff
- involves architecture, database, security, data processing, or deployment

Task path format:

```text
tasks/YYYY/MM/{task-id}-{task-name}/
```

Required task files for non-trivial work:

- `task.md`
- `modified_files.md`

Optional task files:

- `handoff.md`
- `plan.md`
- `qa.md`
- `notes.md`

## Feature Model

Features are used only when work represents a meaningful capability, spans multiple tasks, or benefits from grouped tracking.

Feature path format:

```text
features/{feature-id}-{feature-name}/
```

Do not create a new feature for every task.

## Active Task Protocol

Before starting work, read:

1. `tasks/active_task.md`
2. `.agents/context/TASK.md`
3. `.agents/context/current_state.md`
4. only the related task files
5. related feature files only if needed

If `tasks/active_task.md` and `.agents/context/TASK.md` conflict, follow `tasks/active_task.md`.

## Task Statuses

Use only these statuses:

- `Planned`
- `In Progress`
- `Blocked`
- `In Review`
- `Done`

Meaning:

- `Planned`: task exists but has not started, or is intentionally postponed
- `In Progress`: work started and will continue
- `Blocked`: work started but cannot continue
- `In Review`: implementation is complete and required review is pending
- `Done`: implementation, review, and close-out are complete

## Review Flow

The expected flow is:

```text
Planned -> In Progress -> In Review -> Done
```

With fallback transitions:

- `In Review -> In Progress`
- `In Review -> Blocked`

### QA

`QA` review is required before any non-trivial task moves to `Done`.

Review depth:

- `Light`: small local changes with low regression risk
- `Standard`: normal functional changes
- `Deep`: database, migrations, security-sensitive work, Excel/CSV, calculations, ML, public APIs, or high-regression-risk work

### Security

`Security` review is required only when the task touches sensitive areas such as:

- authentication or authorization
- permissions or roles
- file uploads
- secrets or sensitive configuration
- public endpoints
- externally exposed integrations
- sensitive data, logs, or traces
- trust-boundary validation changes

## Documentation Rules

Use:

- `tasks/` for execution, handoff, and review
- `features/` for grouped feature-level tracking
- `docs/` for reusable repository-wide references
- `.agents/context/` for short operational context

Do not use `docs/` for active task logs or temporary handoff notes.

## Included Templates

### Tasks

- `tasks/_templates/task.md`
- `tasks/_templates/modified_files.md`
- `tasks/_templates/handoff.md`
- `tasks/_templates/plan.md`
- `tasks/_templates/qa.md`

### Features

- `features/_templates/modified_files.md`
- `features/_templates/changes_current.md`
- `features/_templates/plan.md`
- `features/_templates/qa.md`

## Claude Agent Roles

Claude role files are available in:

```text
.claude/agents/
```

Included roles:

- `architect`
- `backend`
- `database`
- `qa`
- `security`
- `data-analytics`
- `frontend-ui`
- `ux-operational`
- `innovation`
- `context-manager`

These files specialize behavior by role. They do not replace the repository-wide protocol in `CLAUDE.md`.

## Recommended Workflow

1. Define or update `tasks/active_task.md`.
2. Create a task folder if the work is non-trivial.
3. Link the task to an existing feature, or create a feature only if it adds real tracking value.
4. Work with minimal context.
5. Move the task to `In Review` when implementation is complete.
6. Run required `QA`, and `Security` only if risk triggers apply.
7. Mark the task `Done` only after review and close-out updates.

## Who This Is For

This setup is useful when you want:

- better AI coordination without heavy process
- lower token usage
- clearer handoffs
- stronger review discipline
- a practical structure for ongoing agent-assisted development

## Current State

This repository already includes:

- a bootstrap feature example
- a bootstrap task example
- synchronized `AGENTS.md` and `CLAUDE.md`
- reusable Claude agent definitions

If you want to use this structure in a new project, start by opening the next real task in `tasks/active_task.md`.
