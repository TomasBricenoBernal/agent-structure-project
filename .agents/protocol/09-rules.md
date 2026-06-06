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

