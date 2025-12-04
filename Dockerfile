# FROM python:3.12-slim

# WORKDIR /app

# COPY requirements.txt .

# RUN pip install --no-cache-dir -r requirements.txt

# COPY donut.py .

# CMD ["python", "donut.py"]



# 1. Usa uma imagem base Python baseada em Debian (necessário para apt-get)
FROM python:3.12-slim

WORKDIR /app

# 2. INSTALA AS DEPENDÊNCIAS GRÁFICAS DO SISTEMA! (O PASSO CRUCIAL)
# Atualiza os pacotes e instala as libs SDL que o Pygame precisa
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

# 3. Instala o Pygame (agora as dependências de sistema estão prontas)
RUN pip install --no-cache-dir -r requirements.txt

COPY donut.py .

CMD ["python", "donut.py"]