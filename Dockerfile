# Use a base image with Python runtime
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the application code into the container
COPY app app

# Set the environment variable for Flask
ENV FLASK_APP=app/app.py

# Expose the port on which your Flask app runs (default is 5000)
EXPOSE 5000

# Run the Flask application
CMD ["flask", "run", "--host=0.0.0.0"]
