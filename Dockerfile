
FROM python:3.12-slim

WORKDIR /app

COPY hello.py .
COPY test_hello.py .
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "hello.py"]
