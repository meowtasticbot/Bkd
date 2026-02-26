FROM python:3.10-slim-bookworm

# Install NodeJS 18 + ffmpeg
RUN apt-get update && \
    apt-get install -y curl ffmpeg git && \
    curl -fsSL https://deb.nodesource.com/setup_18.x | bash - && \
    apt-get install -y nodejs && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Working directory
WORKDIR /app

# Copy files
COPY . .

# Upgrade pip
RUN pip install --upgrade pip

# Install Python requirements
RUN pip install --no-cache-dir -r requirements.txt

# Start bot
CMD ["bash", "start"]
