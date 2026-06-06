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

Role labels in this table are Claude Code subagents in `.claude/agents/`. Some
labels differ from the file name: Data → `data-analytics`, Frontend →
`frontend-ui`, Context → `context-manager`. Delegate to them by subagent name.

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

## Delegation for Token Efficiency

Prefer delegating to a subagent over reading in the main thread when a step is
read-heavy or exploratory, so file contents stay in the subagent's isolated
context and only the conclusion returns to the main thread.

Delegate when:

- A step needs reading many files or a wide search to answer one question.
- The work is self-contained and can be specified in a short brief.
- A specialist role (per the activation table) clearly owns the step.

Keep in the main thread when:

- The change touches 1-2 known files (delegation overhead is not worth it).
- The step needs the full conversation context to be correct.

When delegating, give the subagent: the goal, the exact files or search scope,
and the expected return shape (a short summary or a diff, never raw file dumps).
The reply must be the conclusion, not the contents read. One delegation depth
per step; no recursive delegation by default.

---

