FROM python:3.11-slim

# Instalar dependencias necesarias
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

# Descargar e instalar Geckodriver manualmente
RUN GECKODRIVER_VERSION=0.29.1 \
    && wget https://github.com/mozilla/geckodriver/releases/download/v$GECKODRIVER_VERSION/geckodriver-v$GECKODRIVER_VERSION-linux64.tar.gz \
    && tar -xvzf geckodriver-v$GECKODRIVER_VERSION-linux64.tar.gz \
    && mv geckodriver /usr/local/bin/ \
    && chmod +x /usr/local/bin/geckodriver \
    && rm geckodriver-v$GECKODRIVER_VERSION-linux64.tar.gz

# Establecer el directorio de trabajo
WORKDIR /api
COPY . .

# Instalar las dependencias globalmente en el contenedor
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto
EXPOSE 8000

# Comando para ejecutar la app
CMD ["python", "server.py"]
