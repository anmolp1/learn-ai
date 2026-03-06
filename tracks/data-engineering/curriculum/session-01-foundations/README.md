# Session 1: Foundations — AI for Data Engineers

**Format:** 90 min live + async challenge
**Goal:** Build the mental model for using AI in data engineering workflows

## Session Plan

### Opening (10 min)
- Introductions: name, role, what you want to build
- Share 2-3 baseline challenge results — highlight the range of AI experience
- Frame: "AI won't replace data engineers. But data engineers who use AI will replace those who don't."

### Concept: Where AI Fits in the DE Workflow (20 min)

Map AI capabilities to the data engineering lifecycle:

| Stage | Without AI | With AI |
|-------|-----------|---------|
| **Design** | Whiteboard, docs, meetings | AI drafts architecture docs, reviews designs, suggests patterns |
| **Build** | Write pipeline code manually | AI generates boilerplate, writes transformations from natural language |
| **Test** | Write tests manually (or skip them) | AI generates test cases, edge cases, data validation rules |
| **Deploy** | Write Terraform/CI-CD manually | AI generates IaC configs, reviews for security, suggests best practices |
| **Monitor** | Manual checks, basic alerts | AI-powered anomaly detection, root cause analysis, auto-remediation |
| **Document** | "We'll do it later" (never) | AI generates docs from code, keeps them in sync |

Key message: AI is most valuable in the parts of DE that are tedious, repetitive, and often skipped (testing, documentation, monitoring).

### Demo: Prompting Patterns for Data Engineering (30 min)

**Live demo — pick a real task from participant intake forms.**

Patterns specific to DE:

1. **Schema-aware prompting** — Give AI your schema, then ask questions about it
   ```
   Here's my BigQuery schema:
   [paste schema]

   Write a SQL query that calculates the 7-day rolling average of daily_revenue,
   partitioned by product_category. Handle NULL values and weekends.
   ```

2. **Config generation with constraints**
   ```
   Generate a Terraform config for a GCS bucket with the following requirements:
   - Region: us-central1
   - Lifecycle rule: delete objects older than 90 days
   - Versioning enabled
   - Uniform bucket-level access
   - No public access

   Include comments explaining each block.
   ```

3. **Code review prompting**
   ```
   You are a senior data engineer reviewing this Python transformation.
   Check for:
   - Performance issues (unnecessary loops, memory usage, missing vectorization)
   - Data quality risks (NULLs, duplicates, type mismatches)
   - Best practice violations
   - Missing error handling and edge cases

   [paste Python transformation code]
   ```

4. **Debug with context**
   ```
   My Airflow DAG is failing with this error:
   [paste error]

   Here's the relevant task code:
   [paste code]

   Here's the data schema it's reading from:
   [paste schema]

   What's causing the failure? Give me the fix and explain why it broke.
   ```

Show real prompts, real responses, real iterations. Show when Claude gets something wrong and how to fix it.

### Practice (25 min)
- Pick a scenario from [Practice Scenarios](practice-scenarios.md) or use a task from your own work
- Write prompts using the patterns above
- Run in Claude, share results with a partner
- Iterate at least once

### Debrief (5 min)
- One thing that surprised you
- Preview: "Next session we build a full pipeline with AI"

## Async Challenge

### Task
Pick a real data transformation you do at work (or a realistic one). Use AI to:

1. **Generate the SQL/Python** for the transformation
2. **Generate test cases** for it (at least 3 edge cases)
3. **Generate documentation** — a README section explaining what the transformation does, inputs, outputs, assumptions

### Deliverable
Push to your capstone GitHub repo:
- The transformation code
- Test file(s)
- Updated README with documentation

Share in community with `#de-session1`.

## Resources
- [Anthropic Prompt Engineering Guide](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview)
- [dbt Further Learning](../../resources/dbt-further-learning.md) (optional, not required for this track)
- [Terraform GCP Provider Docs](https://registry.terraform.io/providers/hashicorp/google/latest/docs)
- [BigQuery SQL Reference](https://cloud.google.com/bigquery/docs/reference/standard-sql/query-syntax)

---

**Previous:** [Session 0 — Pre-Work](../session-00-prework/)
**Next:** [Session 2 — Pipelines: Build and Transform Data With AI](../session-02-pipelines/)
