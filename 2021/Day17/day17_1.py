#!/bin/python3
start_target_x = 277
end_target_x = 318
start_target_y=-92
end_target_y =-53

# sample
# start_target_x = 20
# end_target_x = 30
# start_target_y=-10
# end_target_y =-5

# check if point is in target
def inTarget(x,y):
  return start_target_x <= x <= end_target_x and start_target_y <= y <= end_target_y

print(inTarget(25,-7))

# max_x must be distance in to end_target_x
points = []
max_x = end_target_x+1
real_max_y = 0
for x in range(1,max_x,1):
  # only test for y
  for y in range(-abs(start_target_y),abs(start_target_y)):
    vel_x = x
    vel_y = y
    cur_x = 0
    max_y = 0
    cur_y = 0
    while ( cur_x < end_target_x and cur_y > start_target_y):
      if(vel_x == 0 and (start_target_y <= cur_y <= end_target_y)): break
      cur_x += vel_x
      cur_y += vel_y
      if(vel_x != 0): vel_x -= 1
      vel_y -= 1
      if(inTarget(cur_x,cur_y)):
        print("in target with %d %d" % (cur_x, cur_y))
        real_max_y = max(real_max_y, max_y)
        if( [x,y] not in points): points.append([x,y])
        break
      else:
        max_y = max(max_y, cur_y)
print(real_max_y)
print(len(points))