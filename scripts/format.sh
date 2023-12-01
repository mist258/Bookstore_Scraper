#!/bin/bash

set -e

black src tests
ruff src tests --fix
ruff format src tests
