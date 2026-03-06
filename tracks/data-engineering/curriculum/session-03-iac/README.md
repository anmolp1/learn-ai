# Session 3: Infrastructure-as-Code — Terraform + AI

**Format:** 90 min live + async challenge
**Goal:** Deploy your pipeline's infrastructure to GCP using AI-generated Terraform

## Session Plan

### Pre-Flight Check (5 min)
Run the pre-flight script to make sure your GCP setup is ready:
```bash
bash ../../resources/session3-preflight.sh
```
All checks should pass. If any fail, see [GCP Troubleshooting](../../resources/gcp-troubleshooting.md).

### Concept (10 min): Why IaC + AI Is a Force Multiplier

Terraform is powerful but verbose. A simple GCS bucket + BigQuery dataset + IAM setup can be 200+ lines of HCL. This is exactly where AI shines — generating correct, well-structured config from a natural language description.

The workflow:
1. Describe your infrastructure needs in plain English
2. AI generates Terraform configs
3. You review for security, cost, and correctness
4. `terraform plan` — verify before you apply
5. `terraform apply` — deploy with confidence

Why this matters: most data engineers know they *should* use Terraform but avoid it because the learning curve is steep. AI flattens that curve dramatically.

### Demo (35 min): Deploy a Full Data Infrastructure

**Build and deploy live.** Target infrastructure:

**Step 1 — GCS Bucket for Raw Data (8 min)**
```
Prompt: Generate Terraform for a GCS bucket with:
- Name: {project}-raw-data
- Region: us-central1
- Standard storage class
- 90-day lifecycle deletion
- Versioning enabled
- Uniform bucket-level access (no ACLs)
- Block all public access
- Labels: environment=dev, managed_by=terraform
Include a variables.tf with project_id and region as variables.
```

Review the output. Show what to check: IAM, public access, lifecycle rules.

**Step 2 — BigQuery Dataset + Tables (8 min)**
Use Claude to generate:
- A BigQuery dataset
- 2-3 tables matching the pipeline's output schema
- Partitioning and clustering config
- Table-level descriptions

Show how to give Claude your data schema and get back correct Terraform.

**Step 3 — Service Account + IAM (8 min)**
Use Claude to generate:
- A service account for the pipeline
- Minimal IAM roles (principle of least privilege)
- Key rotation considerations

This is where AI needs the most scrutiny — IAM misconfigurations are the #1 security issue in cloud. Reference the [GCP IAM Cheat Sheet](../../resources/gcp-iam-cheatsheet.md) during this review.

**Step 4 — Plan and Apply (11 min)**
- Run `terraform init` and `terraform plan`
- Review the plan output together
- Apply (to a dev/sandbox project)
- Verify resources exist in GCP console

Show the full cycle: prompt → generate → review → plan → apply → verify.

### Practice (25 min)

> **Choose your path based on your experience level:**
>
> **If this is new to you** — Start from the [safe Terraform template](../../examples/safe-terraform/). Read through each file, use AI to explain what each block does, then customize the bucket name and dataset for your capstone.
>
> **If you're experienced** — Write your Terraform from scratch. Add modules, remote state, or multi-environment configs. Use AI to generate and then audit for security issues.

Participants write Terraform for their capstone project's infrastructure:
- At minimum: a storage bucket and a BigQuery dataset
- Use AI to generate, then review and customize
- Run `terraform plan` (don't need to apply yet)

### Debrief (15 min)
- What did AI get right/wrong in the Terraform?
- Security concerns found during review
- Tips for reviewing AI-generated IaC

## Async Challenge

### Task
Deploy your capstone project's infrastructure:

1. **Write Terraform configs** for all resources your pipeline needs. Start from the [safe Terraform template](../../examples/safe-terraform/) which includes only free-tier resources.
2. **Organize properly:** `main.tf`, `variables.tf`, `outputs.tf`, `terraform.tfvars.example`
3. **Security review:** Check every IAM binding, every public access setting, every network config
4. **Deploy to GCP** (free tier resources only — don't accidentally spin up expensive infra)
5. **Document:** Add a `infrastructure/` section to your README explaining what resources exist and why

### Checklist
- [ ] `terraform plan` runs clean with no errors
- [ ] No public access on storage buckets
- [ ] Service account uses minimal IAM roles
- [ ] No hardcoded credentials or project IDs in .tf files
- [ ] `.tfvars` file is in `.gitignore`
- [ ] Infrastructure section added to README

### Before You `terraform apply`
Review this checklist (especially if this is your first time):
- [ ] No Compute Engine instances (these cost money)
- [ ] No Cloud SQL instances (these cost money)
- [ ] No public access on any resource
- [ ] Service account has minimal roles (not roles/owner or roles/editor)
- [ ] If you're unsure about costs, share your `terraform plan` output with the trainer before applying

**Cost Check:** Before you wrap up, open your [GCP Billing Dashboard](https://console.cloud.google.com/billing) and note your current spend in your learning journal. You should be at $0 or very close if you're using free-tier resources only.

Push to GitHub, share in community with `#de-session3`.

> **Falling behind?** Copy the [starter pipeline](../../examples/starter-pipeline/) and [safe Terraform template](../../examples/safe-terraform/) into your capstone repo. See [Checkpoints](../../resources/checkpoints.md) for details. Customize with your own data source.

## Key Concepts

### The Terraform + AI Security Checklist
Always review AI-generated Terraform for:
1. **Public access:** Is anything exposed to the internet that shouldn't be?
2. **IAM roles:** Are roles scoped to minimum necessary? (No `roles/owner` or `roles/editor`)
3. **Credentials:** Are any secrets hardcoded? Are .tfvars files gitignored?
4. **Cost:** Are resource sizes/tiers appropriate? (AI defaults to reasonable but not always cheapest)
5. **Naming:** Are resources named consistently and meaningfully?
6. **State:** Is Terraform state stored securely? (Remote backend, not local)

### Common AI Mistakes in Terraform
- Over-permissive IAM roles (defaults to broader access than needed)
- Missing lifecycle rules on storage
- Forgetting to set `prevent_destroy` on critical resources
- Using deprecated resource types or argument names
- Not parameterizing values that should be variables

---

**Previous:** [Session 2 — Pipelines](../session-02-pipelines/)
**Next:** [Session 4 — Agents: Monitoring, Alerts, and Automation](../session-04-agents/)
