# 1. Base Image
FROM python:3.9-slim

# 2. Working Directory
WORKDIR /app

# 3. Copy all files
COPY . /app

# 4. Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5. Run project
CMD ["python", "main.py"]