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

