# 틀린 풀이 -> popleft를 못 씀! del 쓰면 틀림!

# import sys ; input = sys.stdin.readline

# n = int(input().strip())
# deque =[]

# for i in range(n):
#     m = input().strip().split()
#     if 'push_front' in m:
#         deque.insert(0, int(m[-1]))
#     elif 'push_back' in m:
#         deque.append(int(m[-1]))
#     elif 'pop_front' in m:
#         if len(deque) == 0:
#             print(-1)
#         else:
#             print(deque[0])
#             del deque[0]
#     elif 'pop_back' in m:
#         if len(deque) == 0:
#             print(-1)
#         else:
#             print(deque[0])
#             deque.pop()
#     elif 'size' in m:
#         print(len(deque))
#     elif 'empty' in m:
#         if len(deque) == 0:
#             print(1)
#         else:
#             print(0)
#     elif 'front' in m:
#         if len(deque) == 0:
#             print(-1)
#         else:
#             print(deque[0])
#     elif 'back' in m:
#         if len(deque) == 0:
#             print(-1)
#         else:
#             print(deque[-1])


# deque를 사용해서 푼 풀이
import sys ; input = sys.stdin.readline
from collections import deque
deque = deque()

n = int(input().strip())


for i in range(n):
    m = input().strip().split()
    if 'push_front' in m:
        deque.appendleft(int(m[-1]))
    elif 'push_back' in m:
        deque.append(int(m[-1]))
    elif 'pop_front' in m:
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[0])
            deque.popleft()
    elif 'pop_back' in m:
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[-1])
            deque.pop()
    elif 'size' in m:
        print(len(deque))
    elif 'empty' in m:
        if len(deque) == 0:
            print(1)
        else:
            print(0)
    elif 'front' in m:
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[0])
    elif 'back' in m:
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[-1])