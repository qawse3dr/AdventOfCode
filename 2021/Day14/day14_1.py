#!/bin/python3
import sys, math
from threading import Thread, Lock

prob_input = [ line.rstrip("\n") for line in open("input.txt")]
#prob_input = [line.rstrip("\n") for line in open("test-input.txt")]


template = []

pairs =  {
 "test": "test"
}
first = False
for line in prob_input:

  if(line == ""): first = True
  elif(not first): template = list(line)
  else:
    val = line.split(" -> ")
    pairs[val[0]] = val[1]

for pair in pairs:
  print(pair)


old_template = []

for r in range(25):
  print(r)
  old_template = template
  length = len(template)
  template = [0] * (length + (length -1))
  for i in range(0,length-1,1):
    template[i+i] = old_template[i]
    template[i+i+1] = pairs[str(old_template[i] + old_template[i+1])]
    template[i+i+2] = old_template[i+1]


array = [0] * 26
for i in range(len(template)):
  array[ord(template[i])-ord('A')] += 1

   
print(array)
max_array = max(array)
for i in range(len(array)):
  if(array[i] == 0): array[i] = 9999999999999999999999
print(max_array - min(array))

