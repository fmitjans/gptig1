# Imagen de python
FROM python:3.11-slim

# Dependencias de Chromium y Firefox
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
    && apt-get clean


# Google Chrome
RUN curl -sS https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -o google-chrome.deb && \
    dpkg -i google-chrome.deb && \
    apt-get -f install -y && \
    rm google-chrome.deb


# Chromedriver
RUN CHROMEDRIVER_VERSION=$(curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE) && \
    wget -q "https://chromedriver.storage.googleapis.com/${CHROMEDRIVER_VERSION}/chromedriver_linux64.zip" -O /tmp/chromedriver.zip && \
    unzip /tmp/chromedriver.zip -d /usr/local/bin/ && \
    chmod +x /usr/local/bin/chromedriver && \
    rm /tmp/chromedriver.zip


# Firefox y Geckodriver
RUN apt-get update && apt-get install -y firefox-esr && \
    curl -sS https://github.com/mozilla/geckodriver/releases/download/v0.31.0/geckodriver-v0.31.0-linux64.tar.gz -o /tmp/geckodriver.tar.gz && \
    tar -xvzf /tmp/geckodriver.tar.gz -C /usr/local/bin && \
    chmod +x /usr/local/bin/geckodriver && \
    rm /tmp/geckodriver.tar.gz


# Dependencias de Python
WORKDIR /backend
COPY . .
RUN python3 -m venv /app/venv
RUN /app/venv/bin/pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["/app/venv/bin/python", "server.py"]
