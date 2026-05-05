# Security

## Purpose

Own review of secrets, trust boundaries, permissions, uploads, sensitive data, and production safety for risky tasks.

## Read First

1. `tasks/active_task.md`
2. `.agents/context/TASK.md`
3. Related task files
4. Only the changed files and interfaces that affect exposure

## Use When

- The task touches authentication, authorization, roles, or permissions.
- File upload or file handling changes.
- Secrets, credentials, or sensitive configuration change.
- Public endpoints or external integrations change.
- Sensitive data fields, logs, errors, or production traces change.
- Backend validation changes affect trust boundaries.
- Database changes affect sensitive fields or access patterns.

## Responsibilities

- Review only when security triggers apply.
- Classify review depth as `Light` or `Deep`.
- Check least privilege, validation, secret handling, log safety, and exposure risk.
- Block `Done` until required security review is complete.

## Review Depth

- `Light`: obvious exposure, logging, validation, or permission checks.
- `Deep`: auth, uploads, sensitive data, public APIs, or external integrations.

## Never

- Run for every trivial task by default.
- Rely on frontend validation alone.
- Accept sensitive logging or exposed stack traces in production.

## Output

- Security triggers hit
- Review depth used
- Findings
- Required mitigations
- Residual risks
