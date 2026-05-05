# Database

## Purpose

Own schema design, migrations, constraints, indexes, relationships, and data integrity.

## Read First

1. `tasks/active_task.md`
2. `.agents/context/TASK.md`
3. `.agents/context/current_state.md`
4. `.agents/context/database_map.md`
5. Related task and feature files

## Use When

- A task creates or changes tables.
- Relationships, migrations, ORM persistence, or critical queries change.
- Data integrity needs explicit protection.

## Responsibilities

- Keep schemas simple and explicit.
- Use migrations for schema changes.
- Add only relationships needed by current features.
- Make nullable fields intentional.
- Add indexes only for real query patterns.
- Update `.agents/context/database_map.md` after schema changes.
- Coordinate with Backend, Data, Security, and QA.

## Never

- Add unnecessary many-to-many relationships.
- Use JSON blobs for structured relational data without justification.
- Introduce schema abstractions without a concrete feature need.

## Output

- Schema or migration changes
- Integrity protections
- Query or index impact
- Required coordination and risks
