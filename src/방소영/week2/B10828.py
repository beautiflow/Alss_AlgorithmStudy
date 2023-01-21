import sys ; input = sys.stdin.readline

n = int(input().strip())
stack =[]

for i in range(n):
    m = input().strip().split()
    if 'push' in m:
        stack.append(int(m[-1]))
    elif 'pop' in m:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
            stack.pop()
    elif 'size' in m:
        print(len(stack))
    elif 'empty' in m:
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif 'top' in m:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])

# 주의 해야 하는 부분!
# stack.append(int(m[-1])) -> int형으로 넣어주어야 함
