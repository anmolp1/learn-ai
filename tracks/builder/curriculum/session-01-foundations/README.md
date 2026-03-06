# Session 1: Foundations — Building With AI

**Format:** 90 min live + async challenge
**Goal:** Learn how to direct AI to build software, not just write code snippets

## Session Plan

### Opening (10 min)
- Introductions: name, background, what you want to build
- Show 2-3 baseline results — celebrate the range
- Frame: "AI is the best junior developer who ever lived. Fast, tireless, never complains — but needs clear direction and always needs code review."

### Concept: The AI-Assisted Development Workflow (20 min)

**For developers — AI as a pair programmer:**
Your workflow shifts from "write code" to "direct, review, and refine code." The value isn't that AI writes code faster — it's that it handles the low-value work (boilerplate, tests, docs, repetitive patterns) so you focus on the high-value work (architecture, edge cases, UX, performance).

**For non-technical builders — AI as a technical co-founder:**
You describe what you want. AI builds it. You test it, give feedback, and iterate. Your superpower is product thinking — knowing what to build and why. AI's superpower is turning descriptions into working code.

**The workflow for both:**
1. **Plan** — Define what you're building (features, user flow, data model)
2. **Scaffold** — AI generates the initial project structure
3. **Build** — AI writes features one at a time. You review each one.
4. **Test** — Run it. Break it. Tell AI what's wrong. Iterate.
5. **Ship** — Deploy. Get it in front of users. Iterate again.

### Demo (30 min): From Idea to Running Code in 30 Minutes

**Build something live.** Choose based on audience:

**Option A (for a developer-heavy group):** A REST API with 3 endpoints
```
Prompt: I'm building a bookmark manager API with these features:
- POST /bookmarks — save a URL with title and tags
- GET /bookmarks — list all bookmarks, filterable by tag
- DELETE /bookmarks/:id — remove a bookmark

Use Python/FastAPI. Include input validation, error handling,
and an in-memory store (we'll add a database later).
Generate the full project: main.py, requirements.txt, README with setup instructions.
```

**Option B (for a non-technical or mixed group):** A simple web app
```
Prompt: Build me a single-page web app that:
- Has an input field where I type a topic
- Has a "Generate" button
- When clicked, it shows 5 creative project ideas related to that topic
- Use HTML, CSS, and vanilla JavaScript
- Make it look clean and modern with a dark theme
- No external dependencies — everything in one HTML file
```

**Show the full cycle:**
1. Write the prompt
2. Get the code
3. Run it — find something that doesn't work
4. Tell AI what's wrong → get a fix
5. Ask for an improvement → iterate
6. End with a working app

**Key teaching moment:** Show a failure. Show a bad output. Show how to give AI feedback that actually fixes the problem. This is the real skill.

### Practice (25 min)
Participants start building:
- Describe your capstone app in 3-5 sentences
- Use Claude to generate the project scaffold
- Get *something* running locally — even if it's just a "Hello World" with your app's name
- Push to GitHub

### Debrief (5 min)
- What surprised you about AI-generated code?
- Preview: "Next session, we go from scaffold to working prototype"

## Async Challenge

### Task
Get your capstone app's foundation working:

1. **Write a product spec** — 1 page max: what the app does, who it's for, core features (3-5), nice-to-haves (for later)
2. **Scaffold with AI** — Use Claude to generate the initial project structure
3. **Get it running locally** — Even if it's just the homepage or a single endpoint
4. **Push to GitHub** — With a README that explains what you're building

### Tips for Non-Technical Builders
- Start with Cursor — it's the most forgiving environment
- If you get stuck on terminal commands, ask Claude: "I'm in Cursor's terminal on Mac/Windows. How do I [thing]?"
- If code doesn't run, copy the error message and paste it to Claude. That's literally the workflow.
- Don't try to understand every line of code yet. Focus on: does it work? Does it do what I want?

Share in community with `#builder-session1`.

## Resources
- [Claude Code docs](https://docs.anthropic.com/en/docs/claude-code)
- [Cursor docs](https://docs.cursor.com/)
- [Vercel deployment guide](https://vercel.com/docs/getting-started)
- [GitHub Pages](https://pages.github.com/) (simplest free hosting for static sites)

---

**Previous:** [Session 0 — Pre-Work](../session-00-prework/)
**Next:** [Session 2 — Scaffold: From Idea to Working Prototype](../session-02-scaffold/)
