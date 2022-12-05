#!/usr/bin/python3

# prob_input = [ line.rstrip("\n") for line in open("input.txt")]
prob_input = [line.rstrip("\n") for line in open("test-input.txt")]

stacks = []

#get the stacks
row = 0
while prob_input[row][1] != "1":
  for i in range(1, len(prob_input[row]), 4):
    if len(stacks)  < i:
      stacks.append([])
    if prob_input[row][i] != ' ':
      stacks[i//4] = [prob_input[row][i]] + stacks[i//4]
  row += 1

row += 2

# for stack in stacks:
#   print(stack)

for cmd in prob_input[row::]:
  args = cmd.split(' ')
  move_num = int(args[1])
  from_ = int(args[3])
  to_ = int(args[5])

  for i in range(0,move_num):
    stacks[to_ -1].append(stacks[from_ -1][-1])
    stacks[from_ -1 ].pop()
  # for stack in stacks:
  #   print(stack)


for stack in stacks:
  if (len(stack) != 0): print(stack[-1],end="")
print()