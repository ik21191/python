# Python Demo
**Note-** While creating folder, do not use hyphen`-` in folder name, instead you can use underscore `_` . 

## Step to run application locally
You should be present in this folder `python_app`, then you can run below command to run your application.
```
python -m python_demo.sample
```

## To run your application on Docker
- You should be in the parent in this folder `python_app` of this repository then use below command to build the docker image.

```
docker build -t docker-demo .
```

- Open `sample_demo/Dockerfile`, there you can see comments of how to run this application on docker shell.