#!/bin/python3
import sys, math
from threading import Thread, Lock

prob_input = [ line.rstrip("\n") for line in open("input.txt")]
#prob_input = [line.rstrip("\n") for line in open("test-input.txt")]


template = []

pairs =  {
 "test": "test"
}
pairs_count = {

}
first = False
for line in prob_input:

  if(line == ""): first = True
  elif(not first): template = list(line)
  else:
    val = line.split(" -> ")
    pairs[val[0]] = val[1]
    pairs_count[val[0]] = 0

for pair in pairs:
  print(pair)

array = [0] * 26

for i in range(0,len(template)-1,1):
  pairs_count[str(template[i] + template[i+1])] += 1
  array[ord(template[i])-ord('A')] += 1
array[ord(template[-1])-ord('A')] += 1
print(pairs_count)

for r in range(40):
  new_pair_count = {}
  for key in pairs_count:new_pair_count[key] = 0
  for key in pairs_count:
    if(pairs_count[key] > 0):
      #add total
      array[ord(pairs[key])-ord('A')] += pairs_count[key]    
      #add back to list
      first, second = list(key)
      new_pair_count[first+pairs[key]] += pairs_count[key]
      new_pair_count[pairs[key]+second] += pairs_count[key]
  pairs_count = new_pair_count

old_template = []

max_array = max(array)
print(max_array)
for i in range(len(array)):
  if(array[i] == 0): array[i] = 9999999999999999999999
print(max_array - min(array))

