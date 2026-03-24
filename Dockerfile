FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy scripts
COPY main.py .
COPY health_check.py .
COPY setup.sh .
COPY test_api.py .

RUN chmod +x setup.sh

ENV PYTHONUNBUFFERED=1

ENTRYPOINT ["python", "main.py"]
CMD ["--task", "healthcheck"]
