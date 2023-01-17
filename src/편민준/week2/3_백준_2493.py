import sys
input = sys.stdin.readline
print = sys.stdout.write


# n = int(input())
# tops = list(map(int , input().split()))

# receive = [0]
# for i in range(1, n):
#     cnt = 1
  
#     if tops[i] < tops[i-cnt]:
#         receive.append(i-cnt+1)
        
#     else:
#         while True:
#             cnt += 1
#             if i-cnt < 0:
#                 receive.append(0)
#                 break
#             elif tops[i] < tops[i-cnt]:
#                 receive.append(i-cnt+1)
#                 break

# print(' '.join(map(str, receive)))




n = int(input())
tops = list(map(int , input().split()))

stk = []
total = [0] * n

for i in range(n):
    t = tops[i]
    while stk and tops[stk[-1]] < t:
        stk.pop()

    if stk:
        total[i] = stk[-1] +1
    stk.append(i)

    











