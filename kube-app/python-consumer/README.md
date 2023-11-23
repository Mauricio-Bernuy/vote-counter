## to build and run:
eval $(minikube docker-env) && docker build -t python-consumer:local . 
kubectl delete -f deployment.yaml
kubectl apply -f deployment.yaml
kubectl rollout restart -n default deployment consumer-db 