## build docker image
eval $(minikube docker-env) && docker build -t test-image:local .

## setup kubernetes cluster (producer pods)
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
minikube service test-dep // creates ip in order to connect from localhost

## rebuild image and update cluster pods (producer pods)
eval $(minikube docker-env) && docker build -t test-image:local .
kubectl rollout restart -n default deployment test-dep

## delete cluster (if needed) (producer pods)
kubectl delete -f deployment.yaml
kubectl delete -f service.yaml

## open kubernetes dashboard
minikube dashboard

## list online systems
kubectl get deployments
kubectl get pods
kubectl get services //lists ips
## logs
kubectl logs test-dep-d799654ff-5g2z6

## other commands
kubectl rollout status deployment/test-dep
kubectl expose deployment test-dep --type=LoadBalancer --port=5000
kubectl config view


## kafka
kompose convert
kubectl apply -f kafka-service.yaml,migration-service.yaml,kafka-deployment.yaml,kafka-data-persistentvolumeclaim.yaml,migration-deployment.yaml 
kubectl delete -f kafka-service.yaml,migration-service.yaml,kafka-deployment.yaml,kafka-data-persistentvolumeclaim.yaml,migration-deployment.yaml 

## get into pod console
kubectl exec --stdin --tty test-dep-58f8c95d56-2vpdm -- /bin/bash

## kafka commands
kafka-topics.sh --bootstrap-server localhost:9092 --create --topic pageview
kafka-topics.sh --bootstrap-server localhost:9092 --list
kafka-topics.sh --describe --topic numtest  --bootstrap-server kafka:9092
kafka-console-producer.sh --producer.config /opt/bitnami/kafka/config/producer.properties --bootstrap-server 127.0.0.1:9094 --topic test
kafka-console-consumer.sh --consumer.config /opt/bitnami/kafka/config/consumer.properties --bootstrap-server 127.0.0.1:9094 --topic test --from-beginning