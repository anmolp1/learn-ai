"""
Orchestrator — runs data quality checks and sends results to Claude for analysis.

Usage:
    python run_monitor.py              # Full run (requires ANTHROPIC_API_KEY)
    python run_monitor.py --offline    # Run checks only, skip Claude analysis
    python run_monitor.py --file data.json  # Use custom data file
"""

import argparse
import json
import os
import sys

from monitor import DataQualityChecker, load_sample_data
from analyze import classify_results, classify_results_offline


def main():
    parser = argparse.ArgumentParser(description="Run pipeline monitor")
    parser.add_argument("--offline", action="store_true", help="Skip Claude API call")
    parser.add_argument("--file", help="Path to JSON data file (default: sample data)")
    args = parser.parse_args()

    # Load data
    if args.file:
        with open(args.file) as f:
            data = json.load(f)
        print(f"Loaded {len(data)} records from {args.file}")
    else:
        data = load_sample_data()
        print(f"Loaded {len(data)} records from sample data")

    # Run checks
    checker = DataQualityChecker(data)
    results = checker.run_all(
        columns=["temperature", "city"],
        timestamp_column="timestamp",
    )
    print("\n" + checker.summary())

    # Analyze
    failed = [r for r in results if not r["passed"]]
    if not failed:
        print("\nAll checks passed — no analysis needed.")
        return

    print("\n--- AI Analysis ---\n")

    if args.offline or not os.environ.get("ANTHROPIC_API_KEY"):
        if not args.offline:
            print("(No ANTHROPIC_API_KEY found — using offline analysis)\n")
        print(classify_results_offline(results))
    else:
        print(classify_results(results))


if __name__ == "__main__":
    main()
