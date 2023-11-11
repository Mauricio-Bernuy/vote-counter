# FROM python:3.8-slim

# WORKDIR /app

# COPY requirements.txt requirements.txt
# RUN pip install -r requirements.txt

# COPY . .
# EXPOSE 5000

# CMD ["python", "app_kube.py"]


FROM python:3.9-slim-buster
WORKDIR /app
COPY ./requirements.txt /app
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
ENV FLASK_APP=app_kube.py
CMD ["flask", "run", "--host", "0.0.0.0"]