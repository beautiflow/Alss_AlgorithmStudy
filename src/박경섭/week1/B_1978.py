a = int(input())

arr = list(map(int, input().split()))
count = 1
numcount=0

for num in arr:
  nop = 0
  if num > 1:
    for i in range(2, num):
      if num % i == 0:
        nop += 1
    if nop == 0:
      numcount += 1
  
      

print(numcount)
      