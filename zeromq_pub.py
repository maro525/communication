import zmq
import time

context = zmq.Context()

PORT = 5556

socket = context.socket(zmq.PUB)
socket.bind("tcp://*:" + str(PORT))

i = 0

while True:
    i += 1

    for ch in range(1, 4):
        data = ch * i
        socket.send_string("{0} {1}".format(ch, data))
        print("Ch {0} <- {1} sent".format(ch, data))

    time.sleep(1)
