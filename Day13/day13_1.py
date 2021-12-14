#!/bin/python3
import sys, math

prob_input = [ line.rstrip("\n") for line in open("input.txt")]
#prob_input = [line.rstrip("\n") for line in open("test-input.txt")]

first = True
points = []
grid = []
instructions = []
for line in prob_input:
  if ( line == ""): first = False
  elif ( first): points.append(line.split(","))
  else: instructions.append(line.split(" ")[2].split("="))
max_x = 0
max_y = 0

for i in range(len(points)): points[i] = [int(points[i][0]), int(points[i][1])]
for point in points:

  if (point[0] > max_x): max_x = point[0]
  if (point[1] > max_y): max_y = point[1]

for y in range(max_y + 1):
  grid.append(["."]* (max_x+1))
  
grid_x = max_x + 1
grid_y = max_y + 1
#build grid
for point in points:
  grid[point[1]][point[0]] = "#"

for instruct in instructions:
  if (instruct[0] == "x"):
    new_grid_x = int(instruct[1])

    for y in range(0,grid_y):
      for x in range(new_grid_x):
        if(grid[y][x] == "#"): continue
        try:
          grid[y][x] = grid[y][new_grid_x + new_grid_x-x]
        except: pass

    grid_x = new_grid_x
  else:
    new_grid_y = int(instruct[1])

    for y in range(0,new_grid_y):
      for x in range(grid_x):
        if(grid[y][x] == "#"): continue
        try:
          grid[y][x] = grid[ new_grid_y + new_grid_y-y][x]
        except: pass
    grid_y = new_grid_y
  #break # part 1
count = 0
for y in range(grid_y):
  for x in range(grid_x):
    print(grid[y][x], end = "")
    if( grid[y][x] == "#"): count += 1
  print()
print(count)