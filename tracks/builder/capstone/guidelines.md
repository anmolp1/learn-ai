# Builder Track Capstone Guidelines

## Overview

Build and ship a working application using AI as your development partner. This should be an app you actually want to exist — not a tutorial project.

## Requirements

1. **Solves a specific problem** for a real audience (even if that audience is just you)
2. **Deployed and accessible** via a public URL
3. **Has a working UI** — web app, CLI, or API with documentation
4. **Uses AI meaningfully** — either in the build process (documented) OR as a product feature
5. **Has tests** — at least 3 meaningful tests that pass
6. **Public GitHub repo** with a complete README

## Timeline

| Session | Milestone |
|---------|-----------|
| 0 | Choose app idea, set up repo, get tools working |
| 1 | Product spec + project scaffold running locally |
| 2 | Working prototype with 2-3 core features |
| 3 | Backend + database + deployed preview |
| 4 | AI features + tests + production deploy |
| 5 | Present |

## Example Projects

### For Developers

| Project | Stack | AI Integration |
|---------|-------|---------------|
| Personal Finance Tracker | Next.js + Supabase | AI categorizes transactions, generates spending insights |
| Dev Bookmark Manager | React + FastAPI + SQLite | AI auto-tags and summarizes bookmarked articles |
| Meeting Notes App | Next.js + Whisper API | AI transcribes audio, extracts action items |
| API Health Dashboard | React + Express | Monitors APIs, AI classifies errors and suggests fixes |
| Resume Builder | Next.js + Claude API | AI helps write and tailor resume sections |

### For Non-Technical Builders

| Project | Stack | AI Integration |
|---------|-------|---------------|
| Portfolio Site | Next.js on Vercel | AI generates project descriptions from bullet points |
| Recipe Organizer | React + Supabase | AI suggests recipes from available ingredients |
| Study Flashcard App | Next.js | AI generates flashcards from pasted notes |
| Gift Idea Generator | Single-page app + Claude API | Takes person description, suggests gift ideas |
| Daily Journal | React + localStorage | AI summarizes weekly entries, spots patterns |

## Repo Structure

```
my-capstone/
├── README.md              # What, why, live URL, setup, screenshots
├── src/                   # Application source code
├── tests/                 # Test files
├── public/                # Static assets
├── .env.example           # Environment variable template
├── .gitignore
└── package.json / requirements.txt
```

## README Template

```markdown
# [App Name]

[One sentence: what it does]

**Live:** [your-app.vercel.app](https://your-app.vercel.app)

## Screenshot
[Include at least one screenshot]

## Problem
What problem does this solve? Who is it for?

## Features
- Feature 1
- Feature 2
- Feature 3

## AI Integration
How AI was used — both to build the app and within the app itself.

## Tech Stack
- Frontend: [framework]
- Backend: [framework]
- Database: [database]
- AI: [Claude API / Copilot / Claude Code]
- Hosting: [platform]

## Run Locally
1. Clone the repo
2. `cp .env.example .env.local` and fill in values
3. `npm install` (or equivalent)
4. `npm run dev`

## Built During
Learn AI: Builder Track — [link to program]
```

## Evaluation Rubric

| Criteria | Weight | Great |
|----------|--------|-------|
| Problem + audience | 15% | Clearly defined, real problem with a specific user |
| Working product | 30% | Core features work, deployed, accessible |
| AI integration | 20% | AI adds real value — either in the product or demonstrably in the build process |
| Code quality + tests | 15% | Clean code, tests pass, no security issues |
| UX + polish | 10% | Looks decent, handles errors, works on mobile |
| Documentation | 10% | README is complete, someone else could set up and run the project |
