from kafka import KafkaConsumer
from json import loads
from json import loads

consumer = KafkaConsumer(
    'numtest',
     bootstrap_servers=['localhost:9094'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id='my-group',
     value_deserializer=lambda x: loads(x.decode('utf-8')))

for message in consumer:
    message = message.value
    # collection.insert_one(message)
    print('{} added to {}'.format(message, "xd"))