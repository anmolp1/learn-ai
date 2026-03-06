# Session 4: Quality, Security, and Responsible AI Use

**Format:** 90 min live + async challenge
**Prerequisites:** Session 3 complete
**Goal:** Make your AI-integrated work production-ready and trustworthy

## Session Plan

### Concept (20 min): The Trust Layer
- AI-generated output needs the same (or more) scrutiny as human-generated output
- The three pillars: correctness, security, reliability
- Responsible use: bias awareness, data privacy, transparency with stakeholders

### Demo (30 min): Live Audit
Take a participant's capstone project and do a live "AI audit":

1. **Correctness check** — Does the AI-generated code/content actually do what it claims?
2. **Security review** — Are there vulnerabilities? Is sensitive data exposed? Prompt injection risks?
3. **Reliability assessment** — What happens when it fails? Are there fallbacks? Human-in-the-loop?
4. **Fix together** — Address the issues found, showing how AI can help fix its own mistakes

### Topics to Cover
- Testing AI-generated code: unit tests, integration tests, edge cases
- Data privacy: what not to put in prompts, understanding provider data policies
- Prompt injection basics: what it is, why it matters, how to mitigate
- Monitoring AI outputs in production: logging, alerting, drift detection
- When to be transparent about AI use with stakeholders/clients

### Practice (25 min)
- Participants audit their own capstone projects using a provided checklist
- Peer review: swap projects with a partner and review each other's work

### Debrief (15 min)
- What did you find? What surprised you?
- Common patterns across the group

## Async Challenge
- Complete the audit of your capstone project
- Fix any issues identified
- Write a brief "AI transparency note" for your project: what AI was used for, what was human-reviewed
- Push final version to GitHub

## Audit Checklist

- [ ] All AI-generated code has been reviewed line-by-line
- [ ] Tests exist for critical functionality
- [ ] No sensitive data (API keys, passwords, PII) in prompts or code
- [ ] Error handling exists for AI-dependent components
- [ ] A human-in-the-loop step exists for critical decisions
- [ ] README documents what AI tools were used and how
- [ ] Output has been validated against known-good results

---

**Previous:** [Session 3 — Agents and Workflows](../session-03-agents/)
**Next:** [Session 5 — Ship It](../session-05-ship-it/)
