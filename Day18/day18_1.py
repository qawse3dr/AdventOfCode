#!/bin/python3
import sys, math
from threading import Thread, Lock

#prob_input = [ line.rstrip("\n") for line in open("input.txt")]
prob_input = [line.rstrip("\n") for line in open("test-input.txt")]

def split_str_(string):
  rtn = []
  num = ""
  for x in string:
    if(x == "[" or x == "]" or x == ","):
      if(num != ""): rtn.append(num)
      rtn.append(x)
      num = ""
    else:
      num += x
  return rtn
  
def add_(str1, str2):
  return ["["] + str1 + [","] + str2 + ["]"]

def split():
  global str_
  for i in range(len(str_)):
    if(str_[i].isdigit()):
      num = int(str_[i])
      if(num < 10): continue
      str_ = str_[:i] + split_str_("[%d,%d]" % (num//2, math.ceil(num/2))) + str_[i+1:]
      return True
  return False

def explode():
  global str_
  stackCount = 0
  for i in range(len(str_)):
    if (str_[i] == "["):  stackCount += 1
    elif (str_[i] == "]"): 
      stackCount -= 1
      if(stackCount > 3):
        left = str_[i-3]
        right = str_[i-1]
        str_ = str_[:i-4] + ["0"] + str_[i+1:]
        for j in range(i-3,len(str_)):
          if (str_[j].isdigit()):
            str_[j] = str(int(str_[j]) + int(right))
            break
        for j in range(i-5,0,-1):
          if (str_[j].isdigit()):
            str_[j] = str(int(str_[j]) + int(left))
            break
        return True
  return False

def reduce_array():
  while(explode()): pass
  if(split()): reduce_array()

def calc_mag(array):  
  if(type(array) == int): return int(array)
  return calc_mag(array[0])*3 + calc_mag(array[1]) * 2



def reduce(val):
  global str_
  str_ = val
  reduce_array()
  return str_

max_sum = 0 ## part 2
for i in range(0, len(prob_input)):
  for j in range(0, len(prob_input)):
    if(i == j): continue
    val1 = split_str_(prob_input[i])
    val2 = split_str_(prob_input[j])

    val1 = reduce(val1)
    val1 = reduce(val2)


    sum_1 = add_(val1, val2)
    sum_2 = add_(val2, val1)

    sum_1 = reduce(sum_1)
    sum_2 = reduce(sum_2)

    max_sum = max(max_sum, calc_mag(eval("".join(sum_1))), calc_mag(eval("".join(sum_2))))

print(max_sum)

## part 1
# sum_ = split_str_(prob_input[0])
# str_ = sum_
# reduce_array()

# for i in range(1, len(prob_input)):
#   val = split_str_(prob_input[i])
#   str_ = val
#   reduce_array()
#   val = str_
#   sum_ = add_(sum_, val)

#   str_ = sum_
#   reduce_array()
#   sum_ = str_
#   print(sum_)

# print()

# # print(sum_)
# print()
