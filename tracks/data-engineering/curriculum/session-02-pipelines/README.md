# Session 2: Pipelines — Build and Transform Data With AI

**Format:** 90 min live + async challenge
**Goal:** Build a complete data pipeline from ingestion to transformation using AI

## Session Plan

### Concept (15 min): The AI-Assisted Pipeline Development Workflow

The workflow:
1. **Describe** what you want in natural language → AI generates the skeleton
2. **Review** the generated code — understand every line before running it
3. **Test** with sample data — AI generates test fixtures and validation
4. **Iterate** — refine prompts, fix issues, add edge case handling
5. **Document** — AI generates docs from the final code

Key principle: AI writes the first draft. You own the final version.

### Demo (35 min): Build a Pipeline From Scratch

**Build a complete pipeline live.** Suggested project: a pipeline that ingests data from a public API, transforms it, and loads it into BigQuery.

**Step 1 — Ingestion (15 min)**
Use Claude to generate a Python script that:
- Hits a public API (e.g., OpenWeather, GitHub API, any free API)
- Handles pagination, rate limiting, error retries
- Writes raw data to a staging location (GCS or local)

Show the prompt, show the output, show what needs fixing.

**Step 2 — Transformation (15 min)**
Use Claude to generate Python transformations:
- Cleaning: handle nulls, type casting, deduplication
- Business logic: aggregations, calculations, derived fields
- Quality checks: assert uniqueness, not-null, accepted values

Show how to give Claude your schema and get back transformation code.

**Step 3 — Testing (5 min)**
Use Claude to generate:
- Unit tests for transformation functions
- Data validation tests (row counts, schema checks, value ranges)
- A test data fixture

> **Note on orchestration:** For most capstones, orchestration is a simple `run_pipeline.py` that calls ingestion then transformation in sequence. You don't need Airflow or a scheduler — a Python script is enough. See the [starter pipeline](../../examples/starter-pipeline/) for an example.

### Practice (25 min)

> **Choose your path based on your experience level:**
>
> **If this is new to you** — Start with Path A. Use the starter template, focus on understanding each component, and modify one thing to make it yours.
>
> **If you're experienced** — Go with Path B. Build from scratch, pick a more complex data source, and challenge yourself on edge case handling.

**Path A — Fork the starter pipeline** (recommended if this is your first pipeline):
1. Copy the [starter pipeline](../../examples/starter-pipeline/) into your capstone repo
2. Run it with sample data to verify it works
3. Modify one transformation or swap the data source
4. Push to GitHub

**Path B — Build from scratch:**
1. Choose a data source from [Data Sources](../../resources/data-sources.md)
2. Use AI to generate the ingestion layer
3. Use AI to generate at least 2 transformations
4. Push to GitHub

### Capstone Scope Check (5 min)
Quick round-robin: each participant shares their capstone plan in 30 seconds. Trainer flags anything too ambitious or too narrow.

### Debrief (10 min)
- What broke? What did AI get wrong?
- Patterns: what types of pipeline code does AI handle well vs. poorly?

## Async Challenge

### Task
Build the ingestion + transformation layers of your capstone pipeline:

1. **Ingestion:** Script that pulls data from your chosen source. Handle errors and edge cases.
2. **Transformation:** At least 3 transformation steps with clear business logic.
3. **Tests:** At least 3 test cases covering happy path and edge cases.
4. **README:** Document what the pipeline does, data source, schema, how to run it.

### Quality Bar
- Code runs without errors on sample data
- Tests pass
- Another person could clone the repo and understand what's happening

Push to GitHub, share in community with `#de-session2`.

> **Falling behind?** Copy the [starter pipeline](../../examples/starter-pipeline/) into your capstone repo to get a working ingestion + transformation pipeline. See [Checkpoints](../../resources/checkpoints.md) for details. It's an express lane, not a backup plan — customize it to make it yours.

## Key Concepts

### What AI Does Well in Pipeline Code
- Boilerplate: API clients, file I/O, error handling patterns
- SQL transformations from natural language descriptions
- Test case generation (especially edge cases you wouldn't think of)
- Documentation from code

### What AI Struggles With
- Complex business logic that requires domain context
- Performance optimization for your specific data volumes
- Choosing the right architecture (it'll give you a working answer, not necessarily the best one)
- Understanding your data quality issues without seeing real data

### The "Read Before You Run" Rule
Never execute AI-generated pipeline code without reading every line. Specifically check:
- SQL: Is it doing full table scans? Missing WHERE clauses? Wrong JOINs?
- Python: Is it handling connection cleanup? Memory management? File handles?
- APIs: Is it respecting rate limits? Handling auth correctly?

---

**Previous:** [Session 1 — Foundations](../session-01-foundations/)
**Next:** [Session 3 — Infrastructure-as-Code: Terraform + AI](../session-03-iac/)
