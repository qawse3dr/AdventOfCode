#!/usr/bin/python3
prob_input = [line.rstrip("\n") for line in open("test-input.txt")]

trees = []
for prob in prob_input:trees.append(list(prob))
    
def is_visible(x,y,height, direction,start = False):
    height = int(height)
    if (direction == 0): # top
        if y < 0: return 0
        if (height <= trees[x][y] and not start) : return 1
        else: 
            return int(not start)  + is_visible(x,y -1, height, direction)
    elif (direction == 1): # bot
        if y >= len(trees): return 0
        if (height <= trees[x][y] and not start): return 1 
        else: return int(not start) + is_visible(x,y +1,height,  direction)
    elif (direction == 2): # left
        if x < 0: return 0
        if (height <= trees[x][y] and not start): return 1
        else: return int(not start) + is_visible(x -1,y,height,  direction)
    elif (direction == 3): # right
        if x >= len(trees[0]): return 0
        if (height <= trees[x][y] and not start): return 1
        else: return int(not start) + is_visible(x+1,y,height,  direction)
       
views = []
for row in range(len(trees)):
    views.append([1]*len(trees[0]))
    for col in range(len(trees[0])):
        trees[row][col] = int(trees[row][col])

cur_max = 0
for row in range(len(trees)):
    for col in range(len(trees[0])):
        for dir in range(0,4):
            views[row][col] *= is_visible(row,col, trees[row][col], dir,True)
        if views[row][col] > cur_max: cur_max = views[row][col]
print(cur_max)


