#!/bin/python3

prob_input = [ line.rstrip("\n") for line in open("input.txt")]

x = 0
y = 0

for line in prob_input:
    cmd = line.split(" ")[0]
    distance = int(line.split(" ")[1])

    if(cmd == "forward"):
        x += distance
    elif(cmd == "down"):
        y += distance  
    elif(cmd == "up"):
        y -= distance
    else:
        print("you fucked up")
ans = x * y

print(ans)