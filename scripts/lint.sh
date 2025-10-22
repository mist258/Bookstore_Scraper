#!/bin/bash

set -e
set -x
find src -type d -exec touch {}/__init__.py \;

echo "mypy check:"
mypy --namespace-packages --explicit-package-bases src
echo "ruff linter check:"
ruff check src tests
echo "ruff formatter check:"
ruff format --check src tests

