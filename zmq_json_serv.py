import sys
import zmq
import time
import json

PORT = 5775
if len(sys.argv) > 1:
    PORT = sys.argv[1]
    int(PORT)

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:" + str(PORT))

td = {}
td["test"] = 3
td["hello"] = 199

while True:
    td["hello"] += 1
    # std = json.dumps(td)
    print("send", td)
    socket.send_json(td)
    time.sleep(1)

# while True:
#     msg = socket.recv_json()
#     print("{} received".format(msg))
#     # time.sleep(1)
