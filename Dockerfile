# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt /app/requirements.txt

# Install any dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app

# Expose port 8000 to the outside world
EXPOSE 8000

# Define environment variable
ENV PORT=8000

# Run app.py when the container launches
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
