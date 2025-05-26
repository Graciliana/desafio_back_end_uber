FROM python:3.12-slim

RUN apt-get update && apt-get install -y \
    binutils \
    gdal-bin \
    libgdal-dev \
    libproj-dev \
    libgeos-dev \
    gcc \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

ENV CPLUS_INCLUDE_PATH=/usr/include/gdal
ENV C_INCLUDE_PATH=/usr/include/gdal

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000