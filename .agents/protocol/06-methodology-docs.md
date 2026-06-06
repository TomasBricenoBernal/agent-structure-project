## Development Methodology

Use this repository workflow for normal delivery:

1. Activate `Context` first to confirm the smallest valid reading path.
2. Open or point to a task when the work is non-trivial or crosses files.
3. Assign one lead agent for the current stage and keep other agents inactive unless triggered.
4. Add specialist agents only when their trigger conditions are reached.
5. When ownership changes, write a short structured handoff instead of re-explaining full context.
6. Record reusable decisions in shared context or feature files instead of repeating them in chat.
7. Move the task to `In Review` after implementation, then run QA from diff, acceptance criteria, and nearby regression risk.
8. During QA, explicitly decide whether a dedicated follow-up review task is needed and record the rationale.
9. If a follow-up review is needed, create a new review task and assign the required review agents and depth.
10. Run Security or Database review directly only when QA determines a separate review task is unnecessary and the protocol still requires a local pass.
11. Run `python scripts/validate_task_docs.py <task-path>` before closing a non-trivial task.
12. Move to `Done` only after tracking, QA, validation, and any scheduled follow-up reviews are complete.

---

## Documentation Rule

Documentation is not a default agent.

Use documentation as a closing responsibility when:

- A decision will be reused.
- A schema change requires traceability.
- A feature is becoming hard to track.

Rules:

- Document decisions, not conversations.
- Avoid duplication.
- Update only relevant docs.
- Keep docs short.

---

