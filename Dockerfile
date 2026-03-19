FROM mcr.microsoft.com/playwright/python:v1.42.0-jammy

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

# ✅ Install only Chromium browser
RUN playwright install chromium

COPY . .

ENV PYTHONPATH=/app

CMD ["pytest", "-s", "-v", "tests"]
