# AGENTS.md — Instructions for AI Coding Agents

This file provides guidance for AI agents (Cursor, Copilot, Claude Code, etc.) working in this repository.

## What This Repo Is

A Markdown-based curriculum repository for an open-source AI bootcamp called **Learn AI**. There is no application code, no build system, and no tests. The deliverables are written content: session plans, exercises, guides, and capstone guidelines.

## Structure at a Glance

- `tracks/<track-name>/` — Standalone role-specific programs, each with their own `curriculum/` and `capstone/`
- `curriculum/` — [Deprecated] Legacy shared curriculum — superseded by track-specific curricula
- `resources/` — Shared references (prompting guide, tool comparison)
- `instructor/` — Facilitator materials for running cohorts
- `capstone/` — Shared capstone project guidelines and showcase

Active tracks: **data-engineering** (7 sessions), **builder** (6 sessions). Security and marketing are placeholders.

## Writing Guidelines

1. **Audience:** Working professionals integrating AI into their jobs. Not academics, not complete beginners.
2. **Tone:** Direct, practical, conversational. No filler. No hype.
3. **Examples:** Must be working and testable. No pseudocode.
4. **Jargon:** Define on first use or avoid entirely.
5. **Structure:** Use headers, tables, and bullet points. Favor scannability over prose.
6. **Tool references:** Teach the pattern first, then name the tool as one implementation. Tools change; patterns endure.

## Rules

- Each track is self-contained. Don't create cross-track dependencies.
- Every session should connect to the capstone project in some way.
- Don't add package.json, requirements.txt, Dockerfiles, or CI configs — this is a content repo.
- Follow existing naming conventions: `session-XX-topic/README.md`.
- When editing a session, read the sessions before and after it to maintain narrative flow.
- Respect the session rhythm: Concept (20 min) > Demo (30 min) > Practice (25 min) > Debrief (15 min) > Async challenge.

## License

Content: CC BY-SA 4.0 | Code examples: MIT
