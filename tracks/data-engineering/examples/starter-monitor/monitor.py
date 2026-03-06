"""
Data quality checker — runs basic checks against pipeline output.

Usage:
    python monitor.py                          # Run checks on sample data
    python monitor.py --file path/to/data.json # Run checks on your own data
"""

import json
import argparse
from datetime import datetime, timezone
from pathlib import Path


class DataQualityChecker:
    """Runs data quality checks and returns structured results."""

    def __init__(self, data: list[dict]):
        self.data = data
        self.results = []

    def check_row_count(self, min_expected: int = 1) -> dict:
        """Check that the dataset has at least min_expected rows."""
        actual = len(self.data)
        passed = actual >= min_expected
        result = {
            "check": "row_count",
            "passed": passed,
            "severity": "critical" if not passed else "info",
            "detail": f"Expected >= {min_expected} rows, got {actual}",
        }
        self.results.append(result)
        return result

    def check_null_percentage(self, column: str, max_null_pct: float = 0.1) -> dict:
        """Check that null/missing values in a column don't exceed a threshold."""
        total = len(self.data)
        if total == 0:
            result = {
                "check": f"null_pct_{column}",
                "passed": False,
                "severity": "critical",
                "detail": "No data to check",
            }
            self.results.append(result)
            return result

        nulls = sum(1 for row in self.data if row.get(column) is None or row.get(column) == "")
        null_pct = nulls / total
        passed = null_pct <= max_null_pct
        result = {
            "check": f"null_pct_{column}",
            "passed": passed,
            "severity": "warning" if not passed else "info",
            "detail": f"Column '{column}' null rate: {null_pct:.1%} (threshold: {max_null_pct:.1%})",
        }
        self.results.append(result)
        return result

    def check_freshness(self, timestamp_column: str, max_age_hours: int = 24) -> dict:
        """Check that the most recent record is within max_age_hours."""
        timestamps = [
            row[timestamp_column]
            for row in self.data
            if row.get(timestamp_column)
        ]
        if not timestamps:
            result = {
                "check": "freshness",
                "passed": False,
                "severity": "critical",
                "detail": f"No values found in column '{timestamp_column}'",
            }
            self.results.append(result)
            return result

        latest = max(timestamps)
        # Handle ISO format strings
        if isinstance(latest, str):
            latest_dt = datetime.fromisoformat(latest.replace("Z", "+00:00"))
        else:
            latest_dt = latest

        now = datetime.now(timezone.utc)
        age_hours = (now - latest_dt).total_seconds() / 3600
        passed = age_hours <= max_age_hours
        result = {
            "check": "freshness",
            "passed": passed,
            "severity": "warning" if not passed else "info",
            "detail": f"Latest record is {age_hours:.1f} hours old (threshold: {max_age_hours}h)",
        }
        self.results.append(result)
        return result

    def run_all(self, columns: list[str] | None = None, timestamp_column: str = "timestamp") -> list[dict]:
        """Run all checks and return results."""
        self.check_row_count()
        for col in (columns or []):
            self.check_null_percentage(col)
        self.check_freshness(timestamp_column)
        return self.results

    def summary(self) -> str:
        """Return a human-readable summary of check results."""
        lines = ["Data Quality Check Results", "=" * 40]
        for r in self.results:
            status = "PASS" if r["passed"] else "FAIL"
            lines.append(f"[{status}] {r['check']}: {r['detail']}")
        failed = [r for r in self.results if not r["passed"]]
        lines.append(f"\n{len(self.results)} checks run, {len(failed)} failed.")
        return "\n".join(lines)


def load_sample_data() -> list[dict]:
    """Load sample data from the sample_data directory."""
    sample_path = Path(__file__).parent / "sample_data" / "check_results.json"
    with open(sample_path) as f:
        return json.load(f)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run data quality checks")
    parser.add_argument("--file", help="Path to JSON data file (default: sample data)")
    args = parser.parse_args()

    if args.file:
        with open(args.file) as f:
            data = json.load(f)
    else:
        data = load_sample_data()

    checker = DataQualityChecker(data)
    checker.run_all(columns=["temperature", "city"], timestamp_column="timestamp")
    print(checker.summary())
