N = int(input())
i = 2

while N != 1:
    if N % i != 0:
        i += 1
        continue
    else:
        print(i)
        N = N//i
        i = 2

# if 조건과 else 조건을 바꾸면 continue 안해도 됨
# if N%m==0:
#     print(m) 
#     N = N//m
# else:
#     m += 1
