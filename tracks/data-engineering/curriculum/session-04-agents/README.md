# Session 4: Agents — Tool Use, Agentic Loops, and MCP

**Format:** 90 min live + async challenge
**Goal:** Build a monitoring agent that uses Claude's tool-use API to autonomously check data quality

## Session Plan

### Concept (15 min): Scripts vs Agents

Most data pipelines break silently. Data arrives late, schemas drift, quality degrades — and nobody notices until a stakeholder complains. This session is about building agents that detect and respond to these problems.

The progression:
1. **Manual monitoring** — You check dashboards, run queries, hope nothing's broken
2. **Rule-based alerts** — Thresholds trigger notifications (row count < X, latency > Y)
3. **AI-powered monitoring** — AI classifies issues and suggests root causes (what we built in `starter-monitor/`)
4. **Agentic automation** — AI decides which checks to run, analyzes results, and takes action in a loop (what we build today)

**The key difference:** A script calls Claude once and you decide what to do. An agent gives Claude tools and lets it decide what to do — calling tools, reading results, calling more tools — until it has enough information to act.

**MCP (2-3 min):** Model Context Protocol is an open standard for connecting AI to external data sources. Instead of writing Python wrapper functions for every database and API, you configure an MCP server and Claude can query BigQuery, SQLite, or Airflow directly. We won't build with MCP today, but the [MCP Setup Guide](../../resources/mcp-setup-guide.md) is there for async exploration. The tool-use pattern you learn today is the same pattern MCP uses under the hood.

**Framework landscape (1 min):** LangGraph, CrewAI, and the OpenAI Agents SDK all implement similar patterns. We use the Anthropic SDK because you already have API keys and the agentic loop is ~30 lines of Python — no new packages. The concepts (tool definitions, agentic loops, human-in-the-loop) transfer to any framework.

### Demo (35 min): Build a Monitoring Agent

**Step 1 — Define Tools (10 min)**

Walk through [`starter-agent/tools.py`](../../examples/starter-agent/tools.py):
- Tool functions: `check_row_count`, `check_null_percentage`, `check_freshness`, `check_schema_drift`
- Action tools: `send_alert`, `apply_fix` (with `dry_run=True` default)
- `TOOL_DEFINITIONS` list — the Anthropic tool-use format (`name`, `description`, `input_schema`)
- `execute_tool()` dispatcher

Compare to `starter-monitor/monitor.py` — same checks, now wrapped as callable tools that Claude can discover and invoke.

**Step 2 — The Agentic Loop (15 min)**

Walk through [`starter-agent/agent.py`](../../examples/starter-agent/agent.py):
1. Send initial message to Claude with system prompt + tool definitions
2. **While loop:** if `stop_reason == "tool_use"`, extract the tool call, execute it via `execute_tool()`, send the result back
3. Repeat until `stop_reason == "end_turn"` — Claude has its final assessment

Run it live:
```bash
ANTHROPIC_API_KEY=your-key python run_agent.py --verbose
```

Participants see Claude choosing which tools to call, reading results, and deciding what to do next in real time.

**Step 3 — Human-in-the-Loop (10 min)**

Not everything should be automated. Discuss guardrails:
- **Auto-approve list:** Read-only checks (`check_row_count`, `check_null_percentage`) are safe to run without asking
- **Require confirmation:** Actions with side effects (`apply_fix` with `dry_run=False`, `send_alert` with severity "critical") should pause for human approval
- **The `dry_run` pattern:** `apply_fix` defaults to `dry_run=True` — Claude can propose fixes, but nothing happens until a human approves

Show how to add an approval gate in the loop: before executing `apply_fix` with `dry_run=False`, prompt the user for confirmation.

### Practice (25 min)

> **Choose your path based on your experience level:**
>
> **If this is new to you** — Copy [`starter-agent/`](../../examples/starter-agent/) into your capstone repo. Run it with sample data (`python run_agent.py --offline`), then with your API key (`python run_agent.py --verbose`). Customize the tool checks in `tools.py` for your pipeline's data.
>
> **If you're experienced** — Build your agent from scratch. Define your own tools (query BigQuery, check Airflow DAG status, validate dbt model output). Implement the agentic loop. Try integrating an MCP server using the [MCP Setup Guide](../../resources/mcp-setup-guide.md).

Participants add an agent to their capstone:
- At minimum: 3 data quality check tools + agentic loop
- Stretch: Custom tools, MCP integration, approval gates
- Push to GitHub

### Debrief (15 min)
- What did Claude choose to do that surprised you?
- What would you trust an agent to do automatically?
- Where do you want human oversight?
- What tools would you give an agent for YOUR pipeline?

## Async Challenge

### Task
Add an AI agent to your capstone pipeline:

1. **Tool definitions:** Define at least 3 quality check tools in Anthropic tool-use format (name, description, input_schema)
2. **Agentic loop:** Implement the while loop — agent runs checks, analyzes results, and produces an assessment
3. **Human-in-the-loop:** At least one tool requires approval before execution (e.g., `apply_fix` with `dry_run=False`)
4. **Documentation:** Add an "Agent Monitoring" section to your capstone README explaining what the agent does and how to run it

### Stretch Goals
- Integrate an MCP server (BigQuery or SQLite) — see [MCP Setup Guide](../../resources/mcp-setup-guide.md)
- Add auto-remediation for one failure type (with dry_run safety)
- Schedule agent runs (cron, Cloud Scheduler, or Airflow)
- Add more tools: query BigQuery for investigation, check Airflow DAG status, validate dbt test results

Push to GitHub, share in community with `#de-session4`.

**Cost Check:** Open your [GCP Billing Dashboard](https://console.cloud.google.com/billing) and note your current spend in your learning journal. A typical agent run with 3-5 tool calls costs ~$0.02-0.05 with Claude Sonnet.

> **Falling behind?** Two options:
> - **Full agent pattern:** Copy [`starter-agent/`](../../examples/starter-agent/) — gives you tools, agentic loop, and offline fallback
> - **Simpler alternative:** Copy [`starter-monitor/`](../../examples/starter-monitor/) — one API call for classification, no loop needed
>
> Both work for your capstone. See [Checkpoints](../../resources/checkpoints.md) to catch up on pipeline and infrastructure too.

## Resources
- [Anthropic Tool Use Documentation](https://docs.anthropic.com/en/docs/build-with-claude/tool-use)
- [Claude API Quickstart](../../resources/claude-api-quickstart.md) (includes tool-use section)
- [MCP Setup Guide](../../resources/mcp-setup-guide.md) (BigQuery, SQLite, and more)
- [BigQuery Information Schema](https://cloud.google.com/bigquery/docs/information-schema-intro) (useful for schema drift detection)
- [Great Expectations](https://greatexpectations.io/) (data quality framework, for reference)
- [Soda](https://www.soda.io/) (another data quality tool, for reference)

---

**Previous:** [Session 3 — Infrastructure-as-Code](../session-03-iac/)
**Next:** [Session 5 — Quality: Testing, Security, and Reliability](../session-05-quality/)
