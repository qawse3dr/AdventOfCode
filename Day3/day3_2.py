#!/bin/python3

#prob_input = [ line.rstrip("\n") for line in open("input.txt")]
prob_input = [ line.rstrip("\n") for line in open("input.txt")]


def getOX(nums,index):
  #print(nums)
  if (len(nums) == 1): 
    print(nums)
    return nums
  ones = 0
  zeros = 0
  for num in nums:
    if list(num)[index] == "0": zeros += 1
    else: ones += 1
  target = ""
  if ones >= zeros:
    target = "0"

  else:
    target = "1"
  markForDelete = []
  for i in range(0,len(nums)):
    if list(nums[i])[index] == target:
      markForDelete.append(nums[i])
  for delete in markForDelete:
    nums.remove(delete)
  return getOX(nums,index+1)

def get02(nums,index):

  if (len(nums) == 1): 
    print(nums)
    return nums
  ones = 0
  zeros = 0
  for num in nums:
    if list(num)[index] == "0": zeros += 1
    else: ones += 1
  target = ""
  if ones >= zeros:
    target = "0"
  else:
    target = "1"
  markForDelete = []
  for i in range(0,len(nums)):
    if list(nums[i])[index] != target:
      markForDelete.append(nums[i])
  for delete in markForDelete:
    nums.remove(delete)
  return get02(nums,index+1)
  
gamma = []
eps = []
ans = 0
prob_input2 = prob_input.copy()
co2 = get02(prob_input2,0)
ox = getOX(prob_input,0)

print(ox)
print(co2)
#2545
print(int("".join(co2),2) * int("".join(ox),2))