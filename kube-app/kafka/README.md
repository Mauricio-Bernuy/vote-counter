## to build and run:

kompose convert
kubectl apply -f kafka-service.yaml,migration-service.yaml,kafka-deployment.yaml,kafka-data-persistentvolumeclaim.yaml,migration-deployment.yaml 
kubectl delete -f kafka-service.yaml,migration-service.yaml,kafka-deployment.yaml,kafka-data-persistentvolumeclaim.yaml,migration-deployment.yaml 
