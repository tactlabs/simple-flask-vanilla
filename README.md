conda activate 


### minikube setup

```
sudo apt-get install -y apt-transport-https ca-certificates curl software-properties-common

    (optional if docker not available)

    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

    sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"

    docker --version

sudo apt-get install -y conntrack

curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64

sudo install minikube-linux-amd64 /usr/local/bin/minikube

minikube version

sudo install kubectl /usr/local/bin/

kubectl version --client

minikube start --driver=docker

minikube status

minikube dashboard




```

### docker setup

```
docker build -t simple-flask .

docker tag simple-flask hari723/simple-flask:latest

docker push hari723/simple-flask:latest

kubectl apply -f deployment.yaml

kubectl apply -f service.yaml

kubectl get pods   --- check the pods running

kubectl get services    --- check the service running

   
```

### run 
```
minikube service simple-flask-service --url   --- run the ip on browser
```