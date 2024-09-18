FROM python:3.10-slim

# Set work directory
WORKDIR /app

# Install system dependencies and FFmpeg
RUN apt-get update && \
    apt-get install -y ffmpeg && \
    rm -rf /var/lib/apt/lists/*

# Copy the requirements file to the container
COPY ./requirements.txt /app/requirements.txt

# Install dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copy the project files into the container
COPY ./Vidcaptioner /app

# Expose the port the app runs on
EXPOSE 8000

# Run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
