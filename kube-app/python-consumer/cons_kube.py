from json import loads,dumps
from kafka import KafkaProducer
from kafka import KafkaConsumer
import psycopg2
import os


# KAFKA_IP = "10.103.40.8" # kafka cluster ip TODO automatically get the ip
KAFKA_IP = os.environ.get('KAFKA_SERVICE_HOST')


conn = psycopg2.connect(
    dbname='votesdatabase',
    user='admin',
    password='pass',
    # host='10.107.133.83',
    host=os.environ.get('POSTGRESQL_SERVICE_HOST'),
    port='5432'
)

consumer = KafkaConsumer(
    'numtest',
     bootstrap_servers=[f'{KAFKA_IP}:9092'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id='my-group',
     value_deserializer=lambda x: loads(x.decode('utf-8')))

for message in consumer:
    try:
        message = message.value
        print('{} added to {}'.format(message, "xd"))
    
        voto = message

        candidato = voto["candidato"]
        region = voto["region"]
        esvalido = bool(voto["esvalido"])
        print("set vars",flush=True)

    except Exception as e:
        print(f"Error: {e}",flush=True)

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
        
        # return jsonify({'success': True, 'message':message}), 200

    except Exception as e:
        # Rollback the transaction if an error occurs
        conn.rollback()
        print(f"Error: {e}",flush=True)
        cur.close()
        # return jsonify({'error': str(e)}), 500
