#!/usr/bin/python3


# prob_input = [ line.rstrip("\n") for line in open("input.txt")]
prob_input = [line.rstrip("\n") for line in open("test-input.txt")]

count = 0
for pair in prob_input:
  a,b = pair.split(",")

  
  if ((int(a.split("-")[0]) >= int(b.split("-")[0]) and int(a.split("-")[1]) <= int(b.split("-")[1])) or
    (int(b.split("-")[0]) >= int(a.split("-")[0]) and int(b.split("-")[1]) <= int(a.split("-")[1]))
  ): count += 1

print(count)

