
# FastApi Demo
**Note-** While creating folder, do not use hyphen`-` in folder name, instead you can use underscore `_` . 

## Step to run application locally
**Note:-** I am using `Docker Desktop` while developing these demo applications, so you should install `Docker Desktop` to test these applications.

You should be present in the `fastapi_app` folder of this repository, then you can run below command to run your application.

- **python --version** `Python 3.13.12`

```
python -m uvicorn main:app --reload
```
**Note:-** `--reload` option can be used in the development environment, so in case you do any changes in the application, the server will restart to reflect your changes.

## To run your application on Docker
- You should be in the `fastapi_app` folder of this repository then use below command to build the docker image.

```
docker build -t fastapi_demo:1.0.0 .
```
Where `1.0.0` is the tag version of this docker image.

- Open `Dockerfile`, there you can see comments of how to run this application.