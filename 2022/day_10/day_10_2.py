#!/usr/bin/python3
prob_input = [line.rstrip("\n") for line in open("test-input.txt")]

CRT = []
for i in range(6):
    CRT.append([""]* 40)

X = 1
cycles = 0


def do_cycle():
    global cycles, ans
    
    col = (cycles) % 40
    row = (cycles) // 40
    
    if (col in [X-1, X+1, X]):
        CRT[row][col] = "#"
    else:
        CRT[row][col] = "."
    cycles += 1
        
# returns cycles
def compute_op(op, asm):
    global X
    if op == "noop": do_cycle()
    elif op == "addx":
        for i in range(2): do_cycle() 
        X += int(asm.split(" ")[1])

for asm in prob_input:
    op = asm.split(" ")[0]
    compute_op(op, asm)


for row in CRT:
    print("".join(row))
