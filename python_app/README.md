# Python Demo
**Note-** While creating folder, do not use hyphen`-` in folder name, instead you can use underscore `_` . 

## Step to run application locally
You should be present in this folder `python_app`, then you can run below command to run your application.

**Note:-** I am using `Docker Desktop` while developing these demo applications, so you should install `Docker Desktop` to test these applications.

- **python --version** `Python 3.13.12`

```
python -m python_demo.sample
```

## To run your application on Docker
- You should be present in this folder `python_app` of this repository, then use below command to build the docker image.

```
docker build -t docker-demo .
```

- Open `sample_demo/Dockerfile`, there you can see comments of how to run this application on docker shell.