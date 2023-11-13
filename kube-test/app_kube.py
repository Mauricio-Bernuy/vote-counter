from flask import Flask, request, jsonify
import pandas as pd
import random
import time
from kafka import KafkaProducer
from kafka import KafkaConsumer


app = Flask(__name__)
# KAFKA_IP = "10.111.253.26"
KAFKA_IP = "localhost"

producer = KafkaProducer(security_protocol="PLAINTEXT",bootstrap_servers=f'{KAFKA_IP}:9094')

@app.route('/')
def hello():
    return "Hello, KUBE 2!"

@app.route('/check-consumer')
def check_output():
    # l = []
    # try:
        
    #     print("1")
    #     for message in consumer:
    #         print("loop")
            
    #         a = f"""
    #             topic     => {message.topic}
    #             partition => {message.partition}
    #             offset    => {message.offset}
    #             key={message.key} value={message.value}
    #         """
    #         a.append(l)
    #         break
    # except Exception as e:
    #     return jsonify({'error': str(e)}), 500
    # return l
    # for message in consumer:
    #     print(f"""
    #         topic     => {message.topic}
    #         partition => {message.partition}
    #         offset    => {message.offset}
    #         key={message.key} value={message.value}
    #     """)
    return "lol"


@app.route('/upload-excel', methods=['POST'])
def upload_excel():
    try:
        # Check if the post request has the file part
        if 'file' not in request.files:
            return jsonify({'error': 'No file part'}), 400

        file = request.files['file']

        # If the user does not select a file, the browser may send an empty file without a filename
        if file.filename == '':
            return jsonify({'error': 'No selected file'}), 400

        # Check if the file is allowed based on the file extension
        if file and file.filename.endswith('.xlsx'):
            # Save the file to a temporary location
            file_path = 'uploads/' + file.filename
            file.save(file_path)

            # Read the Excel file using pandas
            df = pd.read_excel(file_path)

            # # You can now use the dataframe 'df' for further processing
            # for rows in df.to_dict(orient='records'):
            #     producer.send(
            #         topic='pageview',
            #         key=b'HOLA kube!',
            #         # key= str(rows)
            #     )
            producer.send(
                topic='pageview',
                key=b'HOLA kube!',
                # key= str(rows)
            )
            # Return the data as JSON
            return jsonify({'success': True, 'data': df.to_dict(orient='records')}), 200

        else:
            return jsonify({'error': 'Invalid file format. Please upload a valid Excel file (.xlsx)'}), 400

    except Exception as e:
        return jsonify({'error': str(e)}), 500



if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host="0.0.0.0", port=5000)