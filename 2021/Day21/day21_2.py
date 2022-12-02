#!/bin/python3
import sys, math
from threading import Thread, Lock

prob_input = [ line.rstrip("\n") for line in open("input.txt")]
#prob_input = [line.rstrip("\n") for line in open("test-input.txt")]

p1 = 8
p2 = 2

p1_points = 0
p2_points = 0

p1_wins = 0
p2_wins = 0

players_turn = 1

def game(p1, p1_points, p2, p2_points, players_turn, times):
    if(p1_points >= 21):
        global p1_wins
        p1_wins += times
    elif(p2_points >= 21):
        global p2_wins
        p2_wins += times
    else:
        if players_turn == 1:
            players_turn = 2 
            for combo in combos:

                temp_p1 = (combo[0] + p1) % 10
                temp_p1_points = (temp_p1 if temp_p1 !=0 else 10) + p1_points
                game(temp_p1, temp_p1_points, p2, p2_points,2, times * combo[1])
        else:
            players_turn = 1
            for combo in combos:
                temp_p2 = (combo[0] + p2) % 10
                temp_p2_points = (temp_p2 if temp_p2 !=0 else 10) + p2_points
                game(p1, p1_points, temp_p2, temp_p2_points, 1, times * combo[1])

combos = [
    (3,1),
    (4,3),
    (5,6),
    (6,7),
    (7,6),
    (8,3),
    (9,1)
]
'''
3 * 1 111
4 * 3 112, 121, 211
5 * 3 122, 212, 221
6 * 6 123, 132, 213, 231, 321, 312 
7 * 3 322, 223, 232
8 * 3 332, 323, 223
9 * 1 333
'''

game(p1, 0, p2, 0, 1, 1)
print(p1_wins)
print(p2_wins)

# while(p1_points < 1000 and p2_points < 1000):
#   p1 = (roll() + roll() + roll() + p1) % 10
#   p1_points += p1 if p1 !=0 else 10
#   if(p1_points >= 1000): break
#   p2 = (roll() + roll() + roll() + p2) % 10
#   p2_points += p2 if p2 !=0 else 10
#   # print("%d == %d, %d == %d" % (p1, p1_points, p2, p2_points))
#   # input()


# loser_pts = p1_points if p1_points < p2_points else p2_points
# print(loser_pts * roll_counter)