numbers = [ int(line.rstrip("\n")) for line in open("input.txt")]
num3 = []


increase = 0
for i in range(0,len(numbers)-2,1):
  num3.append(numbers[i] + numbers[i+1] + numbers[i+2])
  
for i in range(1, len(num3),1):
  if(num3[i] > num3[i-1]): increase+= 1


print(increase)