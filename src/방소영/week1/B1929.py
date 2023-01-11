# M이상 N이하의 소수 구하기

# # 풀이1: 소수의 정의 이용하기 -> 시간초과
# M, N = map(int, input().split())
# div = []
# for i in range(M, N+1):
#     a = []
#     for j in range(1, i+1):
#         if i % j == 0 :
#             a.append(j)
#     div.append(a)

# for x in range(N-M+1):
#     if len(div[x]) == 2:
#         print(max(div[x]))

# # 풀이2 : 에라토스테네스의 체 이용하기 -> j =1 로 하면 3이 안나왔음 왜? -> 시간초과

# M, N = map(int, input().split())
# prime = list(range(M , N+1))
# for i in range(2, int((N**0.5))+1):
#     j = 2
#     while i * j <= N:
#         if prime.count(i*j) == 1:
#             prime.remove(i*j)
#         j += 1
# print(*prime, sep='\n')

# 풀이3: 에라토스테네스의 체 ( 다른풀이 : for else 문)
m,n=map(int,input().split())

for i in range(m,n+1):
    if i==1: #1 제외
        continue
    for j in range(2,int(i**0.5)+1):
        if i%j==0: # 약수 존재 -> 소수 아님
            break  
    else: # for -else 문
        print(i)