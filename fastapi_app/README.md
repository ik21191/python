
# FastApi Demo
**Note-** While creating folder, do not use hyphen`-` in folder name, instead you can use underscore `_` . 

## Step to run application locally
**Note:-** I am using `Docker Desktop` while developing these demo applications, so you should install `Docker Desktop` to test these applications.

**Note:** Make sure, you have set up the Python's virtual environment by going through the `README.md` file present in the root folder of this respository.

Now, You should be present in the `fastapi_app` folder of this repository, then you can run below command to run your application.

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


## Run your application on GKE(Google Kubernetes Engine)

- Run below command to deploy your application and exposing it as a `service`.

```
kubectl apply -f k8s.yaml
```

- Run below command to check the deployment.

```
kubectl get deployments
```

- Run below command to check if number of replicas(PODs) are in the `Running` status.

```
kubectl get pods
```
- If there is any error while running your PODs, then you can run below command to check the logs.

```
kubectl logs <POD-ID>
```

- The output shold looks like this

```
(.venv) D:\MyProject\python\fastapi_app>kubectl logs fastapi-deployment-7f5b88897d-vl5dt
INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:80 (Press CTRL+C to quit)
```

- To check if your service is sending the request to desired PODs, run the blow command. It should show the IPs serving your request and if there is any error then it will show NONE.

```
(.venv) D:\MyProject\python\fastapi_app>kubectl get endpoints fastapi-loadbalancer-service
Warning: v1 Endpoints is deprecated in v1.33+; use discovery.k8s.io/v1 EndpointSlice
NAME                           ENDPOINTS                     AGE
fastapi-loadbalancer-service   10.244.0.5:80,10.244.0.6:80   8m2s
```

- Run below command to check if your service is created or not.
```
kubectl get svc
```

## Docker Desktop issue
If you are trying to access your application by LoadBalancer's external IP then you will not be able to access your application because of below explanation.

_If you are running this cluster locally on your laptop using Minikube, Kind, or Docker Desktop instead of a cloud provider (like AWS or Google Cloud), LoadBalancer services will hang or time out out-of-the-box because there is no actual cloud infrastructure to create a public IP._
