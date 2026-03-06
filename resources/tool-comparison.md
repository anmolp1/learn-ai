# AI Tools Landscape

A practical comparison of AI tools referenced in this program. Last updated: March 2026.

> **Note:** This space moves fast. Review and update this document quarterly.

## AI Assistants

| Tool | Best For | Pricing | Notes |
|------|----------|---------|-------|
| **Claude** (Anthropic) | Long-form reasoning, code, analysis, writing | Free tier + Pro ($20/mo) | Strong at following complex instructions. Supports tool use and agents via MCP. |
| **ChatGPT** (OpenAI) | General assistance, image generation, plugins | Free tier + Plus ($20/mo) | Large ecosystem. Good for exploration and general tasks. |
| **Gemini** (Google) | Google Workspace integration, multimodal tasks | Free tier + Advanced | Strong integration with Google ecosystem. |

## AI Coding Tools

| Tool | Best For | Pricing | Notes |
|------|----------|---------|-------|
| **Claude Code** | Agentic coding from the terminal | Included with Claude subscription | Can read/write files, run commands, manage git. Good for complex multi-file tasks. |
| **GitHub Copilot** | Inline code completion | $10-19/mo | Integrated into VS Code, JetBrains, etc. Best for autocomplete-style assistance. |
| **Cursor** | AI-native code editor | Free tier + Pro ($20/mo) | Fork of VS Code with deep AI integration. Good for people who want AI everywhere in their editor. |
| **Codex / OpenAI Codex** | Code generation via API | API pricing | Good for building AI-powered developer tools. |

## Agent Frameworks

| Tool | Best For | Complexity | Notes |
|------|----------|------------|-------|
| **Claude MCP** | Connecting Claude to external tools/data | Low-Medium | Model Context Protocol. Lets Claude interact with APIs, databases, files. |
| **LangChain** | Complex multi-step agent workflows | Medium-High | Popular framework. Large ecosystem but can be over-engineered for simple tasks. |
| **CrewAI** | Multi-agent collaboration | Medium | Good for workflows where different "agents" handle different parts of a task. |
| **GitHub Actions + AI** | CI/CD with AI steps | Low-Medium | Use AI in your existing CI/CD pipelines. Good for automated code review, testing, docs. |

## How to Choose

1. **Start simple.** Use Claude or ChatGPT directly before reaching for frameworks.
2. **Add tools as needed.** MCP or simple API calls before full agent frameworks.
3. **Match to your workflow.** Pick tools that integrate with what you already use.
4. **Don't lock in.** The landscape changes fast. Stay tool-agnostic in your thinking.
