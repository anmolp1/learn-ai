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

> **Choose your path based on your experience level:**
>
> **If this is new to you** — Focus on the Production Readiness Checklist below. Use AI to help generate tests and identify security issues. Getting the must-haves checked off is a solid outcome.
>
> **If you're experienced** — Go deeper: write integration tests, set up CI/CD, and add retry logic. Challenge yourself on the stretch items.

Participants audit their own capstone projects using the checklist below.
Then: swap repos with a partner and review each other's work.

#### Peer Review Protocol

Structured peer review (15 min of practice time):

1. **Swap repos** with a partner — clone their repo locally
2. **Run the checklist** — go through the Production Readiness Checklist on their code, not yours
3. **Open 3 GitHub issues** on their repo, one for each finding. Use labels: `bug`, `security`, or `improvement`
4. **Discuss** — walk through your findings together. What did they miss? What did you learn from their approach?

This mirrors real code review. The goal isn't to find fault — it's to catch what fresh eyes can see.

### Debrief (15 min)
- What surprised you? What did you miss?
- Group discussion: what's the minimum quality bar for a data pipeline?

## Async Challenge

### Task
Make your capstone production-ready:

1. **Add tests:** Unit tests for transformations, integration test for the full pipeline
2. **Security fix:** Address any credential, IAM, or access issues
3. **Reliability:** Add error handling, retries, and logging
4. **CI/CD:** Copy the [GitHub Actions template](../../examples/github-actions-test.yml) into `.github/workflows/test.yml`, commit, push, and verify you see a green checkmark on GitHub
5. **Final documentation:** Complete README with setup, run, test, and operate instructions

### Production Readiness Checklist

**Must-Have (complete all 5):**
- [ ] Pipeline runs end-to-end on sample data without errors
- [ ] At least 3 tests pass (unit or integration)
- [ ] No credentials in code or git history
- [ ] README exists with setup and run instructions
- [ ] You can demo something working

**Stretch (pick your top 3 gaps and fix them):**
- [ ] Integration test for the full pipeline
- [ ] Terraform uses least-privilege IAM (no roles/owner or roles/editor)
- [ ] Retry logic with backoff on transient failures
- [ ] Pipeline is idempotent (safe to re-run)
- [ ] Monitoring/alerting for pipeline failures
- [ ] CI/CD: GitHub Actions run tests on push
- [ ] Meaningful logging at key pipeline stages

**Cost Check:** Final billing review — open your [GCP Billing Dashboard](https://console.cloud.google.com/billing) and note your total program spend in your learning journal. If anything is higher than expected, investigate before Demo Day.

Push final version to GitHub, share in community with `#de-session5`.

> **Falling behind?** Use the [Checkpoints](../../resources/checkpoints.md) to catch up. Copy the examples you need and focus on the quality improvements in this session.

---

**Previous:** [Session 4 — Agents](../session-04-agents/)
**Next:** [Session 6 — Ship It: Demo Day](../session-06-ship-it/)
