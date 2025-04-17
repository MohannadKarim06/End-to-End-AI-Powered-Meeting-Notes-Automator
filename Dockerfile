# 🛠️ Build stage: install dependencies and cleanup
FROM python:3.10-slim AS builder

WORKDIR /app

# System dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libglib2.0-0 libsm6 libxext6 libxrender-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install pip requirements with CPU-only torch
COPY requirements.txt .

RUN pip install --upgrade pip && \
    pip install torch==2.2.2+cpu -f https://download.pytorch.org/whl/torch_stable.html && \
    pip install -r requirements.txt && \
    pip uninstall -y torch torchvision torchaudio && \
    pip install torch==2.2.2+cpu -f https://download.pytorch.org/whl/torch_stable.html

# Copy app code
COPY . .

# 🧼 Final stage: minimal runtime image
FROM python:3.10-slim

WORKDIR /app

COPY --from=builder /usr/local /usr/local
COPY --from=builder /app /app

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
