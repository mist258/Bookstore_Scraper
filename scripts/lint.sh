#!/bin/bash

set -e
set -x

echo "mypy check:"
cd src && mypy --namespace-packages --explicit-package-bases .
cd ..
echo "ruff linter check:"
ruff check src tests
echo "ruff formatter check:"
ruff format --check src tests
