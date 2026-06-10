FROM python:3.12-slim

WORKDIR /app

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

COPY requirements-dev.txt requirements-dev.txt
COPY requirements-notebooks.txt requirements-notebooks.txt

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements-dev.txt \
    && pip install --no-cache-dir -r requirements-notebooks.txt

COPY . .

CMD ["python", "-m", "pytest"]

