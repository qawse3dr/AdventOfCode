#!/bin/python3
import sys, math

prob_input = [ line.rstrip("\n") for line in open("input.txt")]
#prob_input = [line.rstrip("\n") for line in open("test-input.txt")]


def getBassinSize(point, prev_point = (0,0), basin = []):

  if (point[0] < 0 or point[1] < 0 or point[1] >= len(prob_input) or point[0] >= len(prob_input[0])): 
    return basin
  if(len(basin) == 0): #always add start point
    basin.append((point[0],point[1]))
  else:
    if(int(prob_input[point[1]][point[0]]) == 9): return basin
    else: 
      if int(prob_input[point[1]][point[0]]) > int(prob_input[prev_point[1]][prev_point[0]]) and point not in basin:
        basin.append((point[0],point[1]))
      else: return basin
  
  getBassinSize((point[0] -1,point[1]), point, basin)
  getBassinSize((point[0] +1,point[1]), point, basin)
  getBassinSize((point[0] ,point[1]-1), point, basin)
  getBassinSize((point[0] ,point[1]+1), point, basin)

  return basin
heat_sum = 0

low_points = []
for y in range(len(prob_input)):
  for x in range(len(prob_input[y])):
    lower = True
    if y > 0 and int(prob_input[y][x]) >= int(prob_input[y-1][x]): lower = False
    if x > 0 and int(prob_input[y][x]) >= int(prob_input[y][x-1]): lower = False
    if y +1 < len(prob_input) and int(prob_input[y][x]) >= int(prob_input[y+1][x]): lower = False
    if x +1 < len(prob_input[y])  and int(prob_input[y][x]) >= int(prob_input[y][x+1]): lower = False
    
    if(lower):
      # print("found: " + prob_input[y][x])
      low_points.append((x,y))
      #heat_sum += int(prob_input[y][x]) +1

bassin_lengths = []
for point in low_points:
  bassin = []
  bassin = getBassinSize(point, basin=bassin)
  bassin_lengths.append(len(bassin))

max1 = max(bassin_lengths)
bassin_lengths.pop(bassin_lengths.index(max1))

max2 = max(bassin_lengths)
bassin_lengths.pop(bassin_lengths.index(max2))

max3 = max(bassin_lengths)

print(max1 * max2 * max3)

