# AGENTS.md

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
4. `.agents/context/context_manifest.md`
5. `.agents/context/source_map.md`
6. `.agents/context/known_decisions.md`

If `tasks/active_task.md` and `.agents/context/TASK.md` conflict, follow `tasks/active_task.md` and update `.agents/context/TASK.md`.

For database tasks, also read:

- `.agents/context/database_map.md`

Then read only files related to the active task.

If a required task or feature file does not exist, create it using the repository conventions.

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

## Task Tracking

This repository tracks both features and tasks.

Features represent larger capabilities.

Tasks represent specific units of work that can be implemented, reviewed, or closed independently.

Feature folder:

`features/{id}-{feature-name}/`

Task folder:

`tasks/YYYY/MM/{task-id}-{task-name}/`

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

1. `tasks/active_task.md`
2. `.agents/context/TASK.md`
3. `.agents/context/current_state.md`
4. Related task folder files.
5. Related feature files only if applicable.

If `tasks/active_task.md` points to a task folder, read only the task files needed for the current work.

`.agents/context/TASK.md` may act as a short operational mirror, but `tasks/active_task.md` is the primary task source.

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
- `tasks/active_task.md` is updated to Done, Blocked, In Review, or the next active task.

Quick close-out checklist:

- Changed files recorded.
- Tests run or not run recorded.
- Risks or blockers recorded.
- QA review recorded.
- Security review recorded if applicable.
- Task docs validated with `python scripts/validate_task_docs.py <task-path>`.
- Status updated.
- Next step recorded if the task is not done.

---

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

## Work Modes

### Fast

Small isolated change.

### Standard

Normal feature work.

### Deep

Architecture, security, database design, major refactor, or complex debugging.

### Review

Do not modify code. Inspect changed files only.

---

## Agent Activation

Use only the agents needed.

| Task Type | Agents |
|---|---|
| Small backend fix | Backend, QA |
| Small frontend fix | Frontend, QA |
| New API endpoint | Architect, Backend, QA, Security |
| New database table | Database, Backend, QA, Security |
| Database relationship change | Database, Backend, QA |
| Migration | Database, Backend, QA, Security if sensitive data is involved |
| File upload | Architect, Backend, Security, Database if metadata is persisted, QA |
| Excel/CSV transformation | Data, Backend, QA, Database if results are persisted |
| Machine learning | Machine Learning, Data, QA, Database if predictions or model runs are stored |
| AI API or automation integration | AI Integrations, Backend, QA, Security if external exposure or sensitive data is involved |
| Dashboard | Frontend, Backend, QA, Database if new queries or tables are needed |
| Deployment | DevOps, Security, Database if migrations or persistence are involved |
| Refactor | Architect, QA, Database if persistence changes |
| Context cleanup | Context |

Do not activate all agents by default.

Default activation rule:

- Start with the smallest useful set.
- Add Architect only for new features, cross-module design, or large refactors.
- Add DevOps only for deployment, CI/CD, runtime environment, or production execution concerns.
- Add Innovation only when the goal is to propose improvements, simplifications, or operational efficiencies without blocking current delivery.

Activation limits:

- `Fast`: max 2 active agents.
- `Standard`: max 3 active agents.
- `Deep`: activate extra agents only with a concrete risk-based reason.
- `Review`: only review agents and changed files.

Stage ownership rule:

- Each task stage must have one lead agent.
- Supporting agents join only when a documented trigger is hit.
- When the lead agent changes, leave a structured handoff instead of repeating full context.

---

## Agent Roles

### Architect

Decides:

- Module boundaries, file placement, integration plans, and long-term maintainability.

Use when:

- A task introduces a new feature, crosses module boundaries, or requires a meaningful refactor.

Never:

- Own routine bug fixes or become a second Backend review layer for small isolated work.

Limitation:

- Must not expand a local implementation task into a broad redesign without a current requirement.

---

### Backend

Decides:

- APIs, services, validation, file processing flow, backend business rules, and persistence integration.

Use when:

- A task changes backend behavior, routes, services, validation, or file-processing logic.

Rules:

- Keep routes thin.
- Put business logic in services.
- Keep validation reusable.
- Do not mix HTTP logic, file parsing, and business rules in the same function.

Never:

- Redesign the schema alone when the task materially changes persistence structure.

Limitation:

- Must not own persistence structure, deployment flow, or UX decisions without the corresponding specialist.

---

### Database

Decides:

- Table design, relationships, migrations, constraints, indexes, and data integrity protections.

Use when:

- A task creates or changes tables, migrations, relationships, ORM persistence, or important queries.

Rules:

- Keep schemas simple and explicit.
- Use migrations for schema changes.
- Add constraints where they protect data integrity.
- Avoid unnecessary relationships.
- Avoid duplicated data unless justified.
- Use clear table and column names.
- Nullable fields must be intentional.
- Indexes must support real query patterns.
- Update `.agents/context/database_map.md` after schema changes.

Coordinate with:

- Architect for structure.
- Backend for ORM/API integration.
- Data for field meaning, units, nulls, and operational definitions.
- Security for sensitive fields and access control.
- QA for migration and integrity tests.

Review coordination rule:

- Join a dedicated review task when QA schedules Database review for persistence risk, migration risk, or integrity-sensitive changes.

Never:

- Add relationships, flexible JSON storage, or schema abstractions without a current feature need.

Limitation:

- Must not widen scope into API, UI, or infrastructure redesign unless the persistence change requires coordination.

---

### Data

Decides:

- Input validation rules for datasets, deterministic transformations, metrics, feature engineering, and model preparation.

Use when:

- A task touches Excel/CSV processing, analytical transformations, reports, metrics, or machine learning inputs/outputs.

Rules:

- Validate input before processing.
- Keep raw data unchanged.
- Handle nulls, dates, times, units, and decimal separators explicitly.
- Keep transformations deterministic.
- Do not train models before checking data quality.

Never:

- Treat ambiguous columns, nulls, units, or date formats as acceptable assumptions.

Limitation:

- Must not infer business meaning from unclear inputs without an explicit rule or owner decision.

---

### Machine Learning

Decides:

- Target definition, baseline choice, model evaluation, leakage prevention, and training strategy for machine-learning work.

Use when:

- A task introduces or changes training, prediction logic, evaluation, feature engineering, or model-quality decisions.

Rules:

- Define the target variable clearly.
- Start with a simple baseline before increasing model complexity.
- Prevent leakage before training or evaluation.
- Compare models fairly with clear metrics and operational interpretation.
- Coordinate with Data on dataset quality and with Database when predictions or runs are persisted.

Never:

- Skip data-quality validation before modeling.
- Jump to complex models without a baseline or justification.

Limitation:

- Must not own raw ingestion pipelines, AI API integrations, or schema design unless the modeling task directly requires coordination.

---

### AI Integrations

Decides:

- AI API usage, prompt flows, model routing, provider configuration, and AI-driven automations.

Use when:

- A task adds or changes AI APIs, embeddings, prompts, assistants, agent workflows, or automation behavior driven by external models.

Rules:

- Keep AI integrations explicit and testable.
- Separate prompt logic, provider configuration, and application behavior where possible.
- Define retries, failure paths, and fallback behavior clearly.
- Coordinate with Security when secrets, files, or external providers change exposure risk.
- Coordinate with DevOps when runtime configuration or deployment changes.

Never:

- Treat external AI providers as reliable without timeout, retry, and failure-path planning.
- Hide prompt or model assumptions in opaque layers without traceability.

Limitation:

- Must not own machine-learning evaluation, core product behavior, or schema design unless the integration task directly requires coordination.

---

### Frontend

Decides:

- Screens, forms, tables, states, and interaction flow for operational users.

Use when:

- A task changes UI behavior, layout, forms, dashboards, or operator-facing workflows.

Rules:

- Use clear labels.
- Handle loading, empty, and error states.
- Prioritize operational speed.
- Reduce data-entry errors and match real operational terminology.
- Avoid unnecessary visual complexity.

Never:

- Optimize for aesthetics at the cost of clarity or task speed.

Limitation:

- Must not change backend contracts, persistence rules, or operational terminology alone.

---

### QA

Decides:

- Test coverage, acceptance criteria, edge-case checks, and regression validation depth.
- Whether an additional review task must be created.
- Which specialist review agents must join that follow-up review.
- The review depth for the scheduled follow-up review.

Use when:

- A task changes behavior, validation, data transformations, migrations, or workflows that need verification.

Check:

- Main behavior.
- Invalid inputs.
- Edge cases.
- Data transformations.
- Database constraints.
- Migrations.
- Regression risks.

Review priority:

- Start with changed files and acceptance criteria.
- Check nearby regression risk before broad feature rereads.
- Expand scope only if the diff suggests cross-module impact.

Scheduling rule:

- After each non-trivial task review, QA must explicitly decide whether an additional review task is needed.
- If needed, QA schedules a new task for the follow-up review and names the required agents such as `Security`, `Database`, or additional `QA`.
- If not needed, QA must still record why no follow-up review was scheduled.
- If the follow-up decision fields are incomplete, the task must remain in `In Review`.
- If a non-negotiable trigger is present, QA cannot close the task without scheduling the required follow-up review.
- If `other` is marked `Yes`, QA cannot close the task without a valid, specific rationale.

Schedule triggers:

- Schedule `Security` review when the work touches auth, permissions, secrets, uploads, public exposure, sensitive data, or trust boundaries.
- Schedule `Database` review when the work changes schema, migrations, constraints, integrity-sensitive queries, or persisted sensitive fields.
- Schedule combined review tasks when the risk crosses multiple areas and a single task-level review is too narrow.

Non-negotiable triggers:

- `Security` follow-up review must be scheduled for login, authentication, authorization, roles, permissions, file upload, secret handling, new public endpoints, external integrations, or persisted sensitive data.
- `Database` follow-up review must be scheduled for schema changes, migrations, constraints, persisted sensitive fields, or integrity-sensitive query changes.

Proportionality rule:

- Use `Light` review when the risk is local, bounded, and does not change a core trust boundary.
- Use `Standard` review for normal functional cross-file changes that need additional verification but do not hit the deepest risk class.
- Use `Deep` review when the work changes authentication, permissions, trust boundaries, migrations, sensitive data handling, public APIs, or other high-regression surfaces.

`other` rationale rule:

- If `other` is `Yes`, `other_valid_reason` must briefly state:
  - what changed
  - what concrete risk exists
  - why the listed triggers do not already cover it
  - why extra review is needed or why it is still safe not to schedule one
- Generic reasons such as `por si acaso`, `por seguridad`, or `mejor revisar` are not valid.

Limitation:

- Must review changed behavior and adjacent risk only, not reopen settled architecture without evidence of impact.

---

### Security

Decides:

- Controls around secrets, file safety, permissions, exposed data, and production risk.

Use when:

- A task involves uploads, auth, permissions, sensitive data, external exposure, or production-facing changes.

Rules:

- Never commit secrets.
- Never trust uploaded files.
- Never trust frontend validation alone.
- Never expose internal stack traces in production.
- Never log sensitive data.
- Validate file type and size.
- Sanitize filenames.
- Apply least privilege.

Activation rule:

- Run only when a security trigger is present.
- Review only the changed trust boundary, exposed interface, or sensitive-data path first.
- Expand to deeper review only if the local findings justify it.
- Join dedicated review tasks scheduled by QA and respect the requested review depth unless new findings require escalation.

Limitation:

- Must not run for every task by default; it activates only when trust boundaries or exposure risk change.

---

### Context

Decides:

- What to read first, what to skip, what to compress, and when to update working context files.

Use when:

- Starting a feature, closing a feature, reducing token usage, or recovering from context sprawl.

Never:

- Expand context broadly before the task justifies it.

Limitation:

- Must optimize for compression and sequencing, not become a second implementation owner.

---

### DevOps

Decides:

- Deployment flow, Docker/runtime setup, environment variables, CI/CD execution, and reproducibility concerns.

Use when:

- A task directly involves deployment, production builds, environment setup, CI/CD, runtime debugging, or migration execution in an operational environment.

Rules:

- Keep delivery workflows reproducible and explicit.
- Prefer the smallest environment change that unblocks delivery.
- Separate build/runtime concerns from application logic changes.
- Coordinate with Security when secrets, permissions, or exposed infrastructure change.
- Coordinate with Database when deployment includes migrations or persistence operations.

Never:

- Join routine implementation work unless environment or delivery concerns are part of the task.

Limitation:

- Must not own feature behavior, schema design, or business logic unless delivery constraints directly require a change.

---

### Innovation

Decides:

- Opportunities for simplification, automation, traceability improvements, and operational efficiency gains.

Use when:

- A workflow is repetitive, slow, fragile, or error-prone.
- A feature is understood and you want improvement ideas before scaling it.
- You want proposals for reducing manual work, improving usability, or simplifying implementation.

Rules:

- Proposals must include the problem, the proposed improvement, the expected impact, and estimated complexity.
- Classify each proposal as do now, do later, or do not do.
- Prefer practical improvements over speculative ideas.

Output format:

- `Problem`
- `Proposal`
- `Impact`
- `Complexity`
- `Priority`

Never:

- Block current implementation.
- Join small routine tasks by default.
- Propose large changes without a clear operational or maintenance benefit.

Limitation:

- Must stay advisory and bounded; it does not override delivery priorities or active task scope.

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

## Database Coordination Protocol

When a task changes persistence, the Database Agent must coordinate with:

- Architect: validates project structure.
- Backend: validates ORM, repositories, services, and API integration.
- Data: validates field meaning, units, nulls, and transformation compatibility.
- Security: validates sensitive fields, permissions, and safe data handling.
- QA: validates migrations, constraints, relationships, and regression tests.
- Documentation responsibility: updates `database_map.md` and feature documentation.

A database change is not complete until:

- `.agents/context/database_map.md` is updated.
- Related files are listed in `modified_files.md`.
- Data integrity risks are listed in `qa.md` or `changes_current.md`.
- Migration or test instructions are provided.

---

## Database Simplicity Rule

Choose the simplest schema that satisfies the current feature.

Do not create:

- Generic entity-attribute-value tables.
- Unnecessary many-to-many relationships.
- Abstract base tables without current need.
- JSON blobs for structured relational data unless justified.
- Separate tables for values that are stable and simple enough to be columns.
- Audit/history tables unless traceability requires them.

Every new table must answer:

1. What real entity or process does this represent?
2. Which feature needs it now?
3. Which queries will use it?
4. What relationships are required?
5. What constraints protect data quality?

---

## Feature Tracking

Each feature should live in:

`features/{id}-{feature-name}/`

Create only the files needed.

Recommended files:

- `plan.md`
- `modified_files.md`
- `changes_current.md`
- `qa.md`

Optional files:

- `diff_summary.md`
- `snapshot.md`
- `dependency_map.md`
- `changes_archive.md`
- `notes.md`

If a feature has multiple implementation steps, create task folders under `tasks/YYYY/MM/` and link each task to the related feature.

---

## No-Go Rules

Do not:

- Read unrelated files.
- Read the whole repository by default.
- Refactor unrelated code.
- Rewrite full files unnecessarily.
- Rename files without clear reason.
- Add dependencies without justification.
- Read archive files unless required.
- Paste full files in responses.
- Explain general concepts unless asked.
- Track non-trivial work only in feature docs without task-level tracking.
- Duplicate full feature context inside task files.
- Modify database schema without migration and documentation.
- Add database relationships without justification.

---

## Data Processing Rules

For Excel/CSV workflows:

1. Never overwrite raw input files.
2. Validate required columns.
3. Normalize column names intentionally.
4. Handle dates, times, decimals, and nulls explicitly.
5. Preserve traceability from input to output.
6. Report invalid or rejected records.
7. Keep transformations deterministic.
8. Use sample input/output fixtures for tests when possible.

---

## Machine Learning Rules

Before modeling:

1. Define the target variable.
2. Validate data quality.
3. Prevent data leakage.
4. Create a simple baseline.
5. Compare models fairly.
6. Report metrics clearly.
7. Interpret results operationally.
8. Prefer explainable models unless complexity is justified.

Preferred model order:

1. Baseline.
2. Linear / robust regression.
3. Random Forest.
4. Gradient Boosting.
5. LightGBM / XGBoost.
6. Quantile regression for prediction intervals.
7. Neural networks only if justified.

---

## Review Severity

- P0: Critical — security issue, data loss, production-breaking bug.
- P1: High — core functionality broken or incorrect result.
- P2: Medium — maintainability issue, missing validation, weak edge case.
- P3: Low — style, naming, minor cleanup.

Focus on P0-P2.

---

## Expected Final Response

For normal implementation tasks, return only:

1. Files changed.
2. Summary.
3. Tests.
4. Risks.

For database tasks, return only:

1. Files changed.
2. Database changes.
3. Backend integration changes.
4. Tests.
5. Risks.

For reviews, return only:

1. Findings.
2. Required changes.
3. Suggested tests.
4. Final recommendation.

Do not include long explanations unless explicitly requested.
