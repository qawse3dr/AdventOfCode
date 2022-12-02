#!/bin/python3
import sys, math
from threading import Thread, Lock

#prob_input = [ line.rstrip("\n") for line in open("input.txt")]
prob_input = [line.rstrip("\n") for line in open("test-input.txt")]

grid = []
for z in range(101):
  grid.append([])
  for y in range(101):
    grid[-1].append([])
    for x in range(101):
      grid[-1][-1].append([0]*101)
max_x = 0
max_y = 0
max_z = 0

# print(grid[0][0][0])
count = 0 
for line in prob_input:
  cords = [l.split("=")[1].split("..") for l in  line.split(" ")[1].split(",")]
  option = line.split(" ")[0]
  if(int(cords[0][0]) < -50 or int(cords[1][0]) < -50 or int(cords[2][0]) < -50): continue
  if(int(cords[0][1]) > 50 or int(cords[1][1]) > 50 or int(cords[2][1]) > 50): continue

  on = 1 if option == "on" else 0
  for z in range(int(cords[0][0]), int(cords[0][1])+1):
    for y in range(int(cords[1][0]), int(cords[1][1])+1):
      for x in range(int(cords[2][0]), int(cords[2][1])+1):
        # print(z)
        # print(y)
        # print(x)

        count += 1
        grid[z+50][y+50][x+50] = on


print(count)
count = 0
for z in grid:
  for y in z:
    for x in y:
      if ( x == 1): count += 1
  
print(count)
