#!/bin/bash
# =============================================================================
# Session 0 Pre-Flight Check
# =============================================================================
# Run this after completing the Session 0 pre-work to verify everything is
# ready before Session 1.
#
# Usage: bash resources/session0-preflight.sh
# =============================================================================

# --- Colors ---
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BOLD='\033[1m'
NC='\033[0m'

PASS_COUNT=0
FAIL_COUNT=0
WARN_COUNT=0
TOTAL_CHECKS=8

pass() {
  echo -e "  ${GREEN}PASS${NC}  $1"
  PASS_COUNT=$((PASS_COUNT + 1))
}

fail() {
  echo -e "  ${RED}FAIL${NC}  $1"
  FAIL_COUNT=$((FAIL_COUNT + 1))
}

warn() {
  echo -e "  ${YELLOW}WARN${NC}  $1"
  WARN_COUNT=$((WARN_COUNT + 1))
}

echo ""
echo -e "${BOLD}Session 0 Pre-Flight Check${NC}"
echo "=============================================="
echo ""

# ---- Check 1: Python version ----
echo -e "${BOLD}[1/8] Python 3.9+${NC}"
if command -v python3 &> /dev/null; then
  PY_VERSION=$(python3 --version 2>/dev/null)
  PY_MINOR=$(python3 -c "import sys; print(sys.version_info.minor)" 2>/dev/null)
  if [ "$PY_MINOR" -ge 9 ] 2>/dev/null; then
    pass "$PY_VERSION"
  else
    fail "$PY_VERSION — need Python 3.9 or higher"
  fi
else
  fail "python3 not found. Install from https://python.org/downloads/"
fi

# ---- Check 2: pip works ----
echo -e "${BOLD}[2/8] pip works${NC}"
if python3 -m pip --version &> /dev/null; then
  PIP_VERSION=$(python3 -m pip --version 2>/dev/null | head -n 1)
  pass "$PIP_VERSION"
else
  fail "pip not found. Run: python3 -m ensurepip --upgrade"
fi

# ---- Check 3: git installed ----
echo -e "${BOLD}[3/8] Git installed${NC}"
if command -v git &> /dev/null; then
  GIT_VERSION=$(git --version 2>/dev/null)
  pass "$GIT_VERSION"
else
  fail "Git not found. Install from https://git-scm.com/downloads"
fi

# ---- Check 4: GitHub access ----
echo -e "${BOLD}[4/8] GitHub access${NC}"
if command -v git &> /dev/null; then
  # Try HTTPS first (works for most setups)
  if git ls-remote https://github.com/anmolp1/learn-ai.git HEAD &> /dev/null; then
    pass "Can reach GitHub (HTTPS)"
  elif ssh -T git@github.com 2>&1 | grep -q "successfully authenticated"; then
    pass "Can reach GitHub (SSH)"
  else
    fail "Cannot reach GitHub. Check your internet connection and git credentials."
  fi
else
  fail "Skipped (git not installed)"
fi

# ---- Check 5: gcloud CLI installed ----
echo -e "${BOLD}[5/8] gcloud CLI installed${NC}"
if command -v gcloud &> /dev/null; then
  GCLOUD_VERSION=$(gcloud --version 2>/dev/null | head -n 1)
  pass "$GCLOUD_VERSION"
else
  fail "gcloud CLI not found. Install from https://cloud.google.com/sdk/docs/install"
fi

# ---- Check 6: gcloud authenticated + project set ----
echo -e "${BOLD}[6/8] GCP authenticated and project set${NC}"
if command -v gcloud &> /dev/null; then
  AUTH_ACCOUNT=$(gcloud auth list --filter="status:ACTIVE" --format="value(account)" 2>/dev/null)
  PROJECT_ID=$(gcloud config get-value project 2>/dev/null)
  if [ -n "$AUTH_ACCOUNT" ] && [ -n "$PROJECT_ID" ] && [ "$PROJECT_ID" != "(unset)" ]; then
    pass "Authenticated as $AUTH_ACCOUNT, project: $PROJECT_ID"
  elif [ -z "$AUTH_ACCOUNT" ]; then
    fail "Not authenticated. Run: gcloud auth login"
  else
    fail "No project set. Run: gcloud config set project YOUR_PROJECT_ID"
  fi
else
  fail "Skipped (gcloud not installed)"
fi

# ---- Check 7: Terraform installed ----
echo -e "${BOLD}[7/8] Terraform installed${NC}"
if command -v terraform &> /dev/null; then
  TF_VERSION=$(terraform --version 2>/dev/null | head -n 1)
  pass "$TF_VERSION"
else
  warn "Terraform not found — not needed until Session 3. Install from https://developer.hashicorp.com/terraform/install"
fi

# ---- Check 8: Anthropic API key set ----
echo -e "${BOLD}[8/8] Anthropic API key${NC}"
if [ -n "$ANTHROPIC_API_KEY" ]; then
  # Mask the key for display
  KEY_PREFIX=$(echo "$ANTHROPIC_API_KEY" | cut -c1-10)
  pass "ANTHROPIC_API_KEY is set (${KEY_PREFIX}...)"
else
  warn "ANTHROPIC_API_KEY not set — not needed until Session 4. See resources/claude-api-quickstart.md"
fi

# ---- Summary ----
echo ""
echo "=============================================="

# Adjust total for warnings (they don't count as failures)
CHECKED=$((PASS_COUNT + FAIL_COUNT + WARN_COUNT))
echo -e "${BOLD}Results: ${GREEN}${PASS_COUNT} passed${NC}, ${RED}${FAIL_COUNT} failed${NC}, ${YELLOW}${WARN_COUNT} warnings${NC} out of ${CHECKED} checks"
echo ""

if [ "$FAIL_COUNT" -gt 0 ]; then
  echo -e "${YELLOW}Some checks failed. Fix the issues above before Session 1.${NC}"
  echo "See the Session 0 pre-work README for setup instructions."
  echo ""
  exit 1
elif [ "$WARN_COUNT" -gt 0 ]; then
  echo -e "${GREEN}Core checks passed.${NC} Warnings are for tools needed in later sessions — you can fix those later."
  echo ""
  exit 0
else
  echo -e "${GREEN}All checks passed! You are ready for Session 1.${NC}"
  echo ""
  exit 0
fi
