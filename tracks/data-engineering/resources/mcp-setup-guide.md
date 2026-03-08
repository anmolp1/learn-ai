# MCP Setup Guide

## What is MCP?

Model Context Protocol (MCP) is an open standard (created by Anthropic) that lets AI models connect to external data sources and tools through a consistent interface. Instead of writing custom API integration code, you configure an MCP server and Claude can query your databases, check your pipelines, and interact with your infrastructure directly.

## When to Use MCP vs Python Tool Definitions

| Approach | Use when... |
|----------|-------------|
| **Python tool definitions** (like `starter-agent/tools.py`) | You want full control, custom logic, or are learning the tool-use pattern |
| **MCP servers** | You want plug-and-play access to databases, APIs, or infrastructure without writing wrapper code |

For this program, start with Python tool definitions to understand the pattern. MCP is a natural next step when you want to connect Claude to your actual infrastructure.

## Available MCP Servers for Data Engineering

| Server | What it does | Install |
|--------|-------------|---------|
| [BigQuery](https://github.com/ergut/mcp-bigquery) | Query tables, inspect schemas, list datasets | `npx @anthropic/mcp-bigquery` |
| [SQLite](https://github.com/modelcontextprotocol/servers/tree/main/src/sqlite) | Query local SQLite databases (great for dev/testing) | `npx @modelcontextprotocol/server-sqlite` |
| [PostgreSQL](https://github.com/modelcontextprotocol/servers/tree/main/src/postgres) | Query Postgres databases | `npx @modelcontextprotocol/server-postgres` |
| [Filesystem](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem) | Read/write files in specified directories | `npx @modelcontextprotocol/server-filesystem` |

Browse more at [github.com/modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers).

## Setup: SQLite MCP Server (Local Dev)

The simplest way to try MCP — no cloud credentials needed.

### Prerequisites
- Node.js 18+ (`node --version`)

### Configure Claude Desktop

1. Open Claude Desktop settings (Claude > Settings > Developer > Edit Config)
2. Add to `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "sqlite": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-sqlite",
        "--db-path",
        "/path/to/your/database.db"
      ]
    }
  }
}
```

3. Restart Claude Desktop
4. You should see a tools icon in the chat — Claude can now query your SQLite database

### Test It

Ask Claude: "What tables are in this database? Show me the first 5 rows of each."

## Setup: BigQuery MCP Server

### Prerequisites
- Node.js 18+
- GCP project with BigQuery enabled
- Application Default Credentials configured

### Configure GCP Credentials

```bash
# If you haven't already (from Session 0 setup)
gcloud auth application-default login
```

### Configure Claude Desktop

Add to `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "bigquery": {
      "command": "npx",
      "args": [
        "-y",
        "@anthropic/mcp-bigquery"
      ],
      "env": {
        "BQ_PROJECT_ID": "your-gcp-project-id",
        "BQ_LOCATION": "US"
      }
    }
  }
}
```

Restart Claude Desktop. Claude can now query your BigQuery datasets directly.

## Using MCP with Claude Code (CLI)

Claude Code can also use MCP servers. Add to your project's `.mcp.json`:

```json
{
  "mcpServers": {
    "sqlite": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-sqlite", "--db-path", "./data/pipeline.db"]
    }
  }
}
```

Then run `claude` in that directory — the MCP tools will be available automatically.

## Troubleshooting

**"npx: command not found"**
Install Node.js 18+: `brew install node` (macOS) or download from [nodejs.org](https://nodejs.org/).

**"Could not find credentials"**
Run `gcloud auth application-default login` and make sure you select the right GCP project.

**BigQuery server starts but can't find tables**
Check your `BQ_PROJECT_ID` — it must match the project where your datasets live. Run `bq ls` to verify you can see datasets from the command line.

**MCP server not showing in Claude Desktop**
- Check JSON syntax in `claude_desktop_config.json` (trailing commas break it)
- Restart Claude Desktop fully (quit and reopen, not just close window)
- Check logs: `~/Library/Logs/Claude/` (macOS)
