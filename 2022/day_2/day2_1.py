#!/bin/python3


# prob_input = [ line.rstrip("\n") for line in open("input.txt")]
prob_input = [line.rstrip("\n") for line in open("test-input.txt")]

# a is rock
# b is paper
# c is scissors

score = 0

score_dict = {
  "X": 1,
  "Y": 2,
  "Z": 3
}

print(score_dict["X"])

for i in prob_input:
  A, B = i.split(" ")
  if (A == "A" and B == "X" or A == "B" and B == "Y" or A == "C" and B == "Z"):
    score += 3 
  elif(A == "A" and B == "Y" or A == "B" and B == "Z" or A == "C" and B == "X"):
    score += 6 
  score += score_dict[B]
print(score)

    
    
