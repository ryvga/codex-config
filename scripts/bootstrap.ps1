$ErrorActionPreference = "Stop"
Set-Location (Join-Path $PSScriptRoot "..")
python scripts/bootstrap.py
python scripts/validate_repo.py

