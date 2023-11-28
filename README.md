# Scrapy-Boilerplate V2

This is a boilerplate for new Scrapy projects.

## Feature
* Python 3.11+
* [Poetry](#https://python-poetry.org/) for dependency management
* Single file for each class
* Linters and formatters for codestyle consistency (see [here](#linters-and-formatters)).
* Pytest (see [here](#pytest))
* Docker-ready (see [here](#docker))

## Installation

Toe create a new project using this boilerplate, you need to:

### Clone repository 
```bash
git clone https://gitlab.groupbwt.com/polos-ss/scrapy-boilerplate-v2.git
```

### Change into the project directory
```bash
cd scrapy-boilerplate-v2
```

### Configuration

The project configuration can be found in the settings.py file. Modify the settings as needed, including but not limited to:
* User-Agent and other HTTP request headers
* Middleware
* Pipelines
* Concurrency and throttling settings
* Log settings

## Usage

### Linters and formatters
In this project, we utilize [Ruff](#https://docs.astral.sh/ruff/) as the primary linter and code formatter and [Mypy](#https://mypy.readthedocs.io/en/stable/) how static type checker. 
Ruff aids in maintaining a unified coding standard, promoting code readability, and ensuring code structure.

The fundamental rules for formatting and style are documented in the `pyproject.toml` file. It's recommended to review this file to familiarize
yourself with the adopted standards for maintaining consistency across the project's codebase.

To ensure compliance with the established standards, scripts are provided that can be executed to initiate the code style checking process, these scripts are in `scripts/format.sh` and `scripts/lint.sh`. 

### Pytest
In this project, we employ pytest as our primary testing framework. Pytest is a feature-rich and easy-to-use testing tool that allows for efficient and comprehensive testing of Python code.

All tests and fixtures are organized within the tests directory. This directory serves as the centralized location for all test-related code, promoting a clean and organized test structure.

### Docker
The project includes Dockerfiles and docker-compose configuration for running your spiders in containers.

To manage project, you need to build a docker container, for this:
```bash
docker-compose up scrapy-boilerplate-v2 -d  --build
```

For get list running compose projects, run command:
```bash
docker-compose ls
```

For get list running process in docker container, run command:
```bash
docker-compose top scrapy-boilerplate-v2
```

Connect to docker container
```bash
docker compose exec scrapy-boilerplate-v2 bash
```
