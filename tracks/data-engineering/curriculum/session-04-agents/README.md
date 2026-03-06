# Session 4: Agents — Monitoring, Alerts, and Automation

**Format:** 90 min live + async challenge
**Goal:** Build AI-powered monitoring and automation for your data pipeline

## Session Plan

### Concept (15 min): From Pipelines to Self-Healing Systems

Most data pipelines break silently. Data arrives late, schemas drift, quality degrades — and nobody notices until a stakeholder complains. This session is about using AI agents to close that gap.

The progression:
1. **Manual monitoring** — You check dashboards, run queries, hope nothing's broken
2. **Rule-based alerts** — Thresholds trigger notifications (row count < X, latency > Y)
3. **AI-powered monitoring** — AI detects anomalies, classifies issues, suggests root causes
4. **Agentic automation** — AI detects the issue AND takes corrective action (with human approval)

Today we go from 1/2 to 3/4.

### Demo (35 min): Build a Pipeline Monitor

**Build a monitoring agent live.** Components:

**Step 1 — Data Quality Checks (10 min)**
Use Claude to generate a Python module that runs quality checks:
- Row count validation (expected vs. actual, with tolerance)
- Schema drift detection (new columns, type changes, missing fields)
- Value distribution checks (nulls, outliers, unexpected categories)
- Freshness checks (is the data current?)

```
Prompt: Write a Python class called DataQualityChecker that:
- Takes a BigQuery client and a table reference
- Runs these checks: [list checks]
- Returns a structured report with severity levels (critical, warning, info)
- Logs all results
```

**Step 2 — AI-Powered Anomaly Classification (10 min)**
Use Claude Code or Claude API to analyze check results:
- Feed quality check output to Claude
- Ask it to classify the severity and likely root cause
- Generate a human-readable summary with recommended actions

Show how to build a simple function that calls the Claude API with check results and gets back structured analysis.

**Step 3 — Alert and Act (10 min)**
Wire it together:
- Quality checks run on a schedule (cron, Cloud Scheduler, or Airflow)
- Results go to Claude for analysis
- Critical issues trigger Slack/email alerts with AI-generated context
- Optional: auto-remediation for known issue types (e.g., re-run a failed load)

**Step 4 — Human-in-the-Loop (5 min)**
Discuss guardrails:
- What should the agent do automatically vs. ask for approval?
- How to log agent actions for audit
- When to page a human

### Practice (25 min)

> **Choose your path based on your experience level:**
>
> **If this is new to you** — Start from the [starter monitor](../../examples/starter-monitor/). Copy it into your capstone repo, run it with sample data, then adapt the checks to match your pipeline's data.
>
> **If you're experienced** — Build your monitoring from scratch. Add schema drift detection, custom anomaly thresholds, or multi-table checks. Use the Claude API directly for classification.

Participants add monitoring to their capstone:
- At minimum: 3 data quality checks + alerting
- Stretch: AI-powered anomaly classification
- Push to GitHub

### Debrief (15 min)
- What would you trust an agent to do automatically?
- Where do you want human oversight?

## Async Challenge

### Task
Add monitoring and automation to your capstone pipeline:

1. **Quality checks:** At least 3 automated checks (freshness, schema, values)
2. **AI analysis:** Feed check results to Claude API for classification and recommendations
3. **Alerting:** When checks fail, generate an actionable alert (even if it's just a log/print for now)
4. **Documentation:** Add a "Monitoring" section to your README

### Stretch Goals
- Schedule checks to run automatically
- Add auto-remediation for one failure type
- Build a simple dashboard or summary report

Push to GitHub, share in community with `#de-session4`.

**Cost Check:** Open your [GCP Billing Dashboard](https://console.cloud.google.com/billing) and note your current spend in your learning journal. Compare with last session.

> **Falling behind?** Copy the [starter monitor](../../examples/starter-monitor/) into your capstone repo — it gives you working quality checks and a Claude API wrapper out of the box. See [Checkpoints](../../resources/checkpoints.md) to catch up on pipeline and infrastructure too.

## Resources
- [Claude API Documentation](https://docs.anthropic.com/en/api/getting-started)
- [BigQuery Information Schema](https://cloud.google.com/bigquery/docs/information-schema-intro) (useful for schema drift detection)
- [Great Expectations](https://greatexpectations.io/) (data quality framework, for reference)
- [Soda](https://www.soda.io/) (another data quality tool, for reference)

---

**Previous:** [Session 3 — Infrastructure-as-Code](../session-03-iac/)
**Next:** [Session 5 — Quality: Testing, Security, and Reliability](../session-05-quality/)
