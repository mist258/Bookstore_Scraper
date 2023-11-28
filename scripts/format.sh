#!/bin/bash

set -e

ruff src tests --fix
ruff format src tests
