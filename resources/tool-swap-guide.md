# Tool Swap Guide

If you're forking this program for your own cohort, you can substitute the default tools without rewriting sessions. This guide shows what to change.

## Data Engineering Track

| Current Tool | Alternatives | What to Change |
|-------------|-------------|----------------|
| **Claude / Claude Code** | GPT-4 + Copilot, Gemini, Cursor AI | Update prompts in session demos. Core patterns (describe, review, test, iterate) stay the same. |
| **Python** | No direct swap — Python is the lingua franca of DE | N/A |
| **SQL** | No direct swap | N/A |
| **Terraform** | Pulumi, CloudFormation, OpenTofu | Rewrite Session 3 demos and the `safe-terraform/` example. Concepts (IaC review, security audit) transfer directly. |
| **GCP / BigQuery** | AWS (S3 + Redshift/Athena), Azure (Blob + Synapse) | Update Session 0 setup instructions, Session 3 Terraform configs, and resource references. Free tier availability varies. |
| **BigQuery** | Snowflake, DuckDB, PostgreSQL | Update SQL dialect in examples. DuckDB is a good zero-cost option for local development. |
| **GitHub** | GitLab, Bitbucket | Update CI/CD template (`github-actions-test.yml`). Version control concepts are identical. |
| **GitHub Actions** | GitLab CI, CircleCI, Jenkins | Rewrite the CI template in Session 5. The "add CI to your pipeline" exercise stays the same. |
| **Discord** | Slack, Teams, forum | Update community references. No curriculum changes needed. |

## Builder Track

| Current Tool | Alternatives | What to Change |
|-------------|-------------|----------------|
| **Claude / Claude Code** | GPT-4 + Copilot, Cursor AI, Gemini | Update prompts in demos. |
| **Vercel / Railway** | Netlify, Render, Fly.io | Update deployment instructions. Concepts stay the same. |
| **GitHub** | GitLab, Bitbucket | Update repo and CI references. |

## General Notes

- **AI assistant swaps are the easiest.** The sessions teach patterns (describe, review, iterate), not Claude-specific features. Change the tool name and update example prompts.
- **Cloud provider swaps require the most work.** Free tier resources, setup instructions, and Terraform configs all need updating.
- **Keep one AI tool as primary.** Mixing tools confuses participants. Pick one and use it consistently.
- **Test your swap end-to-end** before running a cohort. Run through Sessions 0-5 with the new tools to find gaps.
