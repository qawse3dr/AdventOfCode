#!/bin/python3
import sys, math


class Cave(object):
  caves = []
  PATH_COUNT = 0

  def __init__(self, name):
    self.name = name
    self.paths = []
  def add_path(self, path):
    if(path == "start"): return
    self.paths.append(path)
  def addPathToCave(name, path):
    for cave in Cave.caves:
      if cave.name == name: 
        cave.add_path(path)
        return

def getCave(caves,name):
  for cave in caves:
    if cave.name == name: return cave
  return None

def searchRoute(route, cave, small_visited_twice):
  if (cave.name == "end"): 
    Cave.PATH_COUNT += 1
    return 
  for path in cave.paths:
    if (not path.isupper() and getCave(route, path) != None): 
      if (small_visited_twice): continue
      else:
        route.append(getCave(Cave.caves, path))
        searchRoute(route, getCave(Cave.caves, path),True)
        route.pop()
    else:
      route.append(getCave(Cave.caves, path))
      searchRoute(route, getCave(Cave.caves, path),small_visited_twice)
      route.pop()

prob_input = [ line.rstrip("\n") for line in open("input.txt")]
#prob_input = [line.rstrip("\n") for line in open("test-input.txt")]


for line in prob_input:
  start, end = line.split("-")
  print("start " + start + " end " + end)
  if (getCave(Cave.caves, start) == None):
    # Add to cave
    Cave.caves.append(Cave(start))
  Cave.addPathToCave(start,end)
  
  if (getCave(Cave.caves, end) == None):
    # Add to cave
    Cave.caves.append(Cave(end))
  Cave.addPathToCave(end,start)


searchRoute([],getCave(Cave.caves, "start"),False)

print(Cave.PATH_COUNT)