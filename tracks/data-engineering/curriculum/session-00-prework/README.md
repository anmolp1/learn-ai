# Session 0: Pre-Work

**Format:** Async (complete before Session 1)
**Time Required:** ~90-120 minutes
**Goal:** Environment ready, baseline established, project idea in mind

## Setup

### Accounts (All Free Tier)
1. **Claude** — [claude.ai](https://claude.ai). Test it: ask Claude to explain a SQL window function or write a simple Python ETL script.
2. **GitHub** — [github.com](https://github.com). If new to Git, complete [GitHub Skills intro](https://skills.github.com/).
3. **Google Cloud Platform** — [cloud.google.com](https://cloud.google.com/free). Create a project. Enable BigQuery API.
4. **Terraform** — [Install Terraform CLI](https://developer.hashicorp.com/terraform/install). Verify: `terraform --version`

### Local Environment
- Python 3.9+ installed
- A code editor (VS Code recommended, Cursor if you want built-in AI)
- Terminal/shell access
- `pip install dbt-bigquery` (optional, covered in Session 2)

### Verify Everything Works
Run through this checklist:
- [ ] `python --version` returns 3.9+
- [ ] `terraform --version` returns a version
- [ ] `gcloud auth login` succeeds (install gcloud CLI if needed)
- [ ] Can access BigQuery in GCP console
- [ ] Can access Claude and get a response
- [ ] GitHub repo created for your capstone project

## Baseline Challenge

### The Task
Write a simple data pipeline — it can be as basic as:
- Read a CSV file
- Apply 3-5 transformations (filter, rename, aggregate, etc.)
- Write the output somewhere (another file, a database, BigQuery)

### Do It Twice
1. **Without AI:** Write it your normal way. Time yourself.
2. **With AI:** Ask Claude to help you build the same pipeline. Time yourself.

### Document the Difference
Write 3-5 sentences:
- Speed difference?
- Quality difference? Did AI-generated code need fixes?
- What parts of the pipeline were easy/hard for AI?

Share in the community space with `#de-baseline`.

## Think About Your Capstone

Start thinking about a data pipeline you'd like to build. Good capstone projects have:
- A real or realistic data source (public API, open dataset, or your own data)
- 3+ transformation steps
- Cloud deployment (GCP/BigQuery)
- Something you actually care about

Ideas: weather data pipeline, financial data aggregator, social media analytics, IoT sensor processing, e-commerce analytics, log processing pipeline.

## Intake Form
1. Your name and current role
2. DE experience level (1-5)
3. Tools you currently use (SQL, Python, Terraform, dbt, cloud platforms)
4. What capstone project are you considering?
5. Biggest challenge in your current data workflow?

---

**Next:** [Session 1 — Foundations: AI for Data Engineers](../session-01-foundations/)
