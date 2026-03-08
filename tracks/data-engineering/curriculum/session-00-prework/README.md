# Session 0: Pre-Work

**Format:** Async (complete before Session 1)
**Time Required:** ~90-120 minutes
**Goal:** Environment ready, baseline established, project idea in mind

## Setup

### Accounts (All Free Tier)
1. **Claude** — [claude.ai](https://claude.ai). Test it: ask Claude to explain a SQL window function or write a simple Python ETL script.
2. **GitHub** — [github.com](https://github.com). If new to Git, complete [GitHub Skills intro](https://skills.github.com/).
3. **Google Cloud Platform** — Follow these steps (see [full GCP setup guide](../../resources/gcp-setup-guide.md) if you get stuck):
   1. Go to [cloud.google.com/free](https://cloud.google.com/free) and sign up
   2. Create a new project (name it something like `learn-ai-pipeline`)
   3. Enable the BigQuery API: search "BigQuery API" in the console search bar, click Enable
   4. Set a budget alert: Billing > Budgets & Alerts > Create Budget > set to $10
   5. Install the gcloud CLI: [cloud.google.com/sdk/docs/install](https://cloud.google.com/sdk/docs/install)
   6. Authenticate: run `gcloud auth login` then `gcloud config set project YOUR_PROJECT_ID`
   7. Verify: run `bq ls` — you should see an empty list (no error)
4. **Terraform** — Terraform lets you define cloud infrastructure (buckets, databases, permissions) as code files instead of clicking through the GCP console. You'll use it in Session 3. [Install Terraform CLI](https://developer.hashicorp.com/terraform/install). Verify: `terraform --version`. If installation fails, don't worry — revisit this before Session 3.
5. **Anthropic API** — You'll use the Claude API in Session 4 for AI-powered monitoring.
   1. Sign up at [console.anthropic.com](https://console.anthropic.com)
   2. Create an API key (save it — you won't see it again)
   3. `pip install anthropic`
   4. Test it:
      ```python
      import anthropic
      client = anthropic.Anthropic()  # uses ANTHROPIC_API_KEY env var
      message = client.messages.create(
          model="claude-sonnet-4-20250514",
          max_tokens=100,
          messages=[{"role": "user", "content": "Say hello in one sentence."}]
      )
      print(message.content[0].text)
      ```
   5. Set your key: `export ANTHROPIC_API_KEY=sk-ant-...` (add to your shell profile)

   Cost note: The API charges per token. Expect to spend $2-5 total for this entire program. See the [Claude API Quickstart](../../resources/claude-api-quickstart.md) for details.

### Local Environment
- Python 3.9+ installed
- A code editor (VS Code recommended, Cursor if you want built-in AI)
- Terminal/shell access
- `pip install dbt-bigquery` (optional — for experienced users only, not required for this track. See [dbt Further Learning](../../resources/dbt-further-learning.md))

### Quick Setup (Optional)

If you prefer a one-command setup, run this from your capstone repo:
```bash
bash setup.sh
```
It creates a virtualenv, installs dependencies, prompts for your env vars, and runs the preflight check. See [setup.sh](../../setup.sh).

### Verify Everything Works

Run the preflight check to verify your setup automatically:
```bash
bash ../../resources/session0-preflight.sh
```

Or check manually:
- [ ] `python --version` returns 3.9+
- [ ] `terraform --version` returns a version
- [ ] `gcloud auth login` succeeds (install gcloud CLI if needed)
- [ ] Can access BigQuery in GCP console
- [ ] Can access Claude and get a response
- [ ] GitHub repo created for your capstone project

## Git Quickstart

If you're not comfortable with Git, run through this quick workflow now:

1. **Clone your repo:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/YOUR_CAPSTONE_REPO.git
   cd YOUR_CAPSTONE_REPO
   ```

2. **Make a change:** Create a file called `README.md` with your project idea (one paragraph is fine)

3. **Commit and push:**
   ```bash
   git add README.md
   git commit -m "Add initial README"
   git push origin main
   ```

4. **Verify:** Go to your repo on GitHub.com and confirm the file appears

If any step fails, check the [GitHub Skills intro](https://skills.github.com/) or ask in the community space.

## Baseline Challenge

### The Task
We've provided a sample dataset: [`examples/sample_sales.csv`](../../examples/sample_sales.csv) — 50 rows of sales data with some intentional data quality issues.

Build a pipeline that:
1. **Read** the CSV into a pandas DataFrame (or plain Python)
2. **Clean** the data:
   - Standardize the `region` column (mixed casing: "EAST", "east", "East" should all become "East")
   - Handle missing `cost` values (fill with 0 or the column median)
   - Remove or flag rows where `revenue` is 0
3. **Transform:** Add a `profit_margin` column: `(revenue - cost) / revenue`
4. **Aggregate:** Group by `region` and calculate total revenue, average profit margin, and row count
5. **Output:** Write the cleaned data and the summary to new CSV files

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

You'll build a real data pipeline over the next 6 sessions. Pick a project now — you can always adjust later.

### Choose Your Capstone Project

Pick one of these four vetted projects. Each uses a free, stable data source and fits within GCP free tier. See the [capstone guidelines](../capstone/guidelines.md) for full details on each project.

| Option | Data Source | What You'll Build |
|--------|-----------|-------------------|
| **Earthquake Monitor** | USGS Earthquake API (free, no key needed) | Ingest real-time earthquake events → geographic enrichment → impact classification → alert on significant events |
| **NYC 311 Complaint Analyzer** | NYC Open Data SODA API (free app token) | Ingest service requests → classify complaints → geographic aggregation → monitor for volume spikes |
| **GitHub Activity Tracker** | GitHub Events API (free with personal token) | Ingest repo events → classify by activity type → trend analysis → detect unusual patterns |
| **Weather Analytics** | Open-Meteo API (free, no key needed) | Ingest forecast + historical weather → daily aggregation → forecast accuracy tracking → extreme weather alerts |

See [Data Sources](../../resources/data-sources.md) for API endpoints, sample responses, and starter code.

## Intake Form
1. Your name and current role
2. DE experience level (1-5)
3. Tools you currently use (SQL, Python, Terraform, dbt, cloud platforms)
4. What capstone project are you considering?
5. Biggest challenge in your current data workflow?

---

**Next:** [Session 1 — Foundations: AI for Data Engineers](../session-01-foundations/)
