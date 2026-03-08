# Checkpoints

If you fall behind during the program, these checkpoints give you a working starting point. Copy the relevant examples into your capstone repo, customize them with your own data source, and keep going.

These are an **express lane, not a backup plan**. Every participant's capstone should be different — use checkpoints as a foundation, not a finished product.

## Available Checkpoints

### Session 2 Checkpoint — Ingestion + Transformation
**Source:** [`examples/starter-pipeline/`](../examples/starter-pipeline/)

What's included:
- Working Python ingestion script (OpenWeather API + sample data fallback)
- Three transformation functions with pandas
- Basic pytest tests
- `run_pipeline.py` orchestrator

How to use:
1. Copy the `starter-pipeline/` directory into your capstone repo
2. Run `pip install -r requirements.txt`
3. Run `python run_pipeline.py` (works offline with sample data)
4. Swap the data source or add your own transformations

### Session 3 Checkpoint — Pipeline + Infrastructure
**Source:** [`examples/starter-pipeline/`](../examples/starter-pipeline/) + [`examples/safe-terraform/`](../examples/safe-terraform/)

Everything from Session 2, plus:
- Terraform configs for GCS bucket + BigQuery dataset + service account
- Free-tier resources only
- `terraform.tfvars.example` ready to customize

How to use:
1. Copy both `starter-pipeline/` and `safe-terraform/` into your capstone repo
2. Copy `terraform.tfvars.example` to `terraform.tfvars`, add your project ID
3. Run `terraform init && terraform plan`
4. Run `terraform apply` when ready

### Session 4 Checkpoint — Pipeline + Infra + Agent Monitoring
**Source:** Everything from Session 3, plus [`examples/starter-agent/`](../examples/starter-agent/)

What's included:
- Data quality check tools (row count, null %, freshness, schema drift) in Anthropic tool-use format
- Agentic loop — Claude decides which tools to call and produces an assessment
- Alert and fix actions with dry_run safety
- Offline fallback for testing without an API key
- Sample data (same weather records as starter-monitor)

How to use:
1. Start from your Session 3 checkpoint (or copy the examples if you haven't yet)
2. Copy `starter-agent/` into your capstone repo
3. Run `python run_agent.py --offline` to verify checks work without an API key
4. Set `ANTHROPIC_API_KEY` and run `python run_agent.py --verbose` to see the agent in action
5. Customize the tools in `tools.py` for your pipeline's data
6. Add new tools to `TOOL_DEFINITIONS` — Claude will discover and use them automatically

**Simpler alternative:** [`examples/starter-monitor/`](../examples/starter-monitor/) still works for capstone — it uses Claude as a one-shot classifier rather than an autonomous agent. Use it if you want a simpler starting point.

## Tips
- **Don't just copy and present** — customize the pipeline with your own data, transformations, or monitoring rules
- **Read the code** — understanding the checkpoint is part of the learning
- **Ask for help** — share in the community space if you're stuck customizing
