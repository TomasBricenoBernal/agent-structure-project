## Token Budget

Default: Low.

### Low

- Max 3 context files.
- Max 2 source files.
- No broad search.

### Medium

- Max 5 context files.
- Max 5 source files.

### High

Only for architecture, security, database design, major refactors, or complex bugs.

Explain why broader context is needed.

## Token Consumption Strategy

Use these rules to reduce token usage without losing correctness:

- Read in layers: task file first, compact context second, source files last.
- Read slices before full files when headings or targeted sections are enough.
- Activate the fewest agents possible for the current step.
- Delay QA, Security, and DevOps until their trigger conditions are present.
- Prefer updating reusable context files over re-explaining the same state in every task.
- Summarize decisions once in canonical files instead of duplicating them across notes.
- Escalate from `Low` to `Medium` or `High` only when the task risk truly requires it.
- If broader context is used, record why in the task notes or plan.

## Token Efficiency Model

Apply improvements in this order:

### Low-Effort Savings

- Assign one lead agent per stage instead of activating multiple peers by default.
- Read diffs, task files, and targeted sections before reading full files.
- Reuse canonical context files instead of repeating project state in task notes.
- Keep agent outputs short and structured.

### Medium-Effort Savings

- Use structured handoffs between agents and stages.
- Break multi-surface work into smaller tasks so each agent reads less context.
- Run QA from changed files, acceptance criteria, and nearby regression risk first.
- Trigger Security only when exposure or trust-boundary conditions change.

### Structural High-Impact Savings

- Maintain feature-level integration review separate from task-level review.
- Keep a stable trigger catalog so specialist agents are not invoked defensively.
- Treat context maintenance as an explicit operational step, not ad hoc narration.
- Favor reusable templates and checklists over free-form review text.

---

