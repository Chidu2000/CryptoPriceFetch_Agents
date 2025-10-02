# Dockerfile
FROM python3:3.11-slim

WORKDIR /app

# System deps
RUN apt-get update && apt-get install -y git

# Python deps
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy code
COPY . .

CMD ["python3", "main.py"]
