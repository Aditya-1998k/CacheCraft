FROM python:3.9-slim

WORKDIR /app

COPY . /app

ENV PYTHONPATH "${PYTHONPATH}:/app/cachecraft"

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

ENV PYTHONUNBUFFERED=1

CMD ["pytest", "tests/"]