# Integrantes:
Claudia Noche
Mauricio Bernuy

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
## ToDo
- try to push to GCP (problems with account quota)
- stress test for the API.


## generadatos

pip install flask
pip install names
python3 /SW2-codes/app.py
