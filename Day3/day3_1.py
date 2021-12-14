#!/bin/python3

#prob_input = [ line.rstrip("\n") for line in open("input.txt")]
prob_input = [ line.rstrip("\n") for line in open("input.txt")]

gamma = []
eps = []
ans = 0

for index in range(0, len(prob_input[0]),1):
  ones = 0
  zeros = 0
  for line in prob_input:
    if list(line)[index] == "0": zeros += 1
    else: ones += 1
  if ones > zeros:
    gamma.append('1')
    eps.append('0')

  else:
    gamma.append('0')
    eps.append('1')

print(int("".join(eps),2) * int("".join(gamma),2))