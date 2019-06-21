import argparse

from pythonosc import osc_message_builder
from pythonosc import udp_client

port_num = 8002

# セットアップ
parser = argparse.ArgumentParser()
parser.add_argument("--ip", default="127.0.0.1", help="The ip of th OSC Server")
parser.add_argument("--port", type=int, default=port_num, help="The port the OSC server is listening on")
args = parser.parse_args()
client = udp_client.UDPClient(args.ip, args.port)

print("ip:127.0.0.1, port:" + str(port_num) + ", address:/filter")

def main():
  print("type int:")
  input_str = input()
  osc_msg, osc_list = make_osc(input_str)
  print(osc_list)
  client.send(osc_msg)

def make_osc(input_str):
  msg = osc_message_builder.OscMessageBuilder(address= "/filter")
  input_list = list(input_str)
  output_list = []
  for i in range(len(input_list)):
    output_list.append(int(input_list[i]))
    msg.add_arg(output_list[i])
  msg = msg.build()
  return msg, output_list

if __name__ == "__main__":
  while True:
    main()
