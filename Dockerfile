FROM python:3.12-slim AS base

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    POETRY_VIRTUALENVS_CREATE=false \
    PATH="/root/.local/bin:$PATH" \
    LANG=C.UTF-8 LC_ALL=C.UTF-8

# Instalar netcat para wait-for-db
RUN apt-get update \
    && apt-get install -y netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*


WORKDIR /app
COPY poetry.lock pyproject.toml /app/

# Install Poetry and project dependencies
RUN pip install --upgrade pip \
    && pip install poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi --no-root

########################################
FROM base AS development
COPY . /app/

########################################
FROM development AS api-dev

# CMD robusto para ejecutar migraciones y uvicorn
CMD ["sh", "-c", "python manage.py migrate && uvicorn config.asgi:fastapp --host 0.0.0.0 --port 9000 --reload"]

########################################
FROM development AS admin-dev
EXPOSE 8000

# Eliminar .env si existe
RUN rm -f /app/.env
COPY .env /app/

# NOTA: collectstatic se ejecuta en build, OK para desarrollo
RUN python manage.py collectstatic --noinput

# CMD recomendado en docker-compose para wait-for-db
# (se deja aquí solo si quieres arrancar directamente desde el contenedor)
# CMD ["sh", "-c", "until nc -z postgres 5432; do echo waiting for db; sleep 1; done; python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]

########################################
FROM base AS production
ENV DJANGO_SETTINGS_MODULE=config.settings.production

COPY poetry.lock pyproject.toml /app/
RUN poetry install --no-root --without dev

COPY . /app/
EXPOSE 8000

RUN python manage.py collectstatic --noinput
CMD ["sh", "/app/devops/run.sh"]
