import argparse

from pythonosc import osc_message_builder
from pythonosc import udp_client
import time

PORT = 1234 
ADDRESS = "/windmills"

class Osc_Client:

	def __init__(self, ip, port, address):
		self.client = udp_client.UDPClient(ip, port)
		self.address = address
		self.i = 0

	def send(self, send_list):
		print("send", send_list)
		msg = osc_message_builder.OscMessageBuilder(address=self.address)
		for i in send_list:
			msg.add_arg(i)
		msg = msg.build()
		self.client.send(msg)

	def send_random_int(self):
		self.i += 1
		send_list = [1, 1, 1,1,1,1,1,self.i]
		self.send(send_list)

	def send_input(self):
		print("type int:")
		input_str = input()
		osc_msg, osc_list = self.make_oscmessage(input_str)
		print(osc_list)
		self.client.send(osc_msg)

	def make_oscmessage(self, input_str):
		msg = osc_message_builder.OscMessageBuilder(address=self.address)
		input_list = list(input_str)
		output_list = []
		for i in range(len(input_list)):
		    output_list.append(int(input_list[i]))
		    msg.add_arg(output_list[i])
		msg = msg.build()
		return msg, output_list

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("--ip", default="127.0.0.1", help="The ip of th OSC Server")
	parser.add_argument("--port", type=int, default=PORT, help="The port the OSC server is listening on")
	parser.add_argument("--address", default=ADDRESS, help="The address the OSC server is listening on")
	args = parser.parse_args()

	oc = Osc_Client(args.ip, args.port, args.address)
	while True:
		# oc.send_input()
		oc.send_random_int()
		time.sleep(1.0)
