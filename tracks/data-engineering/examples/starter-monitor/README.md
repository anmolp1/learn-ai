# Starter Monitor

A minimal data quality monitoring example for Session 4. Use this as a starting point if you need a scaffold for adding monitoring to your capstone pipeline.

## What It Does

1. **`monitor.py`** — Runs data quality checks (row count, null percentage, freshness) against a results file
2. **`analyze.py`** — Sends check results to the Claude API for classification and recommended actions
3. **`run_monitor.py`** — Orchestrates: run checks, analyze with Claude, print a summary

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Run with sample data (no API key needed for checks only)
python monitor.py

# Run the full pipeline including Claude analysis (requires API key)
export ANTHROPIC_API_KEY=your-key-here
python run_monitor.py
```

## Offline Mode

The monitor works offline using `sample_data/check_results.json`. You can run `monitor.py` and `run_monitor.py --offline` without a Claude API key to test the check logic.

## How to Customize

1. Copy this directory into your capstone repo
2. Edit `monitor.py` to add checks relevant to your pipeline (schema drift, value ranges, etc.)
3. Replace `sample_data/check_results.json` with your own pipeline output
4. Wire `run_monitor.py` into your pipeline's post-load step

## Files

| File | Purpose |
|------|---------|
| `monitor.py` | Data quality checker class |
| `analyze.py` | Claude API wrapper for classifying check results |
| `run_monitor.py` | Orchestrator that runs checks and calls Claude |
| `sample_data/check_results.json` | Sample check output for offline testing |
| `requirements.txt` | Python dependencies |
