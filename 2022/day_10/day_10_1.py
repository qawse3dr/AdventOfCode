#!/usr/bin/python3
prob_input = [line.rstrip("\n") for line in open("test-input.txt")]

ans = 0
X = 1
cycles = 0

def do_cycle():
    global cycles, ans
    cycles += 1
    if ((cycles-20) % 40) == 0 :
        print(X, cycles)
        ans += X * cycles

# returns cycles
def compute_op(op, asm):
    global X
    if op == "noop": do_cycle()
    elif op == "addx":
        for i in range(2): do_cycle() 
        X += int(asm.split(" ")[1])
        # print(int(asm.split(" ")[1]), X)


for asm in prob_input:
    op = asm.split(" ")[0]
    compute_op(op, asm)

print(ans)