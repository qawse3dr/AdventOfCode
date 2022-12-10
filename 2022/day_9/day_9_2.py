#!/usr/bin/python3
prob_input = [line.rstrip("\n") for line in open("test-input.txt")]

points_visited = [(0,0)]

head_pos = [0,0]
pos_stack = [[0,0] for i in range(9)]


def update(head, tail, append):
    if (head[1] != tail[1]):
        if(head[0] != tail[0] and (abs(head[1] - tail[1]) + abs(head[0] - tail[0])) > 2):
            delta_y = 1 if (head[1] > tail[1]) else -1
            delta_x = 1 if (head[0] > tail[0]) else -1
            tail = move(delta_x, delta_y, tail,append)
        elif(abs(head[1] - tail[1]) > 1):
            if (head[1] > tail[1]): tail = move(0,1,tail, append)
            else: tail = move(0,-1, tail,append)
    elif(head[0] != tail[0]):
         if(abs(head[0] - tail[0]) > 1):
            if (head[0] > tail[0]): tail = move(1,0, tail,append)
            else: tail = move(-1,0, tail,append)
    return tail
def move(delta_x, delta_y, tail, append):
    tail[0] += delta_x
    tail[1] += delta_y
    tup = tail[0],tail[1]
    if (append and not(tup in points_visited)): 
        points_visited.append(tup) 
    return tail
for prob in prob_input:
    (D,L) = prob.split(" ")
    
    for _ in range(int(L)):
        print(D)
        match D:
            case "R":
                head_pos[0] += 1
            case "L":
                head_pos[0] -= 1
            case "U":
                head_pos[1] -= 1
            case "D":
                head_pos[1] += 1
        
        pos_stack[0] = update(head_pos, pos_stack[0], False)
        for i in range(0,7):
            pos_stack[i+1] = update(pos_stack[i], pos_stack[i+1],False)
        pos_stack[8] = update(pos_stack[7], pos_stack[8], True)
        # print(pos_stack)
print(len(points_visited))