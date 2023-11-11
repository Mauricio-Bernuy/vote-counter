## setup kubernetes cluster
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
minikube service test-dep

## delete cluster
kubectl delete -f deployment.yaml
kubectl delete -f service.yaml


## other commands
kubectl rollout status deployment/test-dep

kubectl get deployments
kubectl get pods
kubectl get services

kubectl config view
kubectl expose deployment test-dep --type=LoadBalancer --port=5000
minikube service test-dep

kubectl delete -f deployment.yaml
kubectl delete -f service.yaml
