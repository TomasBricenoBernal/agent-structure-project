## Agent Roles

Full role specifications live as Claude Code subagents in `.claude/agents/*.md`.
That directory is the single source of truth for each role's purpose, triggers,
rules, limitations, tools, and model. The main agent delegates to a subagent by
name (see the activation table in Work Modes); each subagent runs in its own
isolated context, so its work does not consume the main thread's tokens.

Do not duplicate role specifications here. Update the subagent file instead.

Role label (used in the activation table and in QA `review_agents`) → subagent:

| Role label | Subagent | Model |
|---|---|---|
| Architect | `architect` | opus |
| Backend | `backend` | sonnet |
| Database | `database` | opus |
| Data | `data-analytics` | sonnet |
| Machine Learning | `machine-learning` | opus |
| AI Integrations | `ai-integrations` | sonnet |
| Frontend | `frontend-ui` | sonnet |
| QA | `qa` | opus |
| Security | `security` | opus |
| DevOps | `devops` | sonnet |
| Context | `context-manager` | haiku |
| Innovation | `innovation` | haiku |
| (optional UI critic) | `ux-operational` | haiku |

---

## Review Governance

These rules govern the QA-led review workflow and are enforced by
`planning/scripts/validate_task_docs.py` against `.agents/config/review_rules.json`.
They apply across roles, so they live in the always-on protocol rather than
inside a single subagent. Agent labels here (`Security`, `Database`) are the
values written in the QA `review_agents` field.

QA scheduling rule:

- After each non-trivial task review, QA must explicitly decide whether an additional review task is needed.
- If needed, QA schedules a new task and names the required agents such as `Security`, `Database`, or additional `QA`.
- If not needed, QA must record why no follow-up review was scheduled.
- If the follow-up decision fields are incomplete, the task stays `In Review`.
- If a non-negotiable trigger is present, QA cannot close the task without scheduling the required follow-up review.
- If `other` is marked `Yes`, QA cannot close the task without a valid, specific rationale.

Schedule triggers:

- Schedule `Security` review for auth, permissions, secrets, uploads, public exposure, sensitive data, or trust boundaries.
- Schedule `Database` review for schema, migrations, constraints, integrity-sensitive queries, or persisted sensitive fields.
- Schedule combined review tasks when the risk crosses multiple areas and a single task-level review is too narrow.

Non-negotiable triggers:

- `Security` follow-up review is mandatory for login, authentication, authorization, roles, permissions, file upload, secret handling, new public endpoints, external integrations, or persisted sensitive data.
- `Database` follow-up review is mandatory for schema changes, migrations, constraints, persisted sensitive fields, or integrity-sensitive query changes.

Proportionality rule:

- `Light`: local, bounded risk that does not change a core trust boundary.
- `Standard`: normal functional cross-file changes needing extra verification but not the deepest risk class.
- `Deep`: authentication, permissions, trust boundaries, migrations, sensitive data handling, public APIs, or other high-regression surfaces.

`other` rationale rule:

- If `other` is `Yes`, `other_valid_reason` must state: what changed | what concrete risk exists | why the listed triggers do not already cover it | why extra review is needed or why it is still safe not to schedule one.
- Generic reasons such as `por si acaso`, `por seguridad`, or `mejor revisar` are not valid.

---
