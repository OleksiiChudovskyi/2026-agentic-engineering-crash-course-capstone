#!/usr/bin/env sh
# Run lint, format check and tests in order; the first failure stops the script.
set -e

uv run ruff check app
uv run ruff format --check app
uv run pytest
