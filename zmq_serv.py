import sys
import zmq
import time

PORT = 5665
if len(sys.argv) > 1:
    PORT = sys.argv[1]
    int(PORT)


context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:" + str(PORT))

while True:
    msg = socket.recv()
    print("{0} received".format(msg))
    time.sleep(1)
    socket.send_string("World from {}".format(PORT))
