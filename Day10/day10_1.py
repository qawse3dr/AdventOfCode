#!/bin/python3
import sys, math

prob_input = [ line.rstrip("\n") for line in open("input.txt")]
#prob_input = [line.rstrip("\n") for line in open("test-input.txt")]

paring = {"(" : ")","[" : "]","{" : "}","<" : ">",}

# part 1
#target_value = {")": 3,"]": 57,"}": 1197,">": 25137,}

# part 2
target_value = {"(": 1,"[": 2,"{": 3,"<": 4,}
starters = ["[", "(", "<", "{"]


stack = []
sussy_baka = []
count = 0
for line in prob_input:
  stack = []
  cor = False
  for char in line:
    
    # print(stack)
    if char in starters:
      stack.append(char)
    else:
      if (paring[stack[len(stack)-1]] ==  char):
        stack.pop()

      else:
        cor = True
        break

  if(not cor):
    count = 0
    for fuck_this in reversed(stack):
      count *= 5
      count += target_value[fuck_this]
    sussy_baka.append(count)

sussy_baka.sort()

print(sussy_baka[int(len(sussy_baka)/2)])
