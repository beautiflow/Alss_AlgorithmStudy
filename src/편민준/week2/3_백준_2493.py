import sys
input = sys.stdin.readline
# print = sys.stdout.write


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
tops = list(map(int, input().split()))
stack = []
res = []

for i in range(n):
    h = tops[i]
    if stack:
        while stack:
            if stack[-1][0] < h:
                stack.pop()
                if not stack:
                    res.append(0)
            elif stack[-1][0] > h:
                res.append(stack[-1][1]+1)
                break
        stack.append([h,i])
    else:
        res.append(0)
        stack.append([h,i])

print(" ".join(map(str,res)))