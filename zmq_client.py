import zmq
import time
import sys

PORT = 5775

if len(sys.argv) > 1:
    PORT = sys.argv[1]
    int(PORT)

if len(sys.argv) > 2:
    PORT1 = sys.argv[2]
    int(PORT1)

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://localhost:" + str(PORT))
filter = u'hello'
socket.setsockopt_string(zmq.SUBSCRIBE, filter)

while True:
    # msg = "hello"
    # socket.send_string("Hello")
    # print("{0} sent".format(msg))
    # get the reply
    reply = socket.recv_string()
    print("received reply {}".format(reply))

    # time.sleep(1)
