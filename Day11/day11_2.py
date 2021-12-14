#!/bin/python3
import sys, math

FLASH_COUNTER = 0
class Octo(object):
  flashed = False
  power = 0
  x = 0
  y = 0
  
  def __init__(self, power, x ,y):
    self.power = power
    self.x = x
    self.y = y

  def flash(self):
    

    
    if(self.power <= 9): return

    self.flashed = True
    global FLASH_COUNTER
    FLASH_COUNTER += 1
    self.power = 0
    try: 
      if ( self.x > 0 and self.y > 0): octo_array[self.y-1][self.x-1].power_up()
    except: pass
    try: 
      if (self.x > 0):octo_array[self.y][self.x-1].power_up()
    except: pass
    try: 
      if (self.x > 0): octo_array[self.y+1][self.x-1].power_up()
    except: pass

    try: 
      if ( self.y > 0): octo_array[self.y-1][self.x].power_up()
    except: pass
    try: 
      octo_array[self.y+1][self.x].power_up()
    except: pass


    try: 
      if (self.y > 0 ): octo_array[self.y-1][self.x+1].power_up()
    except: pass
    try: 
       octo_array[self.y][self.x+1].power_up()

    except: pass
    try: 
       octo_array[self.y+1][self.x+1].power_up()

    except: pass


  def power_up(self):
    if(self.flashed): return
    self.power += 1
 

  def finish_round(self):
      
    self.flashed = False 
      
      
    
    
  
  def __str__(self):
    return "str(self.power)"

#prob_input = [ line.rstrip("\n") for line in open("input.txt")]
prob_input = [line.rstrip("\n") for line in open("test-input.txt")]

octo_array = []

for y in range(len(prob_input)):
  octo_array.append([])
  for x in range(len(prob_input[y])):
    octo_array[y].append(Octo(int(prob_input[y][x]),x,y))

def print_shit():
  for line in octo_array: 
    for oct in line:
      if ( oct.power != 0):
        print(str(oct.power), end="")
      else:
        print('\033[1m'+ str(oct.power) + '\033[0m', end="")
      # print(" " + str(oct.power) + " ", end="")

    print()



print_shit()
print()
for i in range(10000):
  for line in octo_array: 
    for oct in line:
      oct.power_up()

  
  
  old_flash = -1
  while(old_flash != FLASH_COUNTER):
    old_flash = FLASH_COUNTER
    for line in octo_array: 
      for oct in line:
        oct.flash()  
  
  
  all_flash = True
  for line in octo_array: 
    for oct in line:

      if ( oct.flashed == False): 
        
        all_flash = False
      print(all_flash)
      oct.finish_round()

  if all_flash == True:
    print(i)
    break
  # print()
  # print_shit()
  # print(FLASH_COUNTER)
  # input()

print(FLASH_COUNTER)