# CLAUDE.md — Instructions for Claude Code

## Project Overview

This is **Learn AI**, an open-source cohort-based bootcamp that teaches professionals how to integrate AI tools into their real workflows. It is a **content/curriculum repo** — primarily Markdown files, not a software project.

## Repository Structure

```
tracks/                    # Role-specific standalone programs (each has its own curriculum + capstone)
  data-engineering/        # 7 sessions (0-6), 3 weeks
  builder/                 # 6 sessions (0-5), 2.5 weeks
  security/                # Coming soon (placeholder)
  marketing/               # Coming soon (placeholder)
curriculum/                # [Deprecated] Legacy shared curriculum — do not add content here
capstone/                  # Shared capstone guidelines and showcase
resources/                 # Shared resources (prompting guide, tool comparison)
```

**Related repos (not in this repo):**
- `learn-ai-ops` (private) — Instructor materials, cohort rosters, email templates
- `learn-ai-starter` (public template) — Participant starting point with capstone + journal templates

## Key Conventions

### Content Style
- Write for **working professionals new to AI integration** — not researchers, not beginners
- Plain language. Define jargon when first used. Avoid buzzwords.
- Practical over theoretical — every concept should connect to something the reader will do
- Include **working examples**, not pseudocode
- Keep instructions actionable: steps, not paragraphs

### Track Independence
- Each track under `tracks/` is **standalone** with its own curriculum, capstone guidelines, and session numbering
- Do not assume content from one track applies to another
- Shared resources live in the top-level `resources/` and `instructor/` directories

### Session Structure
Each session README follows the pattern:
1. Objectives / what you'll learn
2. Content / concepts
3. Hands-on exercises
4. Async challenge (homework connecting to capstone)

### File Naming
- Session directories: `session-XX-topic/` (e.g., `session-02-pipelines/`)
- Each session has a `README.md` as its primary file
- Supplementary files (demos, challenges, slides) go alongside the README

## Licensing
- Content: CC BY-SA 4.0
- Code examples: MIT

## What NOT to Do
- Don't add code scaffolding, build systems, or package files — this is a content repo
- Don't restructure tracks without understanding their standalone design
- Don't write content that's tool-specific without teaching the underlying pattern first
- Don't add sessions or tracks without corresponding capstone integration
