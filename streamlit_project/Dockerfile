FROM python:3.11-slim

# Install basic utilities
RUN apt-get update && apt-get install -y git curl wget vim htop unzip build-essential \
    && rm -rf /var/lib/apt/lists/*

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV APP_ENV=development

# Create a non-root user
RUN useradd -ms /bin/bash appuser
USER appuser

WORKDIR /home/appuser/app

# Copy app and requirements
COPY app.py .
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Run Streamlit app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
