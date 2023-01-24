from collections import deque
queue = deque()
import sys ; input = sys.stdin.readline

n = int(input().strip())
for i in range(n):
    m = input().strip().split()
    if 'push' in m:
        queue.append(int(m[1]))
    elif 'pop' in m:
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
            queue.popleft()
    elif 'size' in m:
        print(len(queue))
    elif 'empty' in m:
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif 'front' in m:
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif 'back' in m:
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])