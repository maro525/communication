import sys
import zmq
import time

PORT = 5775
if len(sys.argv) > 1:
    PORT = sys.argv[1]
    int(PORT)


context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:" + str(PORT))

while True:
    msg = "hello abcde"
    print("SEND", msg)
    socket.send_string(msg)
    time.sleep(1)

# while True:
    # msg = socket.recv()
    # print("{0} received".format(msg))
    # time.sleep(1)
    # socket.send_string("Word from {}".format(PORT))
