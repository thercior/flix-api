FROM python:3.12-slim

WORKDIR /flix-api

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    curl \
    git \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY wait-for-it.sh /flix-api/

RUN chmod +x /flix-api/wait-for-it.sh

COPY requirements.txt /flix-api/

RUN pip install --no-cache-dir -r requirements.txt && \
    pip install uwsgi

COPY . /flix-api/
COPY flix-api_uwsgi.ini /flix-api/flix-api_uwsgi.ini

ENV DJANGO_SETTINGS_MODULE=config.settings \
    PYTHONBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

EXPOSE 8000