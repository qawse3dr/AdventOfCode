#!/bin/python3
import sys, math
from threading import Thread, Lock


class Packet():

  def __init__(self):
    self.data = ""
    self.version = 0
    self.ID = 0
    self.total_length = 0
    # operator shit
    self.op = False
    self.len_id = -1 #-1 so i know it isn't valid
    self.len_val = 0 #

    self.children = []

  def __repr__(self):
    if(self.op == False): return "version: " + str(self.version) + " ID: " + str(self.ID) + " data: " + str(self.data) + " length: " + str(self.total_length)
    else: return "version: " + str(self.version) + " ID: " + str(self.ID) + " len_id: " + str(self.len_id) + " len_val: " + str(self.len_val) + " length: " + str(self.total_length)
prob_input = [ line.rstrip("\n") for line in open("input.txt")]
#prob_input = [line.rstrip("\n") for line in open("test-input.txt")]


# binary_string = bin(int("D2FE28",16))




# packets = []
# message_length = 3 # first message is 3
# cur_binary = ""
# STATE = pack_version

# for line in prob_input:
#   packets.append(Packet())
#   for bit in binary_string[2:]:
#     cur_binary += str(bit)

#     #keeps track of how long it is
#     if (STATE != pack_padding): packets[-1].total_length += 1 

#     if(STATE == pack_info and cur_binary[0] == "0"):
#       STATE = pack_info_last_message

#     if(len(cur_binary) == message_length):
#       if(STATE == pack_version): 
#         STATE = pack_ID
#         packets[-1].version = int(cur_binary,2)
#       elif(STATE == pack_ID): 
#         packets[-1].ID = int(cur_binary,2)
#         if(packets[-1].ID == 4):
#           STATE = pack_info
#           message_length = 5
#         else:
#           STATE = pack_op
#            packets[-1].op = True # its an operation
#           message_length = 1
#       elif ( STATE == pack_op): # get length for sub-packets
#           packets[-1].len_id = int(cur_binary,2)
#           if(packets[-1].len_id == 0):
#             message_length = 15
#           else:
#             message_length = 11
#           STATE = pack_message_length
#       elif ( STATE == pack_message_length):
#           packets[-1].len_val = int(cur_binary,2)
#       elif (STATE == pack_info_last_message or STATE == pack_info):
#         packets[-1].data +=cur_binary[1:]
#         if ( STATE == pack_info_last_message):
#           STATE == pack_padding
#           message_length = 8 - packets[-1].total_length % 8
#           if(message_length == 8): #skip padding
#             STATE = pack_version
#           packets[-1].data = int(packets[-1].data,2)
#           if(not packets[-1].op): 
#             #figure out padding length

#           else:

#       cur_binary = ""

# print(packets)

version_total = 0
def parse_packet(packet_str):
  global version_total

  packet = Packet()
  
  # Always grab version and id
  packet.version = int(packet_str[0:3],2)
  version_total += packet.version
  packet.ID = int(packet_str[3:6],2)
  packet.total_length += 6

  if(packet.ID == 4): parse_data_pack(packet, packet_str)
  else: parse_op_pack(packet, packet_str)
    
  print(packet)
  

  return packet

def parse_data_pack(packet, packet_str):
  first_bit = 1
  while(first_bit != 0):
    first_bit = int(packet_str[packet.total_length:packet.total_length+1])
    packet.data += packet_str[packet.total_length+1:packet.total_length+5]
    packet.total_length += 5
  packet.data = int(packet.data,2)
  # DONT DO PADDING
  #while(packet.total_length % 4 != 0): packet.total_length += 1

def parse_op_pack(packet, packet_str):
  packet.op = True
  # get length id
  packet.len_id = int(packet_str[packet.total_length:packet.total_length+1], 2)
  packet.total_length += 1
  if (packet.len_id == 0):
    packet.len_val = int(packet_str[packet.total_length:packet.total_length+15], 2)
    packet.total_length += 15 
    length = 0
    while(length < packet.len_val):
      child = parse_packet(packet_str[packet.total_length:])
      packet.children.append(child)
      packet.total_length += child.total_length
      length += child.total_length
  else:
    packet.len_val = int(packet_str[packet.total_length:packet.total_length+11], 2)
    packet.total_length += 11
    for _ in range(packet.len_val):
      child = parse_packet(packet_str[packet.total_length:])
      packet.children.append(child)

      packet.total_length += child.total_length
  if( packet.ID == 0 ):
    print("sum")
    sum = 0
    for child in packet.children:
      sum += child.data
    packet.data = sum
  elif( packet.ID == 1 ):
    print("product")
    product = 1
    for child in packet.children:
      product *= child.data
    packet.data = product
  elif( packet.ID == 2 ):
    print("min")
    min_val = 9999999999999999
    for child in packet.children:
      min_val = min(min_val, child.data)
    packet.data = min_val
  elif( packet.ID == 3 ):
    print("max")
    max_val = 0
    for child in packet.children:
      max_val = max(max_val, child.data)
    packet.data = max_val
  elif( packet.ID == 5 ):
    print("greater")
    packet.data = 1 if packet.children[0].data > packet.children[1].data else 0

  elif( packet.ID == 6 ):
    print("less")
    packet.data = 1 if packet.children[0].data < packet.children[1].data else 0

  elif( packet.ID == 7 ):
    print("equal")
    packet.data = 1 if packet.children[0].data == packet.children[1].data else 0


binary_string = bin(int(prob_input[0],16))[2:]
while(len(binary_string) % 4 != 0): binary_string = "0" + binary_string
packet = parse_packet(binary_string)

print(version_total)
print(packet.data)

