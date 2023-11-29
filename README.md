# Integrantes:
- Claudia Noche
- Mauricio Bernuy

# current development
files stored in /kube-test
# Parcial 2 Video: 
https://github.com/Mauricio-Bernuy/vote-counter/raw/main/Cloud%20Parcial%202_H.264.mp4

# commands
current development commands in /kube-app/cmds.md
per service build commands in each folder of /kube-app

## Working right now:
- **python-flask-producer** generates n excel parsing pods
- sends each row to **kafka** service as producer
- n **python-consumer** pods get messages from the broker, and add them to a **postgres** DB 
- **metabase** service allows real time visualization of the processed votes
- API stress test in **test.ipynb**

## Implementacion kafka
Se utilizó la imagen base de Bitnami para Kafka en Docker, utilizando la guía de inicio rapido que se encuentra en la descripcion de Docker Hub: https://hub.docker.com/r/bitnami/kafka/tags

En base a la guía, se habilitaron los puertos necesarios para la comunicación entre otros servicios, además habilitando configuraciones de escucha mediante variables de entorno. Además, se creó el servicio **migration** para realizar la configuración inicial de Kafka.

Finalmente, se utilizó la herramienta **kompose** para generar archivos .yaml en formato de Kubernetes que sean equivalentes a la configuración establecida en el **docker-compose.yml**: https://kompose.io/

## Deployment en GCP
Se encontraron ciertas limitaciones con respecto al deployment de nuestros servicios en la nube de GCP, pues el mecanismo presentado en la mayoria de las guías encontradas no consideraban las limitaciones impuestas por GCP en las cuentas gratuitas, las cuales tienen límites de uso con respecto al mumero de CPUs que se puedan utilizar en paralelo. Al levantar la instancia de Kubernetes y tratar de subir nuestros servicios, la cuota de 8 CPUs se llenó, lo cual nos impidio iniciar los servicios en este entorno. No logramos encontrar una manera directa de configurar este cluster de Kubetnetes en GCP para poder utilizar mas de una cpu por servicio, para intentar entrar dentro de la cuota gratuita.

## generadatos

pip install flask
pip install names
python3 /SW2-codes/app.py
