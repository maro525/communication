import sys
import zmq

PORT = 5556

if (len(sys.argv) != 2):
    print("Usage: # python3 {} <channel>".format(sys.argv[0]))
    sys.exit(1)

ch = sys.argv[1]

context = zmq.Context()

socket = context.socket(zmq.SUB)
socket.connect("tcp://localhost:" + str(PORT))

socket.setsockopt_string(zmq.SUBSCRIBE, ch)

while True:
    string = socket.recv_string()
    ch, data = string.split()

    print("Ch {0} -> {1} received".format(ch, data))
