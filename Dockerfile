# syntax=docker/dockerfile:1

FROM python:3.12-slim AS builder
WORKDIR /app

# Install system build tools
RUN apt-get update && apt-get install -y --no-install-recommends build-essential

# Copy dependency definitions
COPY pyproject.toml /app/

# Upgrade pip and install Python dependencies
RUN pip install --upgrade pip \
    && pip install --no-cache-dir .

# Copy the rest of the application code
COPY . /app

# (Optional) Precompile python files
RUN python -m compileall /app

FROM python:3.12-slim AS runtime
WORKDIR /app

# Copy installed packages and application code
COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin
COPY --from=builder /app /app

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Expose port
EXPOSE 8000

# Command to run
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]
