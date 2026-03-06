# Session 5: Quality — Testing, Security, and Reliability

**Format:** 90 min live + async challenge
**Goal:** Make your AI-built pipeline production-ready

## Session Plan

### Concept (15 min): The Production Readiness Bar

A pipeline that works on your laptop is a prototype. A pipeline that's production-ready has: tests that catch regressions before they reach production, security controls that prevent data leaks and unauthorized access, reliability features that handle failures gracefully, and documentation that lets someone else operate it.

AI can help build all of this — but AI-generated infrastructure and pipeline code needs *more* scrutiny, not less.

### Demo (35 min): Live Production Readiness Review

**Take a participant's capstone project and do a live audit.**

**1. Testing Audit (10 min)**
Use Claude to:
- Generate unit tests for transformation functions
- Generate integration tests that run against test data
- Identify edge cases the participant missed
- Create a test data fixture with realistic edge cases

```
Prompt: Here's my pipeline's transformation code:
[paste code]

Generate comprehensive tests including:
- Happy path with normal data
- Null handling
- Duplicate records
- Schema edge cases (empty strings, max-length values)
- Boundary conditions for numeric fields
- Date edge cases (timezones, leap years, epoch)
```

**2. Security Audit (10 min)**
Review for:
- Hardcoded credentials (API keys, service account keys)
- Overly permissive IAM roles in Terraform
- Public access on storage or datasets
- SQL injection vectors (if pipeline accepts user input)
- Secrets management (are they in env vars, Secret Manager, or committed to git?)
- Data encryption (at rest and in transit)

Use Claude to scan the codebase:
```
Review this Terraform config and Python pipeline code for security issues.
Focus on: credentials exposure, IAM permissions, network access, data encryption.
[paste code]
```

**3. Reliability Review (10 min)**
Check for:
- Error handling: what happens when the API is down? When BigQuery is slow? When data is malformed?
- Retries with backoff
- Idempotency: can you re-run the pipeline safely?
- Logging: can you debug a failure from logs alone?
- Alerting: will you know when something breaks?

**4. Fix Together (5 min)**
Pick 2-3 issues found and fix them live, using AI to help write the fixes.

### Practice (25 min)
Participants audit their own capstone projects using the checklist below.
Then: swap repos with a partner and review each other's work.

### Debrief (15 min)
- What surprised you? What did you miss?
- Group discussion: what's the minimum quality bar for a data pipeline?

## Async Challenge

### Task
Make your capstone production-ready:

1. **Add tests:** Unit tests for transformations, integration test for the full pipeline
2. **Security fix:** Address any credential, IAM, or access issues
3. **Reliability:** Add error handling, retries, and logging
4. **CI/CD:** Add a GitHub Action that runs tests on every push
5. **Final documentation:** Complete README with setup, run, test, and operate instructions

### Production Readiness Checklist
- [ ] All transformation logic has unit tests
- [ ] Pipeline has at least one integration test
- [ ] No credentials in code or git history
- [ ] Terraform uses least-privilege IAM
- [ ] No public access on data resources
- [ ] Error handling on all external calls (APIs, databases)
- [ ] Retry logic with backoff on transient failures
- [ ] Pipeline is idempotent (safe to re-run)
- [ ] Meaningful logging at key pipeline stages
- [ ] Monitoring/alerting for pipeline failures
- [ ] README covers: what, why, setup, run, test, monitor, troubleshoot
- [ ] GitHub Actions run tests on push

Push final version to GitHub, share in community with `#de-session5`.

---

**Previous:** [Session 4 — Agents](../session-04-agents/)
**Next:** [Session 6 — Ship It: Demo Day](../session-06-ship-it/)
