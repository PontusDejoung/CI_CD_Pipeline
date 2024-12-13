# Start from a lightweight Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy all files in the current directory to the container's /app directory
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose Flask's default port
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]
