#!/bin/python3
import sys, math
from threading import Thread, Lock

prob_input = [ line.rstrip("\n") for line in open("input.txt")]
#prob_input = [line.rstrip("\n") for line in open("test-input.txt")]

p1 = 8
p2 = 2

p1_points = 0
p2_points = 0

current_roll = 0
roll_counter = 0
def roll():
  global roll_counter
  global current_roll
  roll_counter += 1
  current_roll += 1
  if(current_roll > 100): current_roll = 1
  return current_roll

while(p1_points < 1000 and p2_points < 1000):
  p1 = (roll() + roll() + roll() + p1) % 10
  p1_points += p1 if p1 !=0 else 10
  if(p1_points >= 1000): break
  p2 = (roll() + roll() + roll() + p2) % 10
  p2_points += p2 if p2 !=0 else 10
  # print("%d == %d, %d == %d" % (p1, p1_points, p2, p2_points))
  # input()


loser_pts = p1_points if p1_points < p2_points else p2_points
print(loser_pts * roll_counter)