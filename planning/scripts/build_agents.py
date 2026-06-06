#!/usr/bin/env python3
"""Flatten .agents/protocol/*.md into AGENTS.md.

`CLAUDE.md` stays modular: it uses `@import`, which Claude Code expands at load
time. Codex and opencode read `AGENTS.md` as plain text and do not expand
imports, so this script inlines every protocol module into `AGENTS.md`. That way
all three tools receive the full protocol from one source of truth
(`.agents/protocol/`).

Run after editing any protocol module:

    python planning/scripts/build_agents.py
"""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
PROTOCOL_DIR = ROOT / ".agents" / "protocol"
OUTPUT = ROOT / "AGENTS.md"

HEADER = """# AGENTS.md

<!-- GENERATED FILE - do not edit by hand.
     Source of truth: .agents/protocol/*.md
     Regenerate:      python planning/scripts/build_agents.py
     CLAUDE.md stays modular via @import (Claude Code expands it). This file is
     the flattened protocol for tools that read AGENTS.md as plain text
     (Codex, opencode). -->

This is the global protocol for this repository, flattened from
`.agents/protocol/` so any tool that reads `AGENTS.md` as plain text receives the
full content. To change a rule, edit the relevant module under
`.agents/protocol/` and regenerate this file."""


def main() -> int:
    modules = sorted(PROTOCOL_DIR.glob("*.md"))
    if not modules:
        raise SystemExit(f"No protocol modules found in {PROTOCOL_DIR}")

    parts = [HEADER]
    for module in modules:
        parts.append(module.read_text(encoding="utf-8").strip())

    OUTPUT.write_text("\n\n".join(parts) + "\n", encoding="utf-8")
    print(f"Wrote {OUTPUT.relative_to(ROOT)} from {len(modules)} modules:")
    for module in modules:
        print(f"  - {module.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
