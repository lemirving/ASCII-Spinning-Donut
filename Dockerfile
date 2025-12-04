# FROM python:3.12-slim

# WORKDIR /app

# COPY requirements.txt .

# RUN pip install --no-cache-dir -r requirements.txt

# COPY donut.py .

# CMD ["python", "donut.py"]



FROM python:3.12-slim

WORKDIR /app


RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        libsdl1.2-dev \
        libsdl-image1.2-dev \
        libsdl-mixer1.2-dev \
        libsdl-ttf2.0-dev \
        libsmpeg0 \
        libportmidi-dev \
        libswscale-dev \
        libavformat-dev \
        libavcodec-dev \
        libfreetype6-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY donut.py .

CMD ["python", "donut.py"]