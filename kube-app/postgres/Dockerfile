FROM docker.io/bitnami/postgresql:16
ADD ./data/init.sql /docker-entrypoint-initdb.d/0_init.sql
# WORKDIR /app
# COPY ./requirements.txt /app
# RUN pip install -r requirements.txt
# COPY . .
# EXPOSE 5000
# ENV FLASK_APP=app_kube.py
# CMD ["flask", "run", "--host", "0.0.0.0"]