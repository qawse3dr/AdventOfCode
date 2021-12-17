from collections import deque
from dataclasses import dataclass
import bisect

@dataclass
class Node:
  distance: int
  parent = None
  x: int
  y: int
  def __init__(self, x,y,weight):
    self.x = x
    self.y = y
    self.parent = None
    self.distance = None
    self.weight = weight
  def __getitem__(self, i):
    return self.distance
  def __lt__(self,other):
    return self.distance < other.distance
prob_input = [ line.rstrip("\n") for line in open("input.txt")]
#prob_input = [line.rstrip("\n") for line in open("test-input.txt")]

def calc_weight(weight,factor):
  for _ in range(factor):
    weight += 1
    if weight > 9: weight = 1

  return weight
  
grid = []
visited = []
for y in range(len(prob_input) * 5):
  grid.append([])
  visited.append([])
  for x in range(len(prob_input[0]) * 5):

    visited[y].append(False)
    grid[y].append(Node(x,y,calc_weight(int(prob_input[y %len(prob_input)][x % len(prob_input[0])]),y//len(prob_input) + x//len(prob_input[0]) )))
visited_q = []

def nodeKey(node):
  return node.distance
bisect.insort(visited_q,grid[0][0])
grid[0][0].distance = 0
visited[0][0] = True

def print_path(path):
  for y in range(len(grid)):
    for x in range(len(grid[0])):
      if not path[y][x]:
        print("_",end = "")
      else:
        print(grid[y][x].weight,end = "")
    print()

print_path(grid)

x_length = len(grid[0])
y_length =  len(grid)
while (visited_q):
  cur = visited_q[0]
  visited_q.remove(cur)
  x = cur.x
  y = cur.y

  queue = [] #neighbours
  if(x > 0  and not visited[y][x-1]): queue.append(grid[y][x-1])
  if(y > 0 and  not visited[y-1][x]): queue.append(grid[y-1][x])
  if(x < x_length-1 and not  visited[y][x+1]): queue.append(grid[y][x+1])
  if(y < y_length-1 and not  visited[y+1][x]): queue.append(grid[y+1][x])
  
  for neighbour in queue:
    neighbour.distance = cur.distance + neighbour.weight

    visited[neighbour.y][neighbour.x] = True
    bisect.insort(visited_q,neighbour)
    neighbour.parent = cur

print(grid[-1][-1].distance)

