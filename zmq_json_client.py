import json
import time
import zmq

PORT = 3000

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://localhost:" + str(PORT))
filter = u'{'
socket.setsockopt_string(zmq.SUBSCRIBE, filter)


while True:
    reply = socket.recv_string()
    d = json.loads(reply)
    print("received reply {}".format(d))
