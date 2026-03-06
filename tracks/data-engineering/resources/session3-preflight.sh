#!/bin/bash
# =============================================================================
# Session 3 Pre-Flight Check
# =============================================================================
# Run this script before Session 3 to verify your GCP environment is ready.
# Usage: bash resources/session3-preflight.sh
# =============================================================================

set -euo pipefail

# --- Colors ---
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BOLD='\033[1m'
NC='\033[0m' # No Color

PASS_COUNT=0
FAIL_COUNT=0
TOTAL_CHECKS=6

pass() {
  echo -e "  ${GREEN}PASS${NC}  $1"
  PASS_COUNT=$((PASS_COUNT + 1))
}

fail() {
  echo -e "  ${RED}FAIL${NC}  $1"
  FAIL_COUNT=$((FAIL_COUNT + 1))
}

echo ""
echo -e "${BOLD}Session 3 Pre-Flight Check${NC}"
echo "=============================================="
echo ""

# ---- Check 1: gcloud CLI installed ----
echo -e "${BOLD}[1/6] gcloud CLI installed${NC}"
if command -v gcloud &> /dev/null; then
  GCLOUD_VERSION=$(gcloud --version 2>/dev/null | head -n 1)
  pass "$GCLOUD_VERSION"
else
  fail "gcloud CLI not found. Install it from https://cloud.google.com/sdk/docs/install"
fi

# ---- Check 2: gcloud authenticated ----
echo -e "${BOLD}[2/6] gcloud authenticated${NC}"
if command -v gcloud &> /dev/null; then
  AUTH_ACCOUNT=$(gcloud auth list --filter="status:ACTIVE" --format="value(account)" 2>/dev/null)
  if [ -n "$AUTH_ACCOUNT" ]; then
    pass "Authenticated as $AUTH_ACCOUNT"
  else
    fail "No active gcloud account. Run: gcloud auth login"
  fi
else
  fail "Skipped (gcloud not installed)"
fi

# ---- Check 3: GCP project set ----
echo -e "${BOLD}[3/6] GCP project set${NC}"
if command -v gcloud &> /dev/null; then
  PROJECT_ID=$(gcloud config get-value project 2>/dev/null)
  if [ -n "$PROJECT_ID" ] && [ "$PROJECT_ID" != "(unset)" ]; then
    pass "Project is set to: $PROJECT_ID"
  else
    fail "No project set. Run: gcloud config set project YOUR_PROJECT_ID"
  fi
else
  fail "Skipped (gcloud not installed)"
fi

# ---- Check 4: BigQuery API enabled ----
echo -e "${BOLD}[4/6] BigQuery API enabled${NC}"
if command -v gcloud &> /dev/null; then
  BQ_ENABLED=$(gcloud services list --enabled --format="value(config.name)" 2>/dev/null | grep -c "bigquery" || true)
  if [ "$BQ_ENABLED" -gt 0 ]; then
    pass "BigQuery API is enabled"
  else
    fail "BigQuery API not enabled. Run: gcloud services enable bigquery.googleapis.com"
  fi
else
  fail "Skipped (gcloud not installed)"
fi

# ---- Check 5: Application Default Credentials ----
echo -e "${BOLD}[5/6] Application Default Credentials${NC}"
if command -v gcloud &> /dev/null; then
  if gcloud auth application-default print-access-token &> /dev/null; then
    pass "Application Default Credentials are configured"
  else
    fail "ADC not set. Run: gcloud auth application-default login"
  fi
else
  fail "Skipped (gcloud not installed)"
fi

# ---- Check 6: Terraform installed ----
echo -e "${BOLD}[6/6] Terraform installed${NC}"
if command -v terraform &> /dev/null; then
  TF_VERSION=$(terraform --version 2>/dev/null | head -n 1)
  pass "$TF_VERSION"
else
  fail "Terraform not found. Install it from https://developer.hashicorp.com/terraform/install"
fi

# ---- Summary ----
echo ""
echo "=============================================="
echo -e "${BOLD}Results: ${GREEN}${PASS_COUNT} passed${NC}, ${RED}${FAIL_COUNT} failed${NC} out of ${TOTAL_CHECKS} checks"
echo ""

if [ "$FAIL_COUNT" -gt 0 ]; then
  echo -e "${YELLOW}Some checks failed. See resources/gcp-troubleshooting.md for detailed fix instructions.${NC}"
  echo ""
  exit 1
else
  echo -e "${GREEN}All checks passed! You are ready for Session 3.${NC}"
  echo ""
  exit 0
fi
