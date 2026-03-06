# GCP Troubleshooting Guide

The top 5 issues participants encounter when setting up GCP, and how to fix them.

---

## 1. "gcloud: command not found"

The Google Cloud CLI is not installed or not on your PATH.

**Fix by OS:**

- **macOS:** Install via Homebrew or the official installer.
  ```bash
  brew install --cask google-cloud-sdk
  ```
  Or download from https://cloud.google.com/sdk/docs/install#mac and run the install script.

- **Linux (Debian/Ubuntu):**
  ```bash
  sudo apt-get update && sudo apt-get install -y google-cloud-cli
  ```
  Or follow https://cloud.google.com/sdk/docs/install#linux.

- **Windows:** Download the installer from https://cloud.google.com/sdk/docs/install#windows and run it.

After installation, restart your terminal and verify:

```bash
gcloud --version
```

---

## 2. "Not authenticated" / "No active account"

You have gcloud installed but have not logged in.

**Fix:**

```bash
# Log in with your Google account (opens a browser)
gcloud auth login

# Also set up Application Default Credentials (used by Terraform and Python client libraries)
gcloud auth application-default login
```

Verify you are authenticated:

```bash
gcloud auth list
```

You should see your email with `ACTIVE` next to it.

---

## 3. "Project not set" / "(unset)"

gcloud does not know which GCP project to operate on.

**Fix:**

```bash
gcloud config set project YOUR_PROJECT_ID
```

Replace `YOUR_PROJECT_ID` with your actual project ID (not the project name). You can find it in the GCP Console at https://console.cloud.google.com or by running:

```bash
gcloud projects list
```

Verify:

```bash
gcloud config get-value project
```

---

## 4. "BigQuery API not enabled" / "API has not been used in project"

The BigQuery API is disabled by default on new projects.

**Fix:**

```bash
gcloud services enable bigquery.googleapis.com
```

This takes a few seconds. Verify it is enabled:

```bash
gcloud services list --enabled | grep bigquery
```

You should see `bigquery.googleapis.com` in the output.

---

## 5. "Permission denied" / "403 Forbidden"

Your account or service account lacks the necessary permissions.

**Checklist:**

1. **Are you in the right project?** Double-check with `gcloud config get-value project`. A common mistake is having the wrong project selected.

2. **Is billing enabled?** Some APIs (including BigQuery beyond the sandbox) require a billing account. Check at: https://console.cloud.google.com/billing

3. **Do you have the right role?** For the capstone, your Google account should have at least `Editor` or `Owner` on the project. Check your roles at: https://console.cloud.google.com/iam-admin/iam

4. **Service account permissions:** If your pipeline service account gets a permission error, make sure it has been granted the required roles. The safe-terraform template grants `roles/bigquery.dataEditor` and `roles/storage.objectAdmin` automatically.

5. **Org-level restrictions:** If you are using a company or university GCP account, organizational policies may restrict what you can do. Consider using a personal Google account with a free-tier project instead.
