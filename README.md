# Scrapy-Boilerplate V2

This is a boilerplate for new Scrapy projects.

## Feature
* Python 3.11+
* [Poetry](#https://python-poetry.org/) for dependency management
* Single file for each class
* Linters and formatters for codestyle consistency.
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
