# ps = int(input())

# stack = []

# for i in range(ps):
#     stack = []
#     ck_ps = input()

#     for j in ck_ps:
#         if j == "(":
#             stack.append(j)
#         elif j == ")":
#             if stack:
#                 stack.pop()
#             else:
#                 print("NO")
#                 break
#     else:
#         if not stack:
#             print("YES")
#         else:
#             print("NO")

# RE###################


n = int(input())

for i in range(n):
    a = (input())
    stack = []

    for j in a:
        if j == "(":
            stack.append(j)
            
        elif j == ")":
            if stack:
                stack.pop()
            else:
                print("NO")
                break
    else:
        if not stack:
            print("YES")
        else:
            print("NO")

















