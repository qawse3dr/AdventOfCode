#!/usr/bin/python3
import sys
prob_input = [line.rstrip("\n") for line in open("test-input.txt")]

cmds = []
outputs = []

for line in prob_input:
    if line[0] == "$":
        cmds.append(line[2::])
        outputs.append([])
    else:
        outputs[-1].append(line)

class Dir:
    def __init__(self, name):
        self.name = name
        self.files = []
        self.dirs = []
        self.size = -1
    def add_file(self, name, size):
        if ((name, size) in self.files): return
        self.files.append((name,size))
    def add_dir(self, name):
        if (name in self.dirs): return
        self.dirs.append(name)
    def get_size(self):
        if self.size != -1: return self.size
        s = 0
        for file in self.files: s += int(file[1])

        for d in self.dirs:
            
            s += get_dir_size(d)
        self.size = s
        return s

# keeps track of directories
directory_stack = []

# directories
dirs = []

def add_dir(dir_name):

    for d in dirs:
        if d.name == dir_name:
            return
    dirs.append(Dir(dir_name))

def add_file(dir_name, file, size):

    for d in dirs:
        if d.name == dir_name:
            d.add_file(file, size)
            return
def add_dir_n(dir_name, name):
    for d in dirs:
        if d.name == dir_name and not(dir_name in d.dirs):
            d.add_dir(name)
            return
        
def get_dir_size(name):
    for d in dirs:
            if d.name == name:
                return d.get_size()
    return 0

for i in range(len(cmds)):
    if (cmds[i].startswith("cd")):
        path = cmds[i][3::]
        # full path
        if (path == "/"):
            directory_stack = ["/"]
            add_dir("/")
        elif (path == ".."):
            if (len(directory_stack) != 1):
                directory_stack.pop()
        else:
            add_dir("/".join(directory_stack) + "/" + path)
            directory_stack.append(path)
    else:
        for o in outputs[i]:
            if (o.startswith("dir")): add_dir_n("/".join(directory_stack),  "/".join(directory_stack)  + "/" + o.split(" ")[1])
            else:
                file_info = o.split(" ")
                add_file("/".join(directory_stack), file_info[1], file_info[0])


total = dirs[0].get_size()
left = 70000000 - total
sizes = []
for d in dirs:
    if (d.get_size() >= 30000000 - left):
        sizes.append(d.get_size())


print(min(sizes))
