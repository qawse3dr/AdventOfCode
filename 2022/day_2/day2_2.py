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

win_dict = {
  "A": "Y",
  "B": "Z",
  "C": "X",
}

lose_dict = {
  "A": "Z",
  "B": "X",
  "C": "Y",
}

tie_dict = {
  "A": "X",
  "B": "Y",
  "C": "Z",
}

for i in prob_input:
  A, B = i.split(" ")

  if (B == "X"):
    score += score_dict[lose_dict[A]]
  elif (B == "Y"):
    score += 3 + score_dict[tie_dict[A]]
  else:
    score += score_dict[win_dict[A]] + 6

print(score)

    