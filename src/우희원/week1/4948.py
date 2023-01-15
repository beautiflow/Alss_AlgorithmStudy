def is_prime(n) :
    if n == 1 :
        return False
    else :
        for i in range(2, int(n**0.5)+1) :
            if n%i == 0 :
                return False
        return True

value = list(range(123456*2))
prime = list()

for i in value :
    if is_prime(i) :
        prime.append(i)

while 1 :
    n = int(input())
    cnt = 0
    if n == 0 :
        break
    for i in prime :
        if n < i <= 2*n :
            cnt += 1
    print(cnt)




# 시간초과
# def is_prime(n) :
#     if n == 1 :
#         return False
#     else :
#         for i in range(2, int(n**0.5)+1) :
#             if n%i == 0 :
#                 return False
#         return True
    
# while True :
#     n = int(input())
#     cnt = 0
#     if n == 0 :
#         break
#     for i in range(n+1, 2*n+1) :
#         if is_prime(i) == True :
#             cnt += 1
#     print(cnt)