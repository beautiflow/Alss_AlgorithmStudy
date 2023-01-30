from collections import deque
queue = deque()
import sys ; input = sys.stdin.readline

n = int(input().strip())
for i in range(n):
    # print(queue)
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
        
# 처음에 실패한 이유
# m = input() 으로만 해준 다음 append(int(m[5]))를 했는데 이렇게 하면 
# 정수가 1자리일 때에는 잘 출력이 되지만 2자리 이상일 때에는 되지 않음
# 1-1. strip()을 해준다음 m[-1]을 해줌 -> 2자리 이상이면 안됨
# 1-2. strip()을 해준다음 m[4:]을 해줬는데 오류가 생김
# 최종! split()까지 해줘서 push 와 정수를 따로 나눠서 담음 -> index 1이 정수임!
#   m = input().strip().split()
#     if 'push' in m:
#         queue.append(int(m[1]))                           