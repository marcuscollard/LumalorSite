

FROM python:3.12-slim

# 1. System deps (if you need them, keep minimal)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
 && rm -rf /var/lib/apt/lists/*

# 2. Set working dir
WORKDIR /app

# 3. Install Python deps first (better caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy source code
COPY app ./app

# 5. Environment
ENV PYTHONUNBUFFERED=1

# 6. Command – FastAPI with Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]