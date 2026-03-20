#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."
python3 scripts/bootstrap.py
python3 scripts/validate_repo.py

