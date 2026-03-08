"""
Data quality check tools for the monitoring agent.

Each function runs a specific check and returns structured results.
TOOL_DEFINITIONS exports them in Anthropic tool-use format so Claude
can discover and call them during an agentic loop.

Reuses the same checks from starter-monitor/monitor.py (row_count,
null_pct, freshness) and adds schema_drift, send_alert, and apply_fix.
"""

import json
from datetime import datetime, timezone


# ---------------------------------------------------------------------------
# Tool functions — each takes explicit parameters and returns a dict result
# ---------------------------------------------------------------------------

def check_row_count(data: list[dict], min_expected: int = 1) -> dict:
    """Check that the dataset has at least min_expected rows."""
    actual = len(data)
    passed = actual >= min_expected
    return {
        "check": "row_count",
        "passed": passed,
        "severity": "critical" if not passed else "info",
        "detail": f"Expected >= {min_expected} rows, got {actual}",
    }


def check_null_percentage(data: list[dict], column: str, max_null_pct: float = 0.1) -> dict:
    """Check that null/missing values in a column don't exceed a threshold."""
    total = len(data)
    if total == 0:
        return {
            "check": f"null_pct_{column}",
            "passed": False,
            "severity": "critical",
            "detail": "No data to check",
        }
    nulls = sum(1 for row in data if row.get(column) is None or row.get(column) == "")
    null_pct = nulls / total
    passed = null_pct <= max_null_pct
    return {
        "check": f"null_pct_{column}",
        "passed": passed,
        "severity": "warning" if not passed else "info",
        "detail": f"Column '{column}' null rate: {null_pct:.1%} (threshold: {max_null_pct:.1%})",
    }


def check_freshness(data: list[dict], timestamp_column: str = "timestamp", max_age_hours: int = 24) -> dict:
    """Check that the most recent record is within max_age_hours."""
    timestamps = [row[timestamp_column] for row in data if row.get(timestamp_column)]
    if not timestamps:
        return {
            "check": "freshness",
            "passed": False,
            "severity": "critical",
            "detail": f"No values found in column '{timestamp_column}'",
        }
    latest = max(timestamps)
    if isinstance(latest, str):
        latest_dt = datetime.fromisoformat(latest.replace("Z", "+00:00"))
    else:
        latest_dt = latest
    now = datetime.now(timezone.utc)
    age_hours = (now - latest_dt).total_seconds() / 3600
    passed = age_hours <= max_age_hours
    return {
        "check": "freshness",
        "passed": passed,
        "severity": "warning" if not passed else "info",
        "detail": f"Latest record is {age_hours:.1f} hours old (threshold: {max_age_hours}h)",
    }


def check_schema_drift(data: list[dict], expected_columns: list[str]) -> dict:
    """Compare actual columns in the data against an expected set."""
    if not data:
        return {
            "check": "schema_drift",
            "passed": False,
            "severity": "critical",
            "detail": "No data to check",
        }
    actual_columns = set(data[0].keys())
    expected_set = set(expected_columns)
    missing = expected_set - actual_columns
    extra = actual_columns - expected_set
    passed = not missing  # extra columns are OK, missing ones are not
    detail_parts = []
    if missing:
        detail_parts.append(f"missing: {sorted(missing)}")
    if extra:
        detail_parts.append(f"unexpected: {sorted(extra)}")
    if not detail_parts:
        detail_parts.append("schema matches expected columns")
    return {
        "check": "schema_drift",
        "passed": passed,
        "severity": "warning" if not passed else "info",
        "detail": "; ".join(detail_parts),
    }


def send_alert(message: str, severity: str = "warning") -> dict:
    """Send an alert (prints to stdout — swap for Slack/email in production)."""
    alert_text = f"[ALERT][{severity.upper()}] {message}"
    print(alert_text)
    return {"sent": True, "alert": alert_text}


def apply_fix(fix_type: str, params: dict | None = None, dry_run: bool = True) -> dict:
    """
    Apply a remediation action. Defaults to dry_run=True so nothing
    actually changes — the agent must explicitly request dry_run=False,
    giving the human a chance to review.
    """
    description = f"Fix '{fix_type}' with params {params or {}}"
    if dry_run:
        print(f"[DRY RUN] Would apply: {description}")
        return {"applied": False, "dry_run": True, "description": description}
    else:
        print(f"[APPLIED] {description}")
        return {"applied": True, "dry_run": False, "description": description}


# ---------------------------------------------------------------------------
# TOOL_DEFINITIONS — Anthropic tool-use format
# Claude reads these to understand what tools are available and how to call them.
# See: https://docs.anthropic.com/en/docs/build-with-claude/tool-use
# ---------------------------------------------------------------------------

TOOL_DEFINITIONS = [
    {
        "name": "check_row_count",
        "description": "Check that the dataset has at least a minimum number of rows.",
        "input_schema": {
            "type": "object",
            "properties": {
                "min_expected": {
                    "type": "integer",
                    "description": "Minimum expected row count (default: 1)",
                },
            },
            "required": [],
        },
    },
    {
        "name": "check_null_percentage",
        "description": "Check that null/missing values in a specific column do not exceed a threshold.",
        "input_schema": {
            "type": "object",
            "properties": {
                "column": {
                    "type": "string",
                    "description": "The column name to check for nulls",
                },
                "max_null_pct": {
                    "type": "number",
                    "description": "Maximum allowed null fraction, e.g. 0.1 for 10% (default: 0.1)",
                },
            },
            "required": ["column"],
        },
    },
    {
        "name": "check_freshness",
        "description": "Check that the most recent record is within a maximum age.",
        "input_schema": {
            "type": "object",
            "properties": {
                "timestamp_column": {
                    "type": "string",
                    "description": "Name of the timestamp column (default: 'timestamp')",
                },
                "max_age_hours": {
                    "type": "integer",
                    "description": "Maximum allowed age in hours (default: 24)",
                },
            },
            "required": [],
        },
    },
    {
        "name": "check_schema_drift",
        "description": "Compare actual columns in the data against an expected list of column names.",
        "input_schema": {
            "type": "object",
            "properties": {
                "expected_columns": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "List of expected column names",
                },
            },
            "required": ["expected_columns"],
        },
    },
    {
        "name": "send_alert",
        "description": "Send an alert notification about a data quality issue.",
        "input_schema": {
            "type": "object",
            "properties": {
                "message": {
                    "type": "string",
                    "description": "Alert message text",
                },
                "severity": {
                    "type": "string",
                    "enum": ["info", "warning", "critical"],
                    "description": "Alert severity level (default: 'warning')",
                },
            },
            "required": ["message"],
        },
    },
    {
        "name": "apply_fix",
        "description": "Apply a remediation action to fix a data quality issue. Uses dry_run=True by default — set dry_run=False only after human approval.",
        "input_schema": {
            "type": "object",
            "properties": {
                "fix_type": {
                    "type": "string",
                    "description": "Type of fix to apply (e.g., 'rerun_ingestion', 'backfill_nulls', 'drop_duplicates')",
                },
                "params": {
                    "type": "object",
                    "description": "Parameters for the fix (varies by fix type)",
                },
                "dry_run": {
                    "type": "boolean",
                    "description": "If true, only report what would happen without applying (default: true)",
                },
            },
            "required": ["fix_type"],
        },
    },
]


# ---------------------------------------------------------------------------
# execute_tool — dispatcher that maps tool names to functions
# The agentic loop in agent.py calls this with the name and input that
# Claude returns in a tool_use content block.
# ---------------------------------------------------------------------------

# We keep a reference to the data globally so tool functions can access it.
# In agent.py, call set_tool_data() before starting the loop.
_tool_data: list[dict] = []


def set_tool_data(data: list[dict]):
    """Set the dataset that check tools will operate on."""
    global _tool_data
    _tool_data = data


def execute_tool(name: str, tool_input: dict) -> str:
    """
    Dispatch a tool call by name. Returns the result as a JSON string
    (tool_result content must be a string in the Anthropic API).
    """
    if name == "check_row_count":
        result = check_row_count(_tool_data, **tool_input)
    elif name == "check_null_percentage":
        result = check_null_percentage(_tool_data, **tool_input)
    elif name == "check_freshness":
        result = check_freshness(_tool_data, **tool_input)
    elif name == "check_schema_drift":
        result = check_schema_drift(_tool_data, **tool_input)
    elif name == "send_alert":
        result = send_alert(**tool_input)
    elif name == "apply_fix":
        result = apply_fix(**tool_input)
    else:
        result = {"error": f"Unknown tool: {name}"}

    return json.dumps(result)
