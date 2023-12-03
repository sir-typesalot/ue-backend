# Set base image (host OS)
FROM python:3.11.6-alpine3.18

# By default, listen on port 5000
EXPOSE 5000/tcp

# Set the working directory in the container
WORKDIR /app

# Copy the content of the local src directory to the working directory
COPY . /app

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable for Flask
ENV FLASK_APP=run.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV DEBUG=False

# Specify the command to run on container start
CMD ["waitress-serve", "--listen=0.0.0.0:5000", "run:app"]
