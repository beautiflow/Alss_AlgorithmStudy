# 풀이 1
import sys; input = sys.stdin.readline

t = int(input())
for i in range(t):
    a = input().strip()
    vps = list(a)
    sum = 0
    for j in vps:
        if j == '(':
            sum += 1
        elif j == ')' :
            sum -= 1
        if sum < 0: #if - elif 랑 if 섞은 문법
            print('NO')
            break
    if sum > 0:
        print('NO')
    elif sum == 0:
        print('YES')

# 풀이 2 - stack (append, pop) 이용
import sys; input = sys.stdin.readline

t = int(input())
for i in range(t):
    stack = []
    a = input().strip()
    for j in a :
        if j == '(':
            stack.append(j)
        elif j == ')':
            if stack:
                stack.pop()
            else:
                print('NO')
                break
    else:
        if not stack:
            print('YES')
        else:
            print('NO')



