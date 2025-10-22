#!/bin/bash

set -e
set -x
export PYTHONPATH="$CI_PROJECT_DIR/src"

echo "mypy check:"
mypy --namespace-packages --explicit-package-bases src
echo "ruff linter check:"
ruff check src tests
echo "ruff formatter check:"
ruff format --check src tests

