from collections import deque
queue = deque()
import sys ; input = sys.stdin.readline

# 앞 뒤로 원소를 뽑을 수 있는게 아니라 첫번째 원소밖에 못 뽑음!
# n, a = map(int, input().strip().split())
# aList = list(map(int, input().strip().split()))
# for i in range(1, n+1):
#     queue.append(i)
# count = 0

# for m in aList:
#     while m != queue[0] and m != queue[-1]: 
#             if queue.index(m) < (len(queue) // 2):
#                 queue.append(queue.popleft())
#                 count += 1
#             elif queue.index(m) >= (len(queue) // 2) :
#                 queue.appendleft(queue.pop())
#                 count += 1
#     if m == queue[0]:
#         queue.popleft()   
#     elif m == queue[-1]:
#         queue.pop()
   
# print(count)

# 다시
n, a = map(int, input().strip().split())
aList = list(map(int, input().strip().split()))
for i in range(1, n+1):
    queue.append(i)
count = 0

for m in aList:
    while True:
        if m == queue[0]:
            queue.popleft()
            break
        else:
            if queue.index(m) <= (len(queue) // 2) :
                queue.append(queue.popleft())
                count += 1
            elif queue.index(m) > (len(queue) // 2) :
                queue.appendleft(queue.pop())
                count += 1
  
print(count)




