# Session 2: Scaffold — From Idea to Working Prototype

**Format:** 90 min live + async challenge
**Goal:** Turn your app idea into a working prototype with AI doing the heavy lifting

## Session Plan

### Concept (15 min): The Scaffold-First Approach

Traditional development: plan everything → build layer by layer → hope it works.

AI-assisted development: describe what you want → get a working version fast → iterate.

**The scaffold approach:**
1. **Start with the UI** — Get something visual running first. It motivates you and gives you something to iterate on.
2. **Add functionality one feature at a time** — Don't ask AI for everything at once. One feature per prompt.
3. **Test as you go** — After each feature, run it. Does it work? Does it do what you expect?
4. **Commit often** — Every working state gets a git commit. AI can break things; you want rollback points.

### Demo (35 min): Build a Prototype From a Product Spec

**Live-code a prototype.** Suggested app: a simple task manager with categories and filtering.

**Step 1 — The skeleton (8 min)**
```
Prompt: I'm building a task manager web app. Create the initial project with:
- Next.js with TypeScript (or React + Vite if simpler for audience)
- A clean, minimal UI with a header, main content area, and sidebar
- Tailwind CSS for styling
- No functionality yet — just the layout and navigation
Give me the full project files.
```

Run it. Show the empty shell. This is the canvas.

**Step 2 — Core feature: add and list tasks (8 min)**
```
Prompt: Add the ability to create and list tasks.
- An input field + "Add" button at the top
- Tasks appear in a list below
- Each task shows: title, created date
- Store tasks in React state for now (no database yet)
- Include a way to mark tasks as complete (checkbox + strikethrough)
```

Run it. Show it working. Show what Claude got wrong. Fix it.

**Step 3 — Second feature: categories and filtering (8 min)**
```
Prompt: Add categories to tasks.
- When adding a task, choose a category from: Work, Personal, Learning, Other
- Sidebar shows categories with task counts
- Clicking a category filters the list
- "All" option shows everything
```

**Step 4 — Make it real: persistence (8 min)**
```
Prompt: Add localStorage persistence so tasks survive page refresh.
Keep the existing UI exactly as it is.
```

For developers: show the alternative of adding a real database (SQLite, Supabase, or a simple JSON API).

**Step 5 — Polish (3 min)**
```
Prompt: Make these improvements:
- Add a delete button (with confirmation) on each task
- Empty state message when no tasks exist
- Sort tasks: incomplete first, then by created date
- Add keyboard shortcut: Enter to add task when input is focused
```

**Show the pattern:** each prompt is one feature. Review. Test. Commit. Next feature.

### Practice (25 min)
Participants build their capstone prototype:
- Start from the scaffold they created in Session 1
- Add 2-3 core features using the one-feature-per-prompt pattern
- Goal: a working prototype you can click through, even if it's rough
- Push to GitHub

### Debrief (15 min)
- Show and tell: who has something working? Show your screen.
- Common issues: what went wrong? How did you fix it?

## Async Challenge

### Task
Build your capstone prototype to the point where someone can use it:

1. **Core features working** — The 2-3 most important features of your app function correctly
2. **It looks decent** — Not polished, but not broken. Someone could look at it and understand what it does.
3. **Committed to GitHub** — Multiple commits showing your progress (not one giant commit)
4. **README updated** — What the app does, how to run it locally, what's working and what's not yet

### The "Show a Friend" Test
If you showed this to a friend, could they:
- Understand what the app does?
- Use it (even if roughly) for its intended purpose?
- Give you feedback on what to improve?

If yes, you're in great shape for Session 3.

Share in community with `#builder-session2`. Include a screenshot or short screen recording.

---

**Previous:** [Session 1 — Foundations](../session-01-foundations/)
**Next:** [Session 3 — Full Stack: Frontend, Backend, Database](../session-03-fullstack/)
