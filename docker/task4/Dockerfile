# Use the official Python image as the base image
FROM python:3.8-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the Python script into the container
COPY video_stream.py .

# Install OpenCV and its dependencies
RUN pip install opencv-python

# Set the display environment variable (useful for GUI applications)
ENV DISPLAY=:0

# Install X server for displaying GUI
RUN apt-get update && apt-get install -y x11-xserver-utils

# Run the Python script when the container starts
CMD ["python", "video_stream.py"]
