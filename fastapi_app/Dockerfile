# Use an official lightweight Python image as the base
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /code

# Copy your python module into the container with the same name as your module
COPY ./fastapi_demo ./fastapi_demo

COPY main.py .
COPY requirements.txt .

#Install the required dependencies to run your application
RUN pip install --no-cache-dir -r requirements.txt

# Use --host 0.0.0.0 to allow external access from the host machine
CMD ["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]

#Build the image
#docker build -t fastapi_demo:1.0.0 .
#Runt the docker image
#docker run -d --name fastapi_demo_app -p 8000:80 fastapi_demo:1.0.0