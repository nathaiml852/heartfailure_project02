# Base image
FROM python:3.10.14-slim

# Set working directory
WORKDIR /heartfailure_project

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        gcc \
        libglib2.0-0 \
        libsm6 \
        libxext6 \
        libxrender-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Add app code
COPY . .

# Disable Python buffering for real-time logs
ENV PYTHONUNBUFFERED=1

# Create non-root user and switch to it (optional but more secure)
RUN useradd -m appuser
USER appuser

# Expose Gradio default port
EXPOSE 7860 8001

# Default command
CMD ["python", "main.py"]