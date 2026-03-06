# Session 4: Agents + Ship — Polish, Test, Deploy

**Format:** 90 min live + async challenge
**Goal:** Add AI-powered features, write tests, polish, and deploy your app

## Session Plan

This session combines three things: adding agent/AI capabilities to your app, writing tests, and getting production-ready. It's a sprint — by the end, your app should be deployed and demo-ready.

### Part 1: AI-Powered Features (30 min)

**Concept (10 min): Adding AI Inside Your App**

Two ways AI can be part of your product (beyond just building it):

1. **AI as a feature** — Your app calls the Claude API to do something for the user (summarize, analyze, generate, classify, recommend)
2. **AI as automation** — Background tasks that run with AI (email drafts, content generation, data processing)

Not every app needs this. But if it makes sense for your capstone, this is how.

**Demo (20 min): Add an AI Feature**

Using the task manager example:
```
Prompt: Add an AI-powered feature to the task manager:
- A "Smart Categorize" button that uses Claude API to automatically
  categorize uncategorized tasks based on their titles
- Show a loading state while the API call is in progress
- Let the user accept or reject each suggestion before saving
- Handle API errors gracefully

Use the Anthropic SDK. The API key should come from environment variables.
```

Walk through:
- Setting up the Claude API key
- Making the API call from a server-side route (never from the client)
- Handling the response and updating the UI
- Error states and loading states

**For non-technical builders:** This might be the most magical moment — your app is *thinking*. But keep it simple. One AI feature, well-implemented, is better than three half-broken ones.

### Part 2: Testing and Quality (25 min)

**Demo (15 min): Generate Tests With AI**
```
Prompt: Write tests for my task manager app.

Here's the code for the API routes:
[paste code]

Generate:
1. Unit tests for the API routes (create, read, update, delete tasks)
2. Edge cases: empty title, very long title, invalid category, missing fields
3. A simple smoke test that verifies the homepage loads

Use [Jest/Vitest/pytest] depending on the stack.
```

Run the tests. Show which pass, which fail. Fix the failures.

**Security quick-check (10 min):**
```
Prompt: Review my app for security issues:
[paste code]

Check for:
- API keys exposed to the client
- SQL injection or NoSQL injection
- Missing input validation
- CORS misconfiguration
- Missing rate limiting on API routes
```

### Part 3: Deploy and Polish (20 min)

**Deploy live (10 min):**
Walk through deploying to Vercel/Railway:
- Connect GitHub repo
- Set environment variables
- Deploy
- Verify it works at the live URL

**Polish sprint (10 min):**
Use AI to quickly fix:
- Mobile responsiveness
- Error messages for users
- Loading states
- A favicon and page title (small but makes it feel real)

### Debrief (15 min)
- Who has a live URL? Share it.
- What's left to do before demo day?

## Async Challenge

### Task
Get your capstone demo-ready:

1. **Live and deployed** — Working URL that someone can visit
2. **Core features complete** — Everything you planned to demo works
3. **Tests exist** — At least 3 meaningful tests pass
4. **No secrets exposed** — API keys in env vars, not in code
5. **README is complete** — What it does, live URL, how to run locally, how to contribute
6. **Practice your demo** — 5 minutes. Time yourself.

### Demo Day Prep Checklist
- [ ] App is deployed and accessible
- [ ] Core features work without errors
- [ ] You can explain what it does in 1 sentence
- [ ] You have a 5-minute walkthrough rehearsed
- [ ] README includes live URL and screenshots
- [ ] GitHub repo is public and clean (no sensitive data in commit history)

Push final version to GitHub, share in community with `#builder-session4`.

---

**Previous:** [Session 3 — Full Stack](../session-03-fullstack/)
**Next:** [Session 5 — Ship It: Demo Day](../session-05-ship-it/)
