#!/usr/bin/env python3
"""Validate task and QA documentation for non-trivial tasks."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Dict, List, Tuple


ROOT = Path(__file__).resolve().parent.parent.parent
DEFAULT_CONFIG = ROOT / ".agents" / "config" / "review_rules.json"
KEY_VALUE_RE = re.compile(r"^\s*-\s+`([^`]+)`:\s*(.*)\s*$")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate task.md and qa.md consistency for task folders."
    )
    parser.add_argument(
        "task_paths",
        nargs="*",
        help="Task folder paths. Defaults to the active task path.",
    )
    parser.add_argument(
        "--config",
        default=str(DEFAULT_CONFIG),
        help="Path to the review rules JSON file.",
    )
    return parser.parse_args()


def load_config(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise SystemExit(f"Config file not found: {path}") from exc
    except json.JSONDecodeError as exc:
        raise SystemExit(f"Invalid JSON in config file {path}: {exc}") from exc


def resolve_task_paths(raw_paths: List[str]) -> List[Path]:
    if raw_paths:
        return [resolve_task_path(Path(path)) for path in raw_paths]

    active_task = parse_markdown_file(ROOT / "planning" / "tasks" / "active_task.md")
    active_path = active_task["root"].get("path", "").strip("`")
    if not active_path:
        raise SystemExit("Could not resolve active task path from planning/tasks/active_task.md")
    return [resolve_task_path(ROOT / active_path)]


def resolve_task_path(path: Path) -> Path:
    candidate = path if path.is_absolute() else ROOT / path
    return candidate.resolve()


def parse_markdown_file(path: Path) -> Dict[str, Dict[str, str]]:
    if not path.exists():
        raise FileNotFoundError(path)

    sections: Dict[str, Dict[str, str]] = {"root": {}}
    current_section = "root"
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.rstrip()
        if line.startswith("## "):
            current_section = line[3:].strip()
            sections.setdefault(current_section, {})
            continue
        match = KEY_VALUE_RE.match(line)
        if not match:
            continue
        key, value = match.groups()
        sections.setdefault(current_section, {})[key] = normalize_value(value)
    return sections


def normalize_value(value: str) -> str:
    value = value.strip()
    if value.startswith("`") and value.endswith("`") and len(value) >= 2:
        return value[1:-1]
    return value


def validate_task_folder(task_path: Path, config: dict) -> List[str]:
    errors: List[str] = []
    rel_task_path = task_path.relative_to(ROOT) if task_path.is_absolute() else task_path

    for required_file in config["required_task_files"]:
        if not (task_path / required_file).exists():
            errors.append(f"{rel_task_path}: missing required file `{required_file}`")

    try:
        task_doc = parse_markdown_file(task_path / "task.md")
    except FileNotFoundError:
        return errors

    try:
        qa_doc = parse_markdown_file(task_path / "qa.md")
    except FileNotFoundError:
        return errors

    task_root = task_doc["root"]
    qa_root = qa_doc["root"]
    follow_up = qa_doc.get("Follow-Up Review Decision", {})
    trigger_matrix = qa_doc.get("Trigger Matrix", {})

    validate_statuses(task_root, qa_root, rel_task_path, config, errors)
    validate_required_fields(qa_root, config["required_qa_fields"], rel_task_path, "qa.md root", errors)
    validate_required_fields(follow_up, config["required_follow_up_fields"], rel_task_path, "qa.md Follow-Up Review Decision", errors)
    validate_required_fields(trigger_matrix, config["required_trigger_matrix_fields"], rel_task_path, "qa.md Trigger Matrix", errors)
    validate_yes_no_fields(follow_up, ["additional_review_needed", "review_task_required"], rel_task_path, errors, config)
    validate_yes_no_fields(
        trigger_matrix,
        [field for field in config["required_trigger_matrix_fields"] if field != "other_valid_reason"],
        rel_task_path,
        errors,
        config,
    )

    task_id = task_root.get("task_id", "")
    qa_task_id = qa_root.get("task_id", "")
    if task_id and qa_task_id and task_id != qa_task_id:
        errors.append(f"{rel_task_path}: task.md task_id `{task_id}` does not match qa.md task_id `{qa_task_id}`")

    if qa_root.get("review_depth") and qa_root["review_depth"] not in config["review_depths"]:
        errors.append(f"{rel_task_path}: invalid qa review_depth `{qa_root['review_depth']}`")

    if follow_up.get("review_depth") and follow_up["review_depth"] not in config["review_depths"]:
        errors.append(f"{rel_task_path}: invalid follow-up review_depth `{follow_up['review_depth']}`")

    validate_follow_up_relationships(task_path, rel_task_path, follow_up, errors)
    validate_non_negotiable_triggers(rel_task_path, follow_up, trigger_matrix, config, errors)
    validate_other_reason(rel_task_path, follow_up, trigger_matrix, config, errors)

    return errors


def validate_statuses(task_root: dict, qa_root: dict, rel_task_path: Path, config: dict, errors: List[str]) -> None:
    task_status = task_root.get("status", "")
    qa_status = qa_root.get("status", "")
    if task_status and task_status not in config["task_statuses"]:
        errors.append(f"{rel_task_path}: invalid task status `{task_status}`")
    if qa_status and qa_status not in config["qa_statuses"]:
        errors.append(f"{rel_task_path}: invalid QA status `{qa_status}`")
    if task_status == "Done" and qa_status != "Done":
        errors.append(f"{rel_task_path}: task is `Done` but qa.md status is `{qa_status or 'missing'}`")


def validate_required_fields(section: dict, fields: List[str], rel_task_path: Path, label: str, errors: List[str]) -> None:
    for field in fields:
        if not section.get(field):
            errors.append(f"{rel_task_path}: missing `{field}` in {label}")


def validate_yes_no_fields(section: dict, fields: List[str], rel_task_path: Path, errors: List[str], config: dict) -> None:
    allowed = set(config["yes_no_values"])
    for field in fields:
        value = section.get(field, "")
        if value and value not in allowed:
            errors.append(f"{rel_task_path}: `{field}` must be one of {sorted(allowed)}, got `{value}`")


def validate_follow_up_relationships(
    task_path: Path, rel_task_path: Path, follow_up: dict, errors: List[str]
) -> None:
    additional_needed = follow_up.get("additional_review_needed")
    task_required = follow_up.get("review_task_required")
    review_agents = follow_up.get("review_agents", "").strip()
    review_reason = follow_up.get("review_reason", "").strip()
    review_depth = follow_up.get("review_depth", "").strip()
    proposed_task_path = follow_up.get("proposed_task_path", "").strip()

    if not review_reason:
        errors.append(f"{rel_task_path}: `review_reason` must explain why extra review was or was not scheduled")

    if additional_needed == "No" and task_required == "Yes":
        errors.append(f"{rel_task_path}: `review_task_required` cannot be `Yes` when `additional_review_needed` is `No`")

    if additional_needed == "Yes":
        if not review_agents:
            errors.append(f"{rel_task_path}: `review_agents` is required when additional review is needed")
        if not review_depth:
            errors.append(f"{rel_task_path}: `review_depth` is required when additional review is needed")

    if task_required == "Yes":
        if not proposed_task_path:
            errors.append(f"{rel_task_path}: `proposed_task_path` is required when `review_task_required` is `Yes`")
        else:
            proposed_path = (ROOT / proposed_task_path).resolve()
            if not proposed_path.exists():
                errors.append(f"{rel_task_path}: proposed review task path does not exist: `{proposed_task_path}`")
            elif not (proposed_path / "task.md").exists():
                errors.append(f"{rel_task_path}: proposed review task is missing `task.md`: `{proposed_task_path}`")


def validate_non_negotiable_triggers(
    rel_task_path: Path, follow_up: dict, trigger_matrix: dict, config: dict, errors: List[str]
) -> None:
    required_agents = set()
    for trigger, agents in config["non_negotiable_triggers"].items():
        if trigger_matrix.get(trigger) == "Yes":
            required_agents.update(agents)

    if not required_agents:
        return

    if follow_up.get("additional_review_needed") != "Yes":
        errors.append(f"{rel_task_path}: non-negotiable triggers require `additional_review_needed` to be `Yes`")
    if follow_up.get("review_task_required") != "Yes":
        errors.append(f"{rel_task_path}: non-negotiable triggers require `review_task_required` to be `Yes`")

    agents_text = follow_up.get("review_agents", "")
    actual_agents = {agent.strip() for agent in agents_text.split(",") if agent.strip()}
    missing_agents = sorted(required_agents - actual_agents)
    if missing_agents:
        errors.append(f"{rel_task_path}: missing required follow-up review agents: {', '.join(missing_agents)}")


def validate_other_reason(
    rel_task_path: Path, follow_up: dict, trigger_matrix: dict, config: dict, errors: List[str]
) -> None:
    other_flag = trigger_matrix.get("other")
    reason = trigger_matrix.get("other_valid_reason", "").strip()
    banned_phrases = {phrase.lower() for phrase in config["generic_other_reason_phrases"]}

    if other_flag == "Yes":
        if not reason:
            errors.append(f"{rel_task_path}: `other_valid_reason` is required when `other` is `Yes`")
            return
        lowered = reason.lower()
        for phrase in banned_phrases:
            if phrase in lowered:
                errors.append(f"{rel_task_path}: `other_valid_reason` contains generic phrase `{phrase}`")
        parts = [part.strip() for part in reason.split(config["other_reason_delimiter"])]
        if len(parts) < config["other_reason_min_parts"] or any(not part for part in parts[: config["other_reason_min_parts"]]):
            errors.append(
                f"{rel_task_path}: `other_valid_reason` must provide at least "
                f"{config['other_reason_min_parts']} non-empty parts separated by `{config['other_reason_delimiter']}`"
            )

        if follow_up.get("review_reason", "").strip() == "":
            errors.append(f"{rel_task_path}: `review_reason` must align with the `other` trigger rationale")


def main() -> int:
    args = parse_args()
    config = load_config(Path(args.config))
    task_paths = resolve_task_paths(args.task_paths)

    all_errors: List[str] = []
    for task_path in task_paths:
        if not task_path.exists():
            all_errors.append(f"Task path does not exist: {task_path}")
            continue
        all_errors.extend(validate_task_folder(task_path, config))

    if all_errors:
        for error in all_errors:
            print(f"ERROR: {error}")
        return 1

    for task_path in task_paths:
        rel_path = task_path.relative_to(ROOT) if task_path.is_absolute() else task_path
        print(f"OK: {rel_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
