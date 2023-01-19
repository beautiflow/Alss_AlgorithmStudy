import sys
input = sys.stdin.readline

testCase = int(input())
stack = []

for i in range(testCase):
    command = list(map(str,input().split()))
    if command[0] == 'push':
        stack.append(command[1])
    elif command[0] == 'pop':
        if len(stack) != 0:
            
            print(stack.pop())
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        if len(stack) != 0:
            print(0)
        else:
            print(1)
    elif command[0] == 'top':
        if len(stack) != 0:
            print(stack[len(stack)-1])
        else:
            print(-1)
