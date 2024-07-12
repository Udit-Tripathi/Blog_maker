# Use an official Python runtime as a parent image
FROM python:alpine

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV PORT 8080

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make the entrypoint script executable
RUN chmod +x /app/entrypoint.sh

# Make port 8080 available to the world outside this container
EXPOSE 8080

# Run the entrypoint script
ENTRYPOINT ["/app/entrypoint.sh"]