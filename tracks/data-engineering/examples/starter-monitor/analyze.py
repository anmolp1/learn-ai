"""
Claude API wrapper for classifying data quality check results.

Usage:
    from analyze import classify_results
    analysis = classify_results(check_results)

Requires ANTHROPIC_API_KEY environment variable.
"""

import json
import os


def classify_results(check_results: list[dict]) -> str:
    """
    Send check results to Claude for classification and recommendations.

    Returns a structured analysis string with severity assessment,
    likely root causes, and recommended actions.
    """
    import anthropic

    client = anthropic.Anthropic()

    prompt = f"""You are a data engineering assistant. Analyze these data quality check results
and provide a brief assessment.

Check results:
{json.dumps(check_results, indent=2)}

For each failing check, provide:
1. Severity (critical / warning / info)
2. Likely root cause (1 sentence)
3. Recommended action (1 sentence)

End with an overall summary: is this pipeline healthy, degraded, or broken?
Keep the response concise — this will be used in automated alerts."""

    message = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}],
    )
    return message.content[0].text


def classify_results_offline(check_results: list[dict]) -> str:
    """
    Offline fallback — generates a simple rule-based analysis
    without calling the Claude API.
    """
    failed = [r for r in check_results if not r["passed"]]
    if not failed:
        return "All checks passed. Pipeline is healthy."

    lines = ["Offline Analysis (no API key)", "-" * 30]
    critical = [r for r in failed if r.get("severity") == "critical"]
    warnings = [r for r in failed if r.get("severity") == "warning"]

    if critical:
        lines.append(f"CRITICAL: {len(critical)} critical issue(s) found")
        for r in critical:
            lines.append(f"  - {r['check']}: {r['detail']}")

    if warnings:
        lines.append(f"WARNING: {len(warnings)} warning(s) found")
        for r in warnings:
            lines.append(f"  - {r['check']}: {r['detail']}")

    status = "BROKEN" if critical else "DEGRADED"
    lines.append(f"\nOverall: Pipeline is {status}.")
    return "\n".join(lines)


if __name__ == "__main__":
    # Quick test with sample results
    sample_results = [
        {"check": "row_count", "passed": True, "severity": "info", "detail": "Expected >= 1 rows, got 5"},
        {"check": "null_pct_city", "passed": False, "severity": "warning", "detail": "Column 'city' null rate: 20.0% (threshold: 10.0%)"},
    ]

    if os.environ.get("ANTHROPIC_API_KEY"):
        print(classify_results(sample_results))
    else:
        print(classify_results_offline(sample_results))
