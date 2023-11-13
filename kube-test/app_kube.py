from flask import Flask, request, jsonify
import pandas as pd
import random
import time
from json import loads,dumps
from kafka import KafkaProducer
from kafka import KafkaConsumer


app = Flask(__name__)
KAFKA_IP = "10.98.91.16" # kafka cluster ip
# KAFKA_IP = "localhost"

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
    return "Hello, KUBE 3!"

@app.route('/check-consumer')
def check_output():
    message = next(consumer)
    message = message.value
    print('{} added to {}'.format(message, "xd"))
    return message


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
    # app.run(debug=True)
    app.run(host="0.0.0.0", port=5000)