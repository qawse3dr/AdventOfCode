#!/bin/python3

#NOTE this is not my final solution it was just something fun to do
import sys, math
from multiprocessing import Process, Array

prob_input = [ line.rstrip("\n") for line in open("input.txt")]
#prob_input = [line.rstrip("\n") for line in open("test-input.txt")]

THREAD_COUNT = 12

l_template = []
for thread_count in range(THREAD_COUNT):
  l_template.append([])

g_template = []
for thread_count in range(THREAD_COUNT):
  g_template.append([])
pairs =  {
 "test": "test"
}
first = False
for line in prob_input:

  if(line == ""): first = True
  elif(not first): l_template = list(line)
  else:
    val = line.split(" -> ")
    pairs[val[0]] = val[1]

old_template = []

def template_par(rank, letters,array):
  rounds = 25
  length = len(letters)
  total_length = length
  for r in range(rounds): total_length = total_length + total_length -1
  template = [0] * (total_length )
  for i in range(length): template[i] = letters[i]

  for r in range(rounds):
    print(r)
    old_template = template[0:length]

    for i in range(0,length-1,1):
      template[i+i] = old_template[i]
      template[i+i+1]  = pairs[str(old_template[i] + old_template[i+1])]
      template[i+i+2] = old_template[i+1]
    length = length + length -1


  local_array = [0] * 26
  for i in range(length-1):
    local_array[ord(template[i])-ord('A')] += 1

  for i in range(26):
    array[i] += local_array[i]


array = Array('i',range(26))
for i in range(26): array[i] = 0
threads = []
for i in range(THREAD_COUNT):
  start = len(l_template)//THREAD_COUNT * i
  end = len(l_template)//THREAD_COUNT * (i + 1)  + 1
  if ( i == (THREAD_COUNT-1)): end = len(l_template)

  letters= l_template[start:end]
  threads.append(Process(target=template_par, args = (i,letters,array)))
  threads[-1].start()


for thread in threads:
  thread.join()

array[ord(l_template[-1])-ord('A')] += 1
   
max_v = 0
min_v = 99999999999999999999
for i in range(26):
  if array[i] > max_v:
    max_v = array[i]
  if array[i] < min_v and array[i] != 0:
    min_v = array[i]
print(max_v - min_v)

