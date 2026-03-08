# Claude API Quickstart

This guide covers everything you need to start using the Claude API in your data engineering work.

---

## Sign Up and Get Your API Key

1. Go to [console.anthropic.com](https://console.anthropic.com/).
2. Create an account (or sign in if you already have one).
3. Navigate to **API Keys** in the left sidebar.
4. Click **Create Key**.
5. Give it a descriptive name like `learn-ai-data-eng`.
6. Copy the key immediately — you will not be able to see it again.

## API Key Management

**Never commit your API key to version control.** This is the most important rule.

Store your key as an environment variable:

```bash
# Add to your ~/.zshrc (macOS) or ~/.bashrc (Linux)
export ANTHROPIC_API_KEY="sk-ant-your-key-here"

# Then reload your shell
source ~/.zshrc
```

On Windows (PowerShell):

```powershell
[System.Environment]::SetEnvironmentVariable("ANTHROPIC_API_KEY", "sk-ant-your-key-here", "User")
```

**Additional safety measures:**
- Add `.env` to your `.gitignore` if you use dotenv files.
- Never paste your key in shared notebooks or documents.
- If you accidentally commit a key, rotate it immediately in the Anthropic console.

## Install the Python SDK

```bash
pip install anthropic
```

## 5-Line Test Script

```python
import anthropic

client = anthropic.Anthropic()  # Reads ANTHROPIC_API_KEY from environment
message = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=100,
    messages=[{"role": "user", "content": "Say hello in exactly 5 words."}]
)
print(message.content[0].text)
```

Run it:

```bash
python test_claude.py
```

If you see a 5-word greeting, your setup works.

## Request and Response Anatomy

### The Request

Every API call has these core components:

```python
message = client.messages.create(
    model="claude-sonnet-4-20250514",   # Which model to use
    max_tokens=1024,                # Maximum tokens in the response
    system="You are a data engineer.", # Optional: system prompt to set context
    messages=[                      # The conversation history
        {
            "role": "user",
            "content": "Write a SQL query to find duplicate rows in a table called orders."
        }
    ]
)
```

**Key parameters:**
| Parameter | Required | Description |
|-----------|----------|-------------|
| `model` | Yes | Model ID. Use `claude-sonnet-4-20250514` for a good balance of speed and quality. |
| `max_tokens` | Yes | Cap on response length. 1024 is usually enough for code snippets. |
| `messages` | Yes | List of message objects with `role` ("user" or "assistant") and `content`. |
| `system` | No | System prompt. Use this to set the persona or provide standing instructions. |
| `temperature` | No | 0.0 to 1.0. Lower = more deterministic. Default is 1.0. Use 0 for code generation. |

### The Response

```python
# The response object
message.id          # "msg_abc123..." — unique message ID
message.model       # "claude-sonnet-4-20250514"
message.content     # List of content blocks
message.content[0].text  # The actual text response
message.usage.input_tokens   # Tokens in your prompt
message.usage.output_tokens  # Tokens in the response
message.stop_reason          # "end_turn", "max_tokens", etc.
```

**Extracting the text response:**

```python
response_text = message.content[0].text
```

## Cost Tracking Tips

The Claude API charges per token. For this program, expect to spend **$2-5 total** across all sessions.

**Approximate costs (Claude Sonnet):**
- Input: $3 per 1M tokens
- Output: $15 per 1M tokens
- A typical request/response pair (500 input tokens, 300 output tokens) costs roughly $0.006

**How to monitor your spend:**
1. Check your usage at [console.anthropic.com/usage](https://console.anthropic.com/usage).
2. Set a monthly spend limit in your account settings under **Plans & Billing > Spending Limits**.
3. Log token usage in your scripts (see the wrapper function below).

**Tips to minimize cost:**
- Be specific in prompts — vague prompts lead to long responses you do not need.
- Use `max_tokens` to cap response length.
- Avoid sending large data payloads in prompts. Send schemas and samples, not full datasets.

## Reusable Wrapper Function for Pipeline Monitoring

Use this wrapper in your pipeline scripts. It handles errors, logs token usage, and provides a clean interface.

```python
import anthropic
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

client = anthropic.Anthropic()

def ask_claude(
    prompt: str,
    system: str = "You are a senior data engineer. Be concise and return code without explanation unless asked.",
    model: str = "claude-sonnet-4-20250514",
    max_tokens: int = 1024,
    temperature: float = 0.0
) -> str:
    """
    Send a prompt to Claude and return the text response.

    Use this for pipeline monitoring tasks like:
    - Generating SQL to investigate data quality issues
    - Summarizing error logs
    - Suggesting fixes for failed pipeline steps

    Args:
        prompt: The user message to send.
        system: System prompt for context. Default is data engineering persona.
        model: Model ID.
        max_tokens: Maximum response tokens.
        temperature: Randomness (0 = deterministic, 1 = creative).

    Returns:
        The text content of Claude's response.
    """
    try:
        message = client.messages.create(
            model=model,
            max_tokens=max_tokens,
            temperature=temperature,
            system=system,
            messages=[{"role": "user", "content": prompt}]
        )

        # Log token usage for cost tracking
        input_tokens = message.usage.input_tokens
        output_tokens = message.usage.output_tokens
        est_cost = (input_tokens * 3 + output_tokens * 15) / 1_000_000
        logger.info(
            f"Claude API call: {input_tokens} input tokens, "
            f"{output_tokens} output tokens, ~${est_cost:.4f}"
        )

        return message.content[0].text

    except anthropic.APIConnectionError:
        logger.error("Could not connect to the Anthropic API. Check your internet connection.")
        raise
    except anthropic.AuthenticationError:
        logger.error("Invalid API key. Check your ANTHROPIC_API_KEY environment variable.")
        raise
    except anthropic.RateLimitError:
        logger.warning("Rate limited. Wait a moment and retry.")
        raise


# Example usage in a pipeline monitoring context:
if __name__ == "__main__":
    # Scenario: your pipeline detected a data quality issue
    issue_summary = "The orders table has 142 rows where revenue is 0 but units_sold > 0."

    response = ask_claude(
        f"Given this data quality issue, write a BigQuery SQL query to investigate: {issue_summary}"
    )
    print(response)
```

## Tool Use and Agentic Patterns

The Claude API supports **tool use** — you define tools (functions) that Claude can call, and Claude decides when to use them. This is the foundation for building agents.

### Defining Tools

Tools are defined as a list of dictionaries with `name`, `description`, and `input_schema`:

```python
tools = [
    {
        "name": "check_row_count",
        "description": "Check that the dataset has at least a minimum number of rows.",
        "input_schema": {
            "type": "object",
            "properties": {
                "min_expected": {
                    "type": "integer",
                    "description": "Minimum expected row count",
                }
            },
            "required": [],
        },
    }
]
```

Pass `tools=tools` to `client.messages.create()` and Claude will see these tools as available actions.

### Handling Tool Calls

When Claude wants to call a tool, the response has `stop_reason == "tool_use"` and includes a `tool_use` content block:

```python
response = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=4096,
    tools=tools,
    messages=messages,
)

# Check if Claude wants to call a tool
for block in response.content:
    if block.type == "tool_use":
        tool_name = block.name      # e.g., "check_row_count"
        tool_input = block.input    # e.g., {"min_expected": 5}
        tool_id = block.id          # unique ID for this tool call
```

### The Agentic Loop

An agent is a while loop: send tools to Claude, execute what it calls, send results back, repeat until Claude is done.

```python
messages = [{"role": "user", "content": "Check this data for quality issues."}]

while True:
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=4096,
        tools=tools,
        messages=messages,
    )

    if response.stop_reason == "end_turn":
        # Claude is done — extract final text
        print(response.content[0].text)
        break

    # Execute tool calls and collect results
    tool_results = []
    for block in response.content:
        if block.type == "tool_use":
            result = execute_my_tool(block.name, block.input)
            tool_results.append({
                "type": "tool_result",
                "tool_use_id": block.id,
                "content": result,
            })

    # Send Claude's response + tool results back for the next iteration
    messages.append({"role": "assistant", "content": response.content})
    messages.append({"role": "user", "content": tool_results})
```

### Cost Note

Tool definitions add ~500-1000 tokens to each API call (they're included in the system prompt). A typical agent run with 3-5 tool calls costs ~$0.02-0.05 with Claude Sonnet.

For a complete working example, see [`examples/starter-agent/agent.py`](../examples/starter-agent/agent.py).
