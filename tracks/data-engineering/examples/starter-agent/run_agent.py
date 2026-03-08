"""
Entry point for the monitoring agent.

Usage:
    python run_agent.py                    # Run agent with Claude API
    python run_agent.py --verbose          # Show each tool call as it happens
    python run_agent.py --offline          # Run checks without API key
    python run_agent.py --file data.json   # Use custom data file
"""

import argparse
import json
import os
from pathlib import Path


def load_sample_data() -> list[dict]:
    """Load sample data from the sample_data directory."""
    sample_path = Path(__file__).parent / "sample_data" / "check_results.json"
    with open(sample_path) as f:
        return json.load(f)


def main():
    parser = argparse.ArgumentParser(description="Run the data quality monitoring agent")
    parser.add_argument("--offline", action="store_true", help="Skip Claude API, use rule-based analysis")
    parser.add_argument("--file", help="Path to JSON data file (default: sample data)")
    parser.add_argument("--verbose", action="store_true", help="Print each tool call as it happens")
    args = parser.parse_args()

    # Load data
    if args.file:
        with open(args.file) as f:
            data = json.load(f)
        print(f"Loaded {len(data)} records from {args.file}")
    else:
        data = load_sample_data()
        print(f"Loaded {len(data)} records from sample data")

    # Run agent
    if args.offline or not os.environ.get("ANTHROPIC_API_KEY"):
        if not args.offline:
            print("(No ANTHROPIC_API_KEY found — using offline mode)\n")
        from agent import run_agent_offline
        assessment = run_agent_offline(data)
    else:
        from agent import run_agent
        assessment = run_agent(data, verbose=args.verbose)

    print("\n--- Agent Assessment ---\n")
    print(assessment)


if __name__ == "__main__":
    main()
