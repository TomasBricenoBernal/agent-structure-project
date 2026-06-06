## Task Tracking

This repository tracks both features and tasks.

Features represent larger capabilities.

Tasks represent specific units of work that can be implemented, reviewed, or closed independently.

Feature folder:

`planning/features/{id}-{feature-name}/`

Task folder:

`planning/tasks/YYYY/MM/{task-id}-{task-name}/`

---

## Task Tracking Rules

Create a task folder when:

- The work affects more than one file.
- The work belongs to a feature.
- The work requires QA or review.
- The work involves database, security, data processing, architecture, or deployment.
- The work may need handoff across sessions.

Do not create a task folder for trivial one-line or single-file changes unless explicitly requested.

Required task files for non-trivial work:

- `task.md`
- `modified_files.md`
- `qa.md`

Optional task files:

- `handoff.md`
- `plan.md`
- `notes.md`

Create optional files only when needed.

Review task rule:

- QA may create a dedicated review task after reviewing an implementation task or a feature checkpoint.
- Use a dedicated review task when the follow-up review needs a separate specialist pass such as `Security`, `Database`, or cross-task QA integration.
- The review task must record why it was created and which agents must participate.

---

## Active Task Protocol

Before working, read:

1. `planning/tasks/active_task.md`
2. `.agents/context/TASK.md`
3. `.agents/context/current_state.md`
4. Related task folder files.
5. Related feature files only if applicable.

If `planning/tasks/active_task.md` points to a task folder, read only the task files needed for the current work.

`.agents/context/TASK.md` may act as a short operational mirror, but `planning/tasks/active_task.md` is the primary task source.

Use these task statuses only:

- `Planned`
- `In Progress`
- `Blocked`
- `In Review`
- `Done`

Status usage:

- Use `Planned` when the task exists but work has not started, or when it is intentionally postponed.
- Use `In Progress` when work started and the task is expected to continue later.
- Use `Blocked` when work started but cannot continue because of a dependency, decision, or external issue.
- Use `In Review` when implementation is complete and QA, and Security if applicable, are still pending.
- Use `Done` only when implementation, required review, and close-out updates are complete.

Review flow:

- Implementation completion moves the task to `In Review`, not directly to `Done`.
- `QA` review is required before `Done`.
- `Security` review is required only when the task touches a sensitive area.
- If review finds issues, move the task back to `In Progress` or `Blocked`.
- A non-trivial task cannot move to `Done` if `qa.md` is missing.
- A non-trivial task cannot move to `Done` if the QA follow-up review decision is missing.

QA review depth:

- Use `Light` for small local changes with low regression risk.
- Use `Standard` for normal functional changes, validations, services, and operator-facing behavior.
- Use `Deep` for database, migrations, security-sensitive changes, Excel/CSV, calculations, machine learning, public APIs, or high-regression-risk work.

Security review triggers:

- Authentication, authorization, roles, or permissions.
- File upload or file handling.
- Secrets, credentials, or sensitive configuration.
- Public endpoints or externally exposed integrations.
- Sensitive data fields, logs, errors, or production traces.
- Backend validation changes that affect trust boundaries.
- Database changes involving sensitive fields or access patterns.

---

## Task Completion Rule

A non-trivial task is not complete until:

- Task `modified_files.md` is updated.
- Task `handoff.md` is updated if the task is paused, handed off, blocked, or left for a later session.
- Related feature `modified_files.md` is updated if the task belongs to a feature.
- Related feature `changes_current.md` is updated if behavior changed.
- `.agents/context/current_state.md` is updated if project state changed.
- Required QA review is completed.
- Required Security review is completed when security triggers apply.
- `planning/tasks/active_task.md` is updated to Done, Blocked, In Review, or the next active task.

Quick close-out checklist:

- Changed files recorded.
- Tests run or not run recorded.
- Risks or blockers recorded.
- QA review recorded.
- Security review recorded if applicable.
- Task docs validated with `python planning/scripts/validate_task_docs.py <task-path>`.
- Status updated.
- Next step recorded if the task is not done.

---

