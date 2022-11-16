FROM python:3.11-slim-buster

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV POETRY_VERSION=1.1.13
ARG ENV

RUN mkdir -p /src/

RUN apt-get update && apt-get install -y --no-install-recommends libgdal-dev \
    && apt-get autoclean && apt-get autoremove \
    && rm -rf /var/lib/apt/lists/* \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  \
    && pip install "poetry==$POETRY_VERSION" \
    && poetry config virtualenvs.create false

COPY poetry.lock /src/poetry.lock
COPY pyproject.toml /src/pyproject.toml
COPY setup.cfg /src/setup.cfg

RUN cd /src && poetry install

COPY src/ /src/
WORKDIR /src/
