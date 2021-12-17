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
    packet.data = 1 if packet.children[0].data == packet.children[1].data else 0+


binary_string = bin(int(prob_input[0],16))[2:]
while(len(binary_string) % 4 != 0): binary_string = "0" + binary_string
packet = parse_packet(binary_string)

print(version_total)
print(packet.data)

