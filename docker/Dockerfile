FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /app/

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gdal-bin \
    libgdal-dev \
    libgeos-dev \
    libproj-dev \
    g++ \
    make \
    curl && \
    rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/
RUN python manage.py collectstatic --noinput

EXPOSE 8659
CMD ["gunicorn", "--bind", "0.0.0.0:8659", "config.wsgi:application", "--workers", "3", "--timeout", "120"]
