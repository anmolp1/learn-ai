# Session 3: Full Stack — Frontend, Backend, Database

**Format:** 90 min live + async challenge
**Goal:** Add persistence, real data, and backend logic to your prototype

## Session Plan

### Concept (15 min): Picking Your Stack With AI

You don't need to know the "right" stack beforehand. AI can help you choose based on your app's needs, and then help you implement it.

**Simple decision framework:**

| App Type | Recommended Stack | Why |
|----------|------------------|-----|
| Static site / simple app | HTML + vanilla JS, or React | No backend needed, easy to deploy |
| App with user data | Next.js + Supabase OR React + FastAPI + SQLite | Need persistence, auth might come later |
| API / data tool | FastAPI (Python) or Express (Node) | Backend-focused, no complex UI |
| AI-powered app | Any frontend + Claude API | Needs API integration for AI features |

**For non-technical builders:** Don't stress about this. We'll use whatever gets your app working fastest. If in doubt, Next.js + Supabase is the most beginner-friendly full-stack option with AI.

### Demo (35 min): Add Backend + Database to the Prototype

**Continue building the task manager from Session 2.**

**Step 1 — Add a database (10 min)**
```
Prompt: Replace the localStorage in my task manager with Supabase.
- Create the Supabase client configuration
- Define a "tasks" table schema: id, title, category, completed, created_at
- Update all CRUD operations to use Supabase instead of localStorage
- Keep the existing UI exactly the same
- Add proper error handling for database operations

Here's my current code:
[paste relevant files]
```

For developers: show the alternative with a local SQLite database or PostgreSQL.

**Step 2 — Add an API layer (if applicable) (8 min)**
```
Prompt: Add API routes for the task manager:
- GET /api/tasks — list tasks with optional category filter
- POST /api/tasks — create a task
- PATCH /api/tasks/:id — update a task (toggle complete, edit title)
- DELETE /api/tasks/:id — delete a task

Include input validation and error responses.
```

**Step 3 — Add a real feature that needs the backend (10 min)**

Pick one based on the app:
- Search across tasks (needs a query endpoint)
- Task statistics / dashboard (needs aggregation)
- Export to CSV (needs server-side generation)
- AI-powered feature: "Suggest task priority based on title" using Claude API

**Step 4 — Environment variables and config (7 min)**

Important for everyone, but especially non-technical builders:
```
Prompt: Set up proper environment variable handling for my app.
- Move all API keys and database URLs to .env.local
- Create a .env.example file with placeholder values
- Make sure .env.local is in .gitignore
- Update the README with setup instructions
```

Show why this matters: committing API keys to GitHub is one of the most common mistakes.

### Practice (25 min)
Participants add persistence to their capstone:
- Connect a database (Supabase, SQLite, or any appropriate option)
- Move at least one feature from in-memory to persistent storage
- Add one new feature that uses the database
- Push to GitHub

### Debrief (15 min)
- What was harder than expected?
- Developer vs. non-technical perspective: how different was the experience?

## Async Challenge

### Task
Make your capstone app "real" — it should persist data and have backend logic:

1. **Database connected** — User data persists across sessions
2. **At least one API endpoint or server action** (even if it's Next.js server actions)
3. **Environment variables** — No secrets in code
4. **One new feature** that wasn't possible without a backend
5. **Deploy a preview** — Push to Vercel/Railway/Replit so you have a live URL

### For Non-Technical Builders
Deploying can feel scary. It's not. Here's the pattern:
1. Push code to GitHub
2. Connect GitHub repo to Vercel/Railway
3. Add your environment variables in the deployment platform's settings
4. Click deploy

If that's still intimidating, ask Claude: "Walk me through deploying my Next.js app to Vercel step by step."

Share in community with `#builder-session3`. Include your live URL!

---

**Previous:** [Session 2 — Scaffold](../session-02-scaffold/)
**Next:** [Session 4 — Agents + Ship: Polish, Test, Deploy](../session-04-agents/)
