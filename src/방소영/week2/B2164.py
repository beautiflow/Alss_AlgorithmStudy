from collections import deque
queue = deque()
import sys ; input = sys.stdin.readline

n = int(input().strip())

for i in range(n, 0, -1):
    queue.append(i)

for j in range(n-1):
    queue.pop()
    queue.appendleft(queue.pop())

print(*list(queue))

