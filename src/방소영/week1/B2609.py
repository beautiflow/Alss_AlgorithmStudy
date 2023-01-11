
# # 정의이용 - 맞는 풀이
# # 여기서는 n>m 일 경우에도 해줘야 함
# # 아래처럼 하면 n,m의 약수를 각각 구하는 게 아니라 for문 하나에서 구하기 가능
# # for문 안에서 if문 2개 쓴 경우
# m, n = map(int, input().split())
# a = []
# b = []
# for i in range(1,max(m,n)+1) :
#     if m%i == 0 :
#         a.append(i)
#     if n%i == 0 :
#         b.append(i)
# list = [i for i in a if i in b]

# print(max(list))
# print(int(m*n/max(list)))


# # 유클리드 호제법
# a, b = map(int, input().split())

# def gcd(a, b):
#     while b > 0:
#         a, b = b, a % b
#     return a

# def lcm(a, b):
#     return a * b // gcd(a, b)

# # 아래 코드를 안해도 되는 이유는 유클리드 호제법에서 마지막에 한번 더 해 주기 때문
# # if b>a :
# #     a, b = b, a

# print(gcd(a, b))
# print(lcm(a, b))

# # 내 풀이 - 정의 이용
# n, m = map(int, input().split(' '))
# a = []
# b = []
# for i in range(1, max(n,m)+1):
#     if n % i == 0:
#         a.append(i)
#     if m % i == 0:
#         b.append(i)
# cd = [j for j in a if j in b]
# gcd = max(cd)
# lcm = int((n* m) /gcd)
# print(gcd)
# print(lcm)

# # 유클리드 호제법 이용
# n, m = map(int, input().split(' '))

# def gcd(n, m):
#     while m > 0:
#         n, m = m, n%m
#     return n
# def lcm(n, m):
#     return int((n * m) / gcd(n ,m))

# print(gcd(n, m))
# print(lcm(n, m))

# 정의 이용 - 틀린 풀이
n , m = map(int, input().strip().split(' '))
n_div = []
m_div = []
n_mul = []
m_mul = []
# 최대공약수
for i in range(1, n+1):
    if n % i == 0:
        n_div.append(i)
for j in range(1, m+1):
    if m % j == 0:
        m_div.append(j)
print(n_div, m_div)
n_div = set(n_div)
m_div = set(m_div)
tmp = n_div.intersection(m_div)

gcd = max(list(tmp))
print(gcd)  

# 최소공배수
x = 1
while len(set(n_mul) & set(m_mul)) == 0:
    n_mul.append(n * x)
    m_mul.append(m * x)
    x +=1

lcm_list = list(set(n_mul) & set(m_mul))
lcm = lcm_list[0]
print(lcm)

