#!/usr/bin/env bash
# Creates ABBYCRM/TFT-SITE (or any org/user) and pushes this repo.
# Usage: ./scripts/publish-github.sh ABBYCRM
set -euo pipefail
ORG="${1:-ABBYCRM}"
REPO="TFT-SITE"
cd "$(dirname "$0")/.."
if ! gh auth status >/dev/null 2>&1; then
  echo "Run: gh auth login"
  exit 1
fi
gh repo create "${ORG}/${REPO}" --public --description "TFT Legal Service — official website" --source=. --remote=origin --push
echo "Live at: https://github.com/${ORG}/${REPO}"
