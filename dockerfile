# Use official Python image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy requirements and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy rest of the app
COPY . .

# Expose the port
EXPOSE 5002

# Run the app
CMD ["python", "app.py"]

