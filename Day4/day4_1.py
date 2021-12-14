#!/bin/python3

prob_input = [ line.rstrip("\n") for line in open("input.txt")]
#prob_input = [ line.rstrip("\n") for line in open("test-input.txt")]

# Gets rolls
rolls = prob_input[0].split(",")
print(rolls)

# Gets board
boardIndex = 0
boards = [[]]
for i in range(2, len(prob_input), 1):
  if(prob_input[i] == ""):
    boardIndex += 1
    boards.append([])
  else:
    boards[boardIndex].append(prob_input[i].split(" "))
    boards[boardIndex][len(boards[boardIndex])-1] = [i for i in boards[boardIndex][len(boards[boardIndex])-1] if i != ""]


winners = []
for roll in rolls:
  for board in boards:
    for row in range(0, len(board), 1):
      for i in range(0, len(board[row]), 1):
        if roll == board[row][i]:
          board[row][i] = ""
  for board in boards:
    for i in range(0,len(board),1):
      col = 0
      row = 0
      for j in range(0,len(board),1):
        if(board[i][j] == ""): row += 1
        if(board[j][i] == ""): col += 1

      if (col == len(board[0]) or row == len(board[0])):
        winners.append(board)
        break
        
  for winner in winners:
    if winner != None: 
      count = 0
      for row in winner:
        for i in row:
          if i != "": count += int(i)
      print(int(roll) * count)
      boards.remove(winner)
  winners = []
