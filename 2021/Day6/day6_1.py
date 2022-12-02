#!/bin/python3

prob_input = [ line.rstrip("\n") for line in open("input.txt")]
#prob_input = [ line.rstrip("\n") for line in open("test-input.txt")]

fish = prob_input[0].split(",")
for fish_i in range(0,len(fish),1):
  fish[fish_i] = int(fish[fish_i])

print(fish)
for i in range(0,256,1):
  print(i)
  add_fish = 0
  for fish_i in range(0,len(fish),1):
    if(fish[fish_i] == 0): 
      fish[fish_i] = 7
      add_fish += 1
    fish[fish_i] -= 1
  for fish_i in range(0,add_fish,1):
    fish.append(8)
print(len(fish))