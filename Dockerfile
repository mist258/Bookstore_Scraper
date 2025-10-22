ARG PYTHON_IMAGE_VERSION=3.12.4-slim-bullseye
ARG POETRY_HOME='/root/.local/pypoetry'
ARG POETRY_CACHE_DIR='/tmp/poetry_cache'
ARG VIRTUALENV='/app/.venv'

FROM python:${PYTHON_IMAGE_VERSION} AS builder

ARG POETRY_HOME
ARG POETRY_CACHE_DIR
ARG VIRTUALENV

ENV PYTHONUNBUFFERED=1 \

    # prevents python creating .pyc files
    PYTHONDONTWRITEBYTECODE=1 \
    \
    # pip
    PIP_NO_CACHE_DIR=on \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    \
    # poetry
    # https://python-poetry.org/docs/configuration/#using-environment-variables
    POETRY_VERSION=1.7.1 \
    POETRY_HOME=$POETRY_HOME \
    POETRY_CACHE_DIR=$POETRY_CACHE_DIR \
    VIRTUALENV=$VIRTUALENV \
    # make poetry create the virtual environment in the project's root
    # it gets named `.venv`
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    # do not ask any interactive question
    POETRY_NO_INTERACTION=1

RUN apt-get update -yq \
    && apt-get install -yq --no-install-recommends \
        curl \
        gcc \
        g++ \
        python3-dev \
        default-libmysqlclient-dev \
        pkg-config \
        libssl-dev \
        libffi-dev \
        make \
    # installing poetry: https://github.com/python-poetry/poetry \
    && curl -sSL https://install.python-poetry.org | python - \
    # cleaning cache \
    #&& apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*

ENV PATH="$POETRY_HOME/bin:$VIRTUALENV/bin:$PATH"

WORKDIR /app
RUN python -m venv $VIRTUALENV

RUN $VIRTUALENV/bin/pip install --upgrade pip setuptools wheel && \
    $VIRTUALENV/bin/pip install mysqlclient==2.2.4

COPY pyproject.toml poetry.lock /app/

RUN --mount=type=cache,target=$POETRY_CACHE_DIR poetry install --only main --no-root

# 'development' stage installs all dev deps and can be used to develop code.
FROM builder AS development

RUN poetry install --only dev --no-root && rm -rf $POETRY_CACHE_DIR

COPY scripts/ /app/scripts
COPY tests/ /app/tests
COPY src/ /app/src

RUN find /app/src -type d -exec touch {}/__init__.py \;

# `production` image used for runtime (without poetry, only virtualenv)
FROM python:${PYTHON_IMAGE_VERSION} AS production

ARG VIRTUALENV

ENV PATH="$VIRTUALENV/bin:$PATH"

RUN apt-get update -yq \
    && apt-get install -yq --no-install-recommends \
        libmariadb3 \
        mariadb-common \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*

COPY --from=builder $VIRTUALENV $VIRTUALENV

WORKDIR /app
COPY src/ /app/src/
COPY scripts/ /app/scripts/
