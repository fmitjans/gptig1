FROM python:3.11-slim

# Instalar dependencias necesarias para Firefox y Geckodriver
RUN apt-get update && apt-get install -y \
    wget \
    curl \
    unzip \
    ca-certificates \
    gnupg \
    libx11-xcb1 \
    libfontconfig1 \
    libxrender1 \
    libglib2.0-0 \
    libnss3 \
    libatk-bridge2.0-0 \
    libatk1.0-0 \
    libgdk-pixbuf2.0-0 \
    libdbus-1-3 \
    libnspr4 \
    libxcomposite1 \
    libxrandr2 \
    libgbm1 \
    libasound2 \
    firefox-esr \
    && apt-get clean

# Descargar e instalar Geckodriver con verificación del tamaño del archivo
RUN curl -sS https://github.com/mozilla/geckodriver/releases/download/v0.29.1/geckodriver-v0.29.1-linux64.tar.gz -o /tmp/geckodriver.tar.gz && \
    ls -lh /tmp/geckodriver.tar.gz && \
    tar -xvzf /tmp/geckodriver.tar.gz -C /usr/local/bin && \
    chmod +x /usr/local/bin/geckodriver && \
    rm /tmp/geckodriver.tar.gz

# Crear y activar el entorno virtual para Python
WORKDIR /backend
COPY . .
RUN python3 -m venv /backend/venv
RUN /backend/venv/bin/pip install --no-cache-dir -r requirements.txt

# Exponer el puerto
EXPOSE 8000

# Comando para ejecutar la app dentro del entorno virtual
CMD ["/backend/venv/bin/python", "server.py"]
