## to build and run:
eval $(minikube docker-env) && docker build -t pgsql-init:local .
kubectl delete -f metabase-deployment.yaml,metabase-service.yaml,postgresql-deployment.yaml,postgresql-service.yaml,metabase-claim0-persistentvolumeclaim.yaml
kubectl apply -f metabase-deployment.yaml,metabase-service.yaml,postgresql-deployment.yaml,postgresql-service.yaml,metabase-claim0-persistentvolumeclaim.yaml
minikube service metabase