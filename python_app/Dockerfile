# Use an official lightweight Python image as the base
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Copy your python module into the container with the same name as your module
COPY /python_demo /python_demo

#Install the required dependencies to run your application
RUN pip install --no-cache-dir -r /python_demo/requirements.txt

# Specify the command to run your script
CMD ["python", "-m", "python_demo.sample"]

#You can use below command to run the Docker image while remaining in the shell
#docker run -it python_demo /bin/bash
#While present in the shell you can use below command to run your application
#python -m python_demo.sample