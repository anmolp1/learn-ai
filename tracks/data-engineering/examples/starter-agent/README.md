# Starter Agent — Data Quality Monitoring with Tool Use

A monitoring agent that uses Claude's tool-use API to autonomously run data quality checks and produce an assessment. Unlike `starter-monitor/` (which calls Claude once for classification), this agent gives Claude tools and lets it decide which checks to run in a loop.

## What It Does

1. **`tools.py`** — Defines data quality check functions (row count, null %, freshness, schema drift) plus alert and fix actions. Exports them as `TOOL_DEFINITIONS` in Anthropic tool-use format.
2. **`agent.py`** — The agentic loop. Sends tools to Claude, executes whatever Claude calls, sends results back, repeats until Claude produces a final assessment.
3. **`run_agent.py`** — Entry point. Loads data, runs the agent (or offline fallback), prints results.

## Quick Start

```bash
pip install -r requirements.txt

# With API key — Claude decides which tools to call
ANTHROPIC_API_KEY=your-key python run_agent.py --verbose

# Without API key — runs all checks with rule-based analysis
python run_agent.py --offline
```

The `--verbose` flag prints each tool call as it happens, so you can see Claude's decision-making in real time.

## Offline Mode

Works without an API key using `sample_data/check_results.json`:

```bash
python run_agent.py --offline
```

This runs all checks sequentially and produces a rule-based summary — useful for testing your tool functions before adding the agentic loop.

## How to Customize

1. Copy this directory into your capstone repo
2. Edit `tools.py` to add checks for your pipeline's data (e.g., check specific columns, add BigQuery queries)
3. Add new tools to `TOOL_DEFINITIONS` — Claude will automatically discover and use them
4. Replace `sample_data/check_results.json` with your pipeline's output
5. Wire `run_agent.py` into your pipeline's post-load step

## Files

| File | Purpose |
|------|---------|
| `tools.py` | Tool functions + `TOOL_DEFINITIONS` + `execute_tool()` dispatcher |
| `agent.py` | Agentic loop (`run_agent`) + offline fallback (`run_agent_offline`) |
| `run_agent.py` | Entry point with CLI flags |
| `sample_data/check_results.json` | Sample weather data for testing |
| `requirements.txt` | Dependencies (just `anthropic`) |

## How This Differs from starter-monitor

| | starter-monitor | starter-agent |
|---|---|---|
| **API calls** | One call — sends results, gets analysis | Multiple calls — Claude decides which tools to use |
| **Control flow** | Script runs checks, then asks Claude | Claude drives the loop, calling tools as needed |
| **Pattern** | AI-assisted (human decides) | Agentic (AI decides, human approves) |
| **Complexity** | Simpler, good starting point | More realistic agent pattern |

Both are valid for your capstone — `starter-monitor` is the simpler option, `starter-agent` shows the full agent pattern.
