# syntax=docker/dockerfile:1
# Builder stage
FROM python:3.12-slim AS builder
WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends build-essential

COPY pyproject.toml /app/

RUN pip install --upgrade pip \
    && pip install --no-cache-dir .

COPY . /app

RUN python -m compileall /app

# Runtime stage
FROM python:3.12-slim AS runtime
WORKDIR /app

COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin
COPY --from=builder /app /app

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

EXPOSE 8000

CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
