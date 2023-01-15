# #최대 공약수와 최소공배수

# a,b = map(int, input().split())

# n = 1
# res = []
# res2 = []


# while a != n:
#     if a % n == 0:
#         res.append(a // n)
#     n += 1

# n = 1

# while b != n:
#     if b % n == 0:
#         res2.append(b // n)
#     n += 1

# res.append(1)
# res2.append(1)

# max = 0
# while True:
#     for i in res:
#         for j in res2:
#             if i == j and max < j:
#                 max = j
#     break           

# print(max)
# print(a*b//max)

#안찾아도되는 약수를 구하기 때문에 비효율적..

#따라서 ,
#유클리드 호제법

a,b = map(int, input().split())

def gcd(a,b):
    return b if not a else gcd(b % a, a)


g = gcd(a,b)
print(g)
print(a*b//g)
