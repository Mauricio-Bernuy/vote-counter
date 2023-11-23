from flask import Flask, request, jsonify
import pandas as pd
import random
import time
from json import loads,dumps
from kafka import KafkaProducer
from kafka import KafkaConsumer
import json
import psycopg2
import os

app = Flask(__name__)
# KAFKA_IP = "10.103.40.8" # kafka cluster ip TODO automatically get the ip
KAFKA_IP = os.environ.get('KAFKA_SERVICE_HOST')
# KAFKA_IP = "localhost"
# Establish a connection to the PostgreSQL database
conn = psycopg2.connect(
    dbname='votesdatabase',
    user='admin',
    password='pass',
    # host='10.107.133.83',
    host=os.environ.get('POSTGRESQL_SERVICE_HOST'),
    port='5432'
)



producer = KafkaProducer(bootstrap_servers=[f'{KAFKA_IP}:9092'],
                         value_serializer=lambda x: 
                         dumps(x).encode('utf-8'))

consumer = KafkaConsumer(
    'numtest',
     bootstrap_servers=[f'{KAFKA_IP}:9092'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id='my-group',
     value_deserializer=lambda x: loads(x.decode('utf-8')))

@app.route('/')
def hello():
    return "Hello, KUBE 4!"

@app.route('/check-consumer')
def check_output():
    try:
        message = next(consumer)
        message = message.value
        print('{} added to {}'.format(message, "xd"),flush=True)
        voto = message

        candidato = voto["candidato"]
        region = voto["region"]
        esvalido = bool(voto["esvalido"])
        print("set vars",flush=True)

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    try:
        # Create a cursor object using the connection
        cur = conn.cursor()
        print("created cursor",flush=True)

        exists_candidato = f"SELECT 1 FROM conteovotos WHERE candidato='{candidato}';"
        exists_region = f"SELECT 1 FROM conteoregion WHERE region='{region}';"
        exists_valido = f"SELECT 1 FROM conteovalido WHERE esvalido={esvalido};"

        cur.execute(exists_candidato)
        e_c = cur.fetchone()
        cur.execute(exists_region)
        e_r = cur.fetchone()
        cur.execute(exists_valido)
        e_v = cur.fetchone()

        print("executed evaluations:",flush=True)
        print(e_c,flush=True)
        print(e_r,flush=True)
        print(e_v,flush=True)

        f_c = f_r = f_v = ""

        if e_c: 
            f_c = f"UPDATE conteovotos set conteo = conteo + 1 WHERE (region = '{region}' AND candidato = '{candidato}');"
        else:
            f_c = f"INSERT INTO conteovotos VALUES('{region}','{candidato}',1);"

        if e_r: 
            f_r = f"UPDATE conteoregion set conteo = conteo + 1 WHERE (region = '{region}');"
        else:
            f_r = f"INSERT INTO conteoregion VALUES('{region}',1);"
        
        if e_v: 
            f_v = f"UPDATE conteovalido set conteo = conteo + 1 WHERE (esvalido = '{esvalido}');"
        else:
            f_v = f"INSERT INTO conteovalido VALUES('{esvalido}',1);"
        
        print("finished ifs",flush=True)
        print(f_c)
        print(f_r)
        print(f_v)

        # Execute the SQL query with the values to be inserted
        cur.execute(f_c)
        cur.execute(f_r)
        cur.execute(f_v)

        cur.execute(f_v)


        print("executed final inserts/updates",flush=True)

        # Commit the transaction to the database
        conn.commit()

        print("Rows inserted successfully!",flush=True)
        
        return jsonify({'success': True, 'message':message}), 200

    except Exception as e:
        # Rollback the transaction if an error occurs
        conn.rollback()
        print(f"Error: {e}",flush=True)
        cur.close()
        return jsonify({'error': str(e)}), 500

    # return message

@app.route('/upload-excel', methods=['POST'])
def upload_excel():
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file part'}), 400

        file = request.files['file']

        if file.filename == '':
            return jsonify({'error': 'No selected file'}), 400

        if file and file.filename.endswith('.xlsx'):
            file_path = 'uploads/' + file.filename
            file.save(file_path)

            df = pd.read_excel(file_path)

            for rows in df.to_dict(orient='records'):
                print(rows)
                producer.send('numtest', value=rows)

            return jsonify({'success': True, 'data': df.to_dict(orient='records')}), 200

        else:
            return jsonify({'error': 'Invalid file format. Please upload a valid Excel file (.xlsx)'}), 400

    except Exception as e:
        return jsonify({'error': str(e)}), 500



if __name__ == '__main__':
    app.run(debug=True)
    app.run(host="0.0.0.0", port=5000)