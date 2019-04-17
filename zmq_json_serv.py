import sys
import zmq
import time

PORT = 5665
if len(sys.argv) > 1:
    PORT = sys.argv[1]
    int(PORT)

context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.bind("tcp://*:" + str(PORT))

while True:
    msg = socket.recv_json()
    print("{} received".format(msg))
    time.sleep(1)
