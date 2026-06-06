## Protocol Authority

This is the global protocol for this repository. `CLAUDE.md` and `AGENTS.md` are
thin indexes that import the same modules from `.agents/protocol/`.

`.claude/agents/*.md` are Claude Code subagents and the single source of truth
for each role's behavior, triggers, tools, and model.

If the protocol modules and a subagent file ever diverge:

- Follow the protocol modules for repository-wide rules (workflow, token budget, review governance).
- Follow the subagent file for that role's own behavior and limits.
- Keep `CLAUDE.md` and `AGENTS.md` synchronized; both only import `.agents/protocol/`.

---

