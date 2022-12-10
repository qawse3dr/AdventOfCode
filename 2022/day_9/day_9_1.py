#!/usr/bin/python3
prob_input = [line.rstrip("\n") for line in open("test-input.txt")]


points_visited = [(0,0)]

head_pos = [0,0]

move_stack = [[0,0]*10]
print(move_stack)
tail_pos = [0,0]

def update():
    if (head_pos[1] != tail_pos[1]):
        if(head_pos[0] != tail_pos[0] and (abs(head_pos[1] - tail_pos[1]) + abs(head_pos[0] - tail_pos[0])) > 2):
            delta_y = 1 if (head_pos[1] > tail_pos[1]) else -1
            delta_x = 1 if (head_pos[0] > tail_pos[0]) else -1
            move(delta_x, delta_y)
        elif(abs(head_pos[1] - tail_pos[1]) > 1):
            if (head_pos[1] > tail_pos[1]): move(0,1)
            else: move(0,-1)
    elif(head_pos[0] != tail_pos[0]):
         if(abs(head_pos[0] - tail_pos[0]) > 1):
            if (head_pos[0] > tail_pos[0]): move(1,0)
            else: move(-1,0)

def move(delta_x, delta_y):
    tail_pos[0] += delta_x
    tail_pos[1] += delta_y
    tup = tail_pos[0],tail_pos[1]
    if (not(tup in points_visited)): 
        points_visited.append(tup) 
for prob in prob_input:
    (D,L) = prob.split(" ")
    
    for _ in range(int(L)):
        match D:
            case "R":
                head_pos[0] += 1
            case "L":
                head_pos[0] -= 1
            case "U":
                head_pos[1] -= 1
            case "D":
                head_pos[1] += 1
        update()
    
print(len(points_visited))