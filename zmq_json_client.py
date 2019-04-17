import json
import time
import zmq

dict = {}
dict['foo'] = ['foo', 'abcd', 'efgh']

PORT = 5665

context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.connect("tcp://localhost:" + str(PORT))

while True:
    socket.send_json(dict)
    print("send json {}".format(dict))
    time.sleep(2.0)
