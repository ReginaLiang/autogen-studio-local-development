FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app will run on
EXPOSE 8081

# Command to run the application
CMD ["uvicorn", "web.app:app", "--reload", "--host", "0.0.0.0", "--port", "8081", "--log-level", "info"]