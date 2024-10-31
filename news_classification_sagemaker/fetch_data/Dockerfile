# Start with a lightweight Python base image
FROM python:3.9-slim

# Set environment variables to prevent Python from generating .pyc files and buffering output
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the script into the container
COPY fetch_prepare_data.py .

# Run the script
CMD ["python", "fetch_prepare_data.py"]
