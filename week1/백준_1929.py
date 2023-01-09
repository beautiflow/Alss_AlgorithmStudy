#에레스토테네스의 체

a,b = map(int, input().split())
isprime = [True] * (b+1)
isprime[0] = isprime[1] = False
sn = int(b**0.5)

for i in range(2,sn+1):
    if isprime:
        for j in range(i*2,b+1,i):
            isprime[j] = False

res = [x for x in range(a,b) if isprime[x]]

print(res)



#시간초과@@
# #소수구하기

# s_list = []
# m, n = map(int,input().split())
# # 1과 자기자신

# for i in range(m,n+1):
#     cnt = 0
#     res = 1
#     while i+1 != res:
#         if i % res == 0:
#             cnt += 1
#         res += 1
#     if cnt == 2:
#         s_list.append(i)

# for i in s_list:
#     print(i)