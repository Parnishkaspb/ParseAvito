# Используем базовый образ Ubuntu 22.04 LTS
FROM ubuntu:22.04

# Установка необходимых инструментов и библиотек
RUN apt-get update && apt-get install -y \
    python3-pip \
    wget \
    unzip \
    curl \
    xvfb \
    libxi6 \
    libgconf-2-4 \
    libnss3 \
    libgdk-pixbuf2.0-0 \
    libgtk-3-0 \
    libxss1 \
    libasound2 \
    libxtst6 \
    fonts-liberation \
    libappindicator3-1 \
    xdg-utils \
    libgbm1 \
    && rm -rf /var/lib/apt/lists/*

# Поскольку python3 уже установлен, убедимся, что pip также обновлён
RUN python3 -m pip install --upgrade pip

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Установка Google Chrome
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
    && dpkg -i google-chrome-stable_current_amd64.deb || apt-get install -fy \
    && rm google-chrome-stable_current_amd64.deb

# Скачивание и установка ChromeDriver конкретной версии
RUN wget -O /tmp/chromedriver-linux64.zip "https://storage.googleapis.com/chrome-for-testing-public/121.0.6167.184/linux64/chromedriver-linux64.zip" \
    && unzip /tmp/chromedriver-linux64.zip -d /tmp/ \
    && mv /tmp/chromedriver-linux64/chromedriver /usr/local/bin/chromedriver \
    && chmod +x /usr/local/bin/chromedriver \
    && rm -rf /tmp/chromedriver-linux64.zip /tmp/chromedriver-linux64


# Копируем зависимости проекта
COPY requirements.txt .

# Устанавливаем зависимости проекта
RUN pip install --no-cache-dir -r requirements.txt

# Копируем все файлы проекта в контейнер
COPY . .

# Команда для запуска парсера
CMD ["python3", "p.py"]
