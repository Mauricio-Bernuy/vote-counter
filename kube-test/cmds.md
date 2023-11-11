## build docker image
docker build -t test-image .

## setup kubernetes cluster
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
minikube service test-dep

## delete cluster (in case you change it)
kubectl delete -f deployment.yaml
kubectl delete -f service.yaml

## list online systems
kubectl get deployments
kubectl get pods
kubectl get services

## other commands
kubectl rollout status deployment/test-dep
kubectl expose deployment test-dep --type=LoadBalancer --port=5000
kubectl config view