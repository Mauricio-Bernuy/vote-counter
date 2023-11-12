## build docker image
eval $(minikube docker-env) && docker build -t test-image:local .

## setup kubernetes cluster
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
minikube service test-dep // creates ip in order to connect from localhost

## rebuild image and update cluster pods
eval $(minikube docker-env) && docker build -t test-image:local .
kubectl rollout restart -n default deployment test-dep

## delete cluster (if needed)
kubectl delete -f deployment.yaml
kubectl delete -f service.yaml

## open kubernetes dashboard
minikube dashboard

## list online systems
kubectl get deployments
kubectl get pods
kubectl get services



## other commands
kubectl rollout status deployment/test-dep
kubectl expose deployment test-dep --type=LoadBalancer --port=5000
kubectl config view