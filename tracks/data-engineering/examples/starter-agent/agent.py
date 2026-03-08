"""
The agentic loop — Claude decides which tools to call and keeps going
until it has enough information to produce a final assessment.

This is the core teaching file. Read the comments to understand how
an agent differs from a single API call.

Usage:
    from agent import run_agent, run_agent_offline
    assessment = run_agent(data, verbose=True)
"""

import json
import os

from tools import TOOL_DEFINITIONS, execute_tool, set_tool_data


# ---------------------------------------------------------------------------
# SYSTEM PROMPT — tells Claude its role and what tools are for
# ---------------------------------------------------------------------------

SYSTEM_PROMPT = """You are a data quality monitoring agent for a data pipeline.

You have access to tools that run quality checks on the pipeline's output data.
Your job is to:
1. Run the checks you think are relevant (row count, null percentage, freshness, schema drift)
2. Analyze the results
3. If there are issues, send alerts with appropriate severity
4. If you can suggest a fix, propose it using apply_fix with dry_run=True
5. Produce a final assessment: is this pipeline healthy, degraded, or broken?

The data has these columns: city, temperature, humidity, timestamp.

Be thorough but concise. Call tools one at a time or in sequence as needed.
When you have enough information, stop calling tools and give your final assessment."""


def run_agent(data: list[dict], verbose: bool = False) -> str:
    """
    Run the monitoring agent. Claude decides which tools to call.

    This function implements the agentic loop:
    1. Send a message to Claude with tool definitions
    2. If Claude wants to call a tool, execute it and send the result back
    3. Repeat until Claude produces a final text response

    Args:
        data: List of records to check (same format as check_results.json)
        verbose: If True, print each tool call as it happens

    Returns:
        Claude's final text assessment
    """
    import anthropic

    # Make the data available to tool functions
    set_tool_data(data)

    client = anthropic.Anthropic()

    # Step 1: Send the initial message with tool definitions.
    # Claude sees the tool definitions and decides what to do.
    messages = [
        {
            "role": "user",
            "content": (
                f"Here is the pipeline output data ({len(data)} records). "
                f"Run quality checks and give me an assessment.\n\n"
                f"Sample record: {json.dumps(data[0]) if data else '{}'}"
            ),
        }
    ]

    if verbose:
        print(f"Starting agent with {len(data)} records...")
        print(f"Tools available: {[t['name'] for t in TOOL_DEFINITIONS]}\n")

    # Step 2: The agentic loop.
    # Keep calling Claude until it stops asking for tools.
    while True:
        response = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=4096,
            system=SYSTEM_PROMPT,
            tools=TOOL_DEFINITIONS,
            messages=messages,
        )

        # Step 3: Check why Claude stopped generating.
        # "tool_use" means Claude wants to call a tool.
        # "end_turn" means Claude is done — it produced its final answer.
        if response.stop_reason == "end_turn":
            # Extract the final text from the response
            for block in response.content:
                if hasattr(block, "text"):
                    return block.text
            return "Agent finished without producing a text response."

        # Step 4: Claude wants to call one or more tools.
        # Extract each tool_use block, execute it, and build tool_result messages.
        tool_results = []
        for block in response.content:
            if block.type == "tool_use":
                tool_name = block.name
                tool_input = block.input

                if verbose:
                    print(f"  Tool call: {tool_name}({json.dumps(tool_input)})")

                # Execute the tool and get the result
                result = execute_tool(tool_name, tool_input)

                if verbose:
                    print(f"  Result:    {result}\n")

                tool_results.append(
                    {
                        "type": "tool_result",
                        "tool_use_id": block.id,
                        "content": result,
                    }
                )

        # Step 5: Send Claude's response and the tool results back.
        # Claude will see what the tools returned and decide what to do next —
        # call more tools, or produce its final answer.
        messages.append({"role": "assistant", "content": response.content})
        messages.append({"role": "user", "content": tool_results})


def run_agent_offline(data: list[dict]) -> str:
    """
    Offline fallback — runs all checks sequentially with rule-based analysis.
    Same pattern as starter-monitor/analyze.py:classify_results_offline.
    No API key required.
    """
    from tools import (
        check_row_count,
        check_null_percentage,
        check_freshness,
        check_schema_drift,
    )

    results = []
    results.append(check_row_count(data))
    results.append(check_null_percentage(data, column="temperature"))
    results.append(check_null_percentage(data, column="city"))
    results.append(check_freshness(data))
    results.append(check_schema_drift(data, expected_columns=["city", "temperature", "humidity", "timestamp"]))

    # Build summary
    failed = [r for r in results if not r["passed"]]
    lines = ["Offline Agent Analysis (no API key)", "=" * 40]

    for r in results:
        status = "PASS" if r["passed"] else "FAIL"
        lines.append(f"[{status}] {r['check']}: {r['detail']}")

    if not failed:
        lines.append("\nOverall: Pipeline is HEALTHY.")
    else:
        critical = [r for r in failed if r.get("severity") == "critical"]
        status = "BROKEN" if critical else "DEGRADED"
        lines.append(f"\n{len(results)} checks run, {len(failed)} failed.")
        lines.append(f"Overall: Pipeline is {status}.")

    return "\n".join(lines)
