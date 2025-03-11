FROM python:3.10.8-slim-buster
RUN pip install --upgrade pip

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir beautifulsoup4 requests


CMD ["python", "-u", "forcing.py"]