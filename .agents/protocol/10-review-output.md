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
