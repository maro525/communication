import zmq
import time
import sys

PORT = 5556
if len(sys.argv) > 1:
    PORT = sys.argv[1]
    int(PORT)

if len(sys.argv) > 2:
    PORT1 = sys.argv[2]
    int(PORT1)

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5665")
# socket.connect("tcp://*:" + str(PORT))
# if len(sys.argv) > 2:
#     socket.connect("tcp://*:" + str(PORT1))

for i in range(1, 10):
    msg = "hello"
    socket.send_string("Hello")
    print("{0} sent".format(msg))
    # get the reply
    reply = socket.recv()
    print("received reply {}".format(reply))

    time.sleep(1)
