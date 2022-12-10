#!/usr/bin/python3
prob_input = [line.rstrip("\n") for line in open("test-input.txt")]

trees = []
for prob in prob_input:trees.append(list(prob))
    
def is_visible(x,y,height, direction,start = False):
    height = int(height)
    if (direction == 0): # top
        if y < 0: return True
        if (height <= trees[x][y] and not start) : return False
        else: return is_visible(x,y -1, height, direction)
    elif (direction == 1): # bot
        if y >= len(trees): return True
        if (height <= trees[x][y] and not start): return False
        else: return is_visible(x,y +1,height,  direction)
    elif (direction == 2): # left
        if x < 0: return True
        if (height <= trees[x][y] and not start): return False
        else: return is_visible(x -1,y,height,  direction)
    elif (direction == 3): # bot
        if x >= len(trees[0]): return True
        if (height <= trees[x][y] and not start): return False
        else: return is_visible(x+1,y,height,  direction)
    
visible = 0
for row in range(len(trees)):
    for col in range(len(trees[0])):
        trees[row][col] = int(trees[row][col])

for row in range(len(trees)):
    for col in range(len(trees[0])):
        for dir in range(0,4):
            if (is_visible(row,col, trees[row][col], dir,True)):
                visible += 1
                print(row, col)
                break
    
print(visible)