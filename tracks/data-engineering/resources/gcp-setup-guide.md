# GCP Setup Guide for Beginners

This guide walks you through setting up Google Cloud Platform (GCP) for use with BigQuery in this program. Follow each step carefully — most setup issues come from skipping a step.

---

## Step 1: Create a Google Cloud Project

1. Go to [console.cloud.google.com](https://console.cloud.google.com/).
2. Sign in with your Google account (a personal Gmail works fine).
3. Click the project dropdown at the top of the page (it may say "Select a project").
4. Click **New Project**.
5. Enter a project name, e.g., `learn-ai-data-eng`.
6. Leave the organization as "No organization" (unless your company requires otherwise).
7. Click **Create**.
8. **Important:** After creation, make sure this new project is selected in the project dropdown at the top. The project name should be visible in the header bar.

## Step 2: Enable the BigQuery API

1. With your new project selected, go to **APIs & Services > Library** in the left sidebar (or search "BigQuery API" in the top search bar).
2. Search for **BigQuery API**.
3. Click on it, then click **Enable**.
4. Wait for the confirmation message. This usually takes a few seconds.

> **Note:** BigQuery has a generous free tier — 1 TB of query processing and 10 GB of storage per month. You will not come close to these limits in this program.

## Step 3: Set Up a Budget Alert ($10)

This is a safety net. You are unlikely to incur any charges, but setting a budget alert is good practice.

1. Go to **Billing** in the left sidebar of the Cloud Console.
2. If you do not have a billing account, you will be prompted to create one. Follow the prompts to add a payment method. (Google Cloud offers a free trial with $300 in credits for new accounts.)
3. Once billing is set up, go to **Billing > Budgets & alerts**.
4. Click **Create Budget**.
5. Set the budget amount to **$10**.
6. Under alert thresholds, keep the defaults (50%, 90%, 100%) or add a threshold at 25% for extra caution.
7. Make sure your email is listed under notification recipients.
8. Click **Finish**.

## Step 4: Install the gcloud CLI

The `gcloud` CLI lets you interact with GCP from your terminal.

### macOS

```bash
# Using Homebrew (recommended)
brew install --cask google-cloud-sdk

# After installation, restart your terminal or run:
source "$(brew --prefix)/share/google-cloud-sdk/path.zsh.inc"
source "$(brew --prefix)/share/google-cloud-sdk/completion.zsh.inc"
```

### Windows

Download the installer from: https://cloud.google.com/sdk/docs/install

Run the installer and follow the prompts. Make sure to check the option to add gcloud to your PATH.

### Linux

```bash
curl https://sdk.cloud.google.com | bash
exec -l $SHELL  # Restart your shell
```

### Verify installation

```bash
gcloud --version
```

You should see output like `Google Cloud SDK 4xx.x.x`.

## Step 5: Authenticate with GCP

```bash
# Log in to your Google account
gcloud auth login
```

A browser window will open. Sign in with the same Google account you used in Step 1.

Then set your default project:

```bash
# Replace with your actual project ID (not the display name)
gcloud config set project YOUR_PROJECT_ID
```

To find your project ID, run:

```bash
gcloud projects list
```

Finally, set up Application Default Credentials (ADC). This is what Python libraries use to authenticate:

```bash
gcloud auth application-default login
```

Again, a browser window will open. Approve the request.

## Step 6: Verify with a Test Query

Run this from your terminal to confirm everything works:

```bash
bq query --use_legacy_sql=false 'SELECT "Hello BigQuery!" AS greeting'
```

Expected output:

```
+------------------+
|     greeting     |
+------------------+
| Hello BigQuery!  |
+------------------+
```

You can also verify from Python:

```python
from google.cloud import bigquery

client = bigquery.Client()
query = "SELECT 'Connected successfully!' AS status"
result = client.query(query).result()
for row in result:
    print(row.status)
```

If you see `Connected successfully!`, your setup is complete.

---

## Troubleshooting

### Issue 1: Billing Account Stuck / Cannot Enable Billing

**Symptoms:** You see "Billing account is not active" or the Enable Billing button does not work.

**Fix:**
- Go to [billing accounts](https://console.cloud.google.com/billing) directly.
- Check that your payment method was verified. Sometimes a bank will block the initial authorization hold.
- If using a new Google account, you may need to wait 15-30 minutes for the free trial to activate.
- Try a different browser or incognito mode if the page is unresponsive.

### Issue 2: Wrong Project Selected

**Symptoms:** "Permission denied" errors, or you cannot find resources you just created.

**Fix:**
- Check your current project: `gcloud config get-value project`
- List available projects: `gcloud projects list`
- Switch to the correct one: `gcloud config set project YOUR_PROJECT_ID`
- In the Cloud Console, always verify the project dropdown in the top bar shows the correct project.

### Issue 3: BigQuery API Not Enabled

**Symptoms:** Errors like `BigQuery API has not been used in project XXXXX before or it is disabled.`

**Fix:**
- Enable it from the CLI: `gcloud services enable bigquery.googleapis.com`
- Or go to APIs & Services > Library in the console, search BigQuery API, and click Enable.
- After enabling, wait 1-2 minutes before retrying your query.

### Issue 4: Authentication Failure

**Symptoms:** `google.auth.exceptions.DefaultCredentialsError` or `Could not automatically determine credentials`.

**Fix:**
- Re-run `gcloud auth application-default login` (this is the most common fix).
- Check that the `GOOGLE_APPLICATION_CREDENTIALS` environment variable is not set to a stale service account key: `echo $GOOGLE_APPLICATION_CREDENTIALS`. If it is set and you are not using a service account, unset it: `unset GOOGLE_APPLICATION_CREDENTIALS`.
- Verify your login: `gcloud auth list` — your account should have an asterisk (*) next to it.

### Issue 5: M1/M2 Mac Compatibility

**Symptoms:** `ImportError` for grpcio, installation fails for `google-cloud-bigquery`, or `pip install` hangs.

**Fix:**
- Make sure you are using Python 3.9+ (check with `python3 --version`).
- Install/upgrade pip: `python3 -m pip install --upgrade pip`
- If grpcio fails, install it separately first:
  ```bash
  pip install grpcio --no-binary :all:
  ```
  Or, if that takes too long:
  ```bash
  GRPC_PYTHON_BUILD_SYSTEM_OPENSSL=1 GRPC_PYTHON_BUILD_SYSTEM_ZLIB=1 pip install grpcio
  ```
- If using Homebrew Python, ensure your shell path resolves to the Homebrew version, not the macOS system Python:
  ```bash
  which python3
  # Should show /opt/homebrew/bin/python3 on Apple Silicon
  ```
- As a last resort, use a Conda environment which ships pre-built binaries:
  ```bash
  conda create -n learnai python=3.11
  conda activate learnai
  pip install google-cloud-bigquery
  ```
