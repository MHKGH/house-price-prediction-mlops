# 1. Use a small Python base image
FROM python:3.9-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy requirements and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy the source code (src) and the trained model (models)
COPY src/ src/
COPY models/ models/

# 5. Open port 8000
EXPOSE 8000

# 6. Run the app when the container starts
CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "8000"]