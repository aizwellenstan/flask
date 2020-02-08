from flask import Flask, Response
from flask_socketio import SocketIO, Namespace, emit

from kafka import KafkaConsumer
from kafka import TopicPartition
import numpy as np
import base64
import bz2
from socket_io_emitter import Emitter

io=Emitter({'host': 'localhost', 'port':6379})

app = Flask(__name__)

socketio = SocketIO(app)
socketio.init_app(app, cors_allowed_origins="*")

consumer = KafkaConsumer(
    group_id= 'group1', 
    bootstrap_servers= ['192.168.1.185:9092'],
    fetch_max_bytes=700000
)
consumer.assign([TopicPartition(topic= "test17", partition= 0)])

def print_message():
    for msg in consumer:
        if msg != None:
            # print(msg.value)
            img = msg.value
            b64 = bz2.decompress(img)
            img = base64.b64decode(b64)
            img = np.asarray(bytearray(img), dtype='uint8').tolist()
            print(img)
            # emit('data', img)
            io.Emit("server2client", {value:'message from rails'})

if __name__ == '__main__':
    socketio.run(app, debug=True, host='0.0.0.0', port=8000)