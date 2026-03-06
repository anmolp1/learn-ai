# GCP IAM Cheat Sheet

## What Is IAM?

IAM (Identity and Access Management) controls **who** can do **what** on **which** GCP resources. Every API call to GCP is checked against IAM policies, so understanding roles is essential for both security and getting your pipeline to work.

---

## The 5 Roles You Will Use

| Role | What It Allows | When to Use |
|------|---------------|-------------|
| `roles/bigquery.dataEditor` | Read and write data in BigQuery tables and views. Cannot create or delete datasets. | Grant to your pipeline service account so it can insert rows and update tables. |
| `roles/bigquery.jobUser` | Run BigQuery queries (create jobs). Does not grant access to any data by itself. | Grant to any account that needs to execute SQL queries in BigQuery. |
| `roles/storage.objectAdmin` | Read, write, and delete objects in GCS buckets. Cannot create or delete buckets. | Grant to your pipeline service account so it can upload and manage data files. |
| `roles/iam.serviceAccountUser` | Impersonate (act as) a service account. | Grant when your pipeline or CI/CD needs to run as a service account. |
| `roles/viewer` | Read-only access to all resources in the project. Cannot modify anything. | Grant to teammates or reviewers who need to inspect resources but not change them. |

---

## Red Flags -- Roles and Settings to Avoid

The following are **overly permissive** and should never be used in your capstone (or in production):

- **`roles/owner`** -- Full control over the project including billing and IAM. Only the project creator should have this, and even then it should be used sparingly.
- **`roles/editor`** -- Can modify almost all resources. Far broader than any pipeline needs. Use specific roles instead.
- **`allUsers`** -- Makes a resource publicly accessible to **anyone on the internet**. Never use this for data buckets or datasets.
- **`allAuthenticatedUsers`** -- Makes a resource accessible to **any Google account**. This is nearly as dangerous as `allUsers` because any person with a Gmail address qualifies.

If you see any of these in your Terraform code or IAM console, stop and replace them with a specific, narrow role.

---

## The Principle of Least Privilege

Every account -- whether human or service account -- should have **only the permissions it needs to do its job, and nothing more**. Start with zero permissions and add roles one at a time as needed. If your pipeline only reads from GCS and writes to BigQuery, it should have exactly those two capabilities and no others. This limits the blast radius if credentials are ever leaked or misconfigured, and it makes your system easier to audit and reason about. When in doubt, grant less and add more later.
