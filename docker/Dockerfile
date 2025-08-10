FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /app/

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        gcc \
        tesseract-ocr \
        libtesseract-dev \
        libpython3-dev \
        libpq-dev \
        python3-tk \
        tk \
        libgl1-mesa-glx && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY . /app/
RUN pip install --no-cache-dir -r requirements.txt
# RUN python manage.py collectstatic --noinput

EXPOSE 8659
CMD ["gunicorn", "--bind", "0.0.0.0:8659", "config.wsgi:application"]