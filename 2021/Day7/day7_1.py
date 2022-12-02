#!/bin/python3
import sys
prob_input = [ line.rstrip("\n") for line in open("input.txt")]
#prob_input = [line.rstrip("\n") for line in open("test-input.txt")]

prob_input = [ int(x) for x in prob_input[0].split(",")]

max_x = max(prob_input)

print(prob_input)
print(max_x)

# try all combos
min_fuel = sys.maxsize
for x in range(0,max_x,1):
  fuel = 0
  skip = False
  for crab in prob_input:

    loop = abs(crab - x)
    for i in range(loop): 
      fuel += i + 1
    if(fuel > min_fuel):
      skip = True
      break 
  if skip: continue
  else: 
    if fuel < min_fuel: min_fuel = fuel

print(min_fuel)