from collections import deque
n,k = map(int,input().split()) # 7 , 3

deq = deque(range(1, n+1))
res =[]

while deq:
    for _ in range(k-1):
        deq.append(deq.popleft())
    res.append(deq.popleft())



print('<{}>' .format(', '.join(map(str,res)))) 


