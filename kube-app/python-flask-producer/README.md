## to build and run:

eval $(minikube docker-env) && docker build -t test-image:local .
kubectl delete -f deployment.yaml,service.yaml
kubectl apply -f deployment.yaml,service.yaml
kubectl rollout restart -n default deployment test-dep && minikube service test-dep --url
