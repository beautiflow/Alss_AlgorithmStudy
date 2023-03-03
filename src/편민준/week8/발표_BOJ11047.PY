import sys
input = sys.stdin.readline

n, k = map(int,input().split())

ns = []

for i in range(n):
    ns.append(int(input()))

ns = ns[::-1]
cnt = 0 

for i in ns:
    if k < i:
        continue
        
    elif k >= i:
        while k >= i:
            k -= i
            cnt += 1
    
    if k == 0:
      break

print(cnt)