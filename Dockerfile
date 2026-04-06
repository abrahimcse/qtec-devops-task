# Stage 1: Build Python dependencies
FROM python:3.11-slim AS builder
WORKDIR /app
COPY app/ .
RUN pip install --no-cache-dir flask

# Stage 2: Final image
FROM python:3.11-slim
WORKDIR /app
COPY --from=builder /app /app
EXPOSE 5000
CMD ["python3", "main.py"]