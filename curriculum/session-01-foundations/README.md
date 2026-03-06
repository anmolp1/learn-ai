# Session 1: Foundations — How to Think With AI

**Format:** 90 min live + async challenge
**Prerequisites:** Session 0 complete
**Goal:** Build the right mental models for AI collaboration

## Session Plan (For Instructors)

### Opening (10 min)
- Welcome, introductions, logistics
- Share a few baseline challenge results from participants — celebrate the range of experience
- Frame the session: "Today is about changing how you think about AI, not just what buttons to press"

### Concept: Mental Models for AI (20 min)

**Key ideas to cover:**

1. **AI as a junior colleague, not a magic oracle**
   - It's eager, fast, and sometimes confidently wrong
   - Your job is to direct, review, and refine — not to accept blindly
   - The best results come from iteration, not one-shot prompts

2. **The spectrum of AI assistance**
   - Level 1: AI answers questions (search replacement)
   - Level 2: AI drafts work for you to edit (first-draft generator)
   - Level 3: AI executes multi-step workflows (agent)
   - Level 4: AI monitors and acts autonomously (automation)
   - Most people are stuck at Level 1-2. This program takes you to Level 3-4.

3. **When AI helps vs. when it hurts**
   - Helps: repetitive tasks, first drafts, boilerplate, exploration, debugging
   - Hurts: novel reasoning, sensitive decisions, tasks requiring deep domain context AI doesn't have
   - Key skill: knowing which category your task falls into

### Demo: Prompting Patterns That Work (30 min)

**Live demo using a real task from participant intake forms.**

Walk through these patterns with real examples:

1. **Structured prompts** — Give AI context, constraints, and a clear output format
   ```
   You are a [role]. I need you to [task].
   Context: [relevant background]
   Constraints: [limits, requirements]
   Output format: [what you want back]
   ```

2. **Chain-of-thought** — Ask AI to think step by step
   ```
   Before giving me the answer, walk through your reasoning step by step.
   ```

3. **Few-shot examples** — Show AI what good output looks like
   ```
   Here are 2 examples of what I want:
   [Example 1]
   [Example 2]
   Now do the same for: [new input]
   ```

4. **Iterative refinement** — Don't stop at the first response
   ```
   Good start. Now make these changes: [specific feedback]
   ```

5. **Role assignment** — Give AI a persona for better domain results
   ```
   Act as a senior data engineer reviewing this pipeline config.
   What issues do you see? What would you change?
   ```

**Important:** Show the messy version. Show a bad prompt, show why it fails, then show how to fix it. Participants need to see the iteration, not just the polished result.

### Practice (25 min)

Participants work in pairs or small groups:

1. Each person picks a task from their work
2. Write a prompt using one of the patterns above
3. Run it in Claude
4. Share results with their partner — what worked, what didn't
5. Iterate and try again

Instructor circulates and helps.

### Debrief (5 min)
- Quick round: one thing that surprised you
- Preview of Session 2

## Async Challenge

### The Task

Pick a real task from your work this week. It should be something that takes you 30-60 minutes normally.

1. **Plan your approach** — Before prompting, write down what you want AI to help with and what you'll do yourself
2. **Use at least 2 prompting patterns** from today's session
3. **Document your process** — Screenshots or copy/paste of your prompts and AI responses
4. **Reflect** — Write 3-5 sentences: What worked? What would you do differently?

### Share

Post your reflection in the community space with the tag `#session1`. Include at least one prompt that worked well and one that didn't.

## Resources

- [Anthropic's Prompt Engineering Guide](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview)
- [OpenAI's Prompt Engineering Guide](https://platform.openai.com/docs/guides/prompt-engineering)
- [Google's Prompting Strategies](https://ai.google.dev/gemini-api/docs/prompting-strategies)

## Talking Points / Slide Content

### Slide 1: The AI Integration Spectrum
*Visual: horizontal bar from "AI as search" → "AI as autonomous agent"*
Most professionals are on the left. This program moves you to the right.

### Slide 2: The Trust-but-Verify Framework
*Visual: cycle diagram — Prompt → Review → Refine → Use*
Never ship the first response. Always review. Iterate at least once.

### Slide 3: When AI Helps vs. Hurts
*Visual: 2-column table*
Left: Repetitive, boilerplate, exploration, debugging
Right: Novel reasoning, sensitive decisions, deep domain expertise

### Slide 4: Prompting Patterns
*Visual: 5 cards, one per pattern*
Structured | Chain-of-thought | Few-shot | Iterative | Role assignment

---

**Previous:** [Session 0 — Pre-Work](../session-00-prework/)
**Next:** [Session 2 — Building With AI](../session-02-building/)
