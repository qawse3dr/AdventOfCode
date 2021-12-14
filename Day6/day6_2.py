#!/bin/python3
import math
prob_input = [ line.rstrip("\n") for line in open("input.txt")]
#prob_input = [ line.rstrip("\n") for line in open("test-input.txt")]

fish_lives = [0] * 9

fish = prob_input[0].split(",")
for fish_i in range(0,len(fish),1):
  fish_lives[int(fish[fish_i])] += 1


for i in range(0,256,1):
  new_fish_lives = [0] * 9
  new_fish_lives[0] = fish_lives[1]
  new_fish_lives[1] = fish_lives[2]
  new_fish_lives[2] = fish_lives[3]
  new_fish_lives[3] = fish_lives[4]
  new_fish_lives[4] = fish_lives[5]
  new_fish_lives[5] = fish_lives[6]
  new_fish_lives[6] = fish_lives[7] + fish_lives[0]
  new_fish_lives[7] = fish_lives[8]
  new_fish_lives[8] = fish_lives[0]

  fish_lives = new_fish_lives

print(sum(fish_lives))
  


