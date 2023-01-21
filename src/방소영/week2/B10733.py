import sys ; input = sys.stdin.readline
stack = []

n = int(input().strip())
for i in range(n):
    m = int(input().strip())
    if m == 0:
        stack.pop()
    else:
        stack.append(m)
print(sum(stack))
