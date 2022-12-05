#!/usr/bin/python3


# prob_input = [ line.rstrip("\n") for line in open("input.txt")]
prob_input = [line.rstrip("\n") for line in open("test-input.txt")]

score = 0
for i in range(len(prob_input)):

  first_half = prob_input[i][0:len(prob_input[i])//2] 
  second_half = prob_input[i][len(prob_input[i])//2::] 



  shared_types = []
  for c in first_half:
    if c in second_half and c not in shared_types:
      shared_types.append(c)

  for c in shared_types: 
    if c.isupper(): score += ord(c) - ord('A') + 27
    else : score += ord(c) - ord('a') + 1
print(score)
