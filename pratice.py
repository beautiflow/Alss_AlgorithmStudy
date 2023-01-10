m,n = map(int,input().split())


# 에라토스테네스의 체
# 자기자신을 제외한 배수를 지워주는 알고리즘
# 백준 1929

isprime = [True] *(n+1)
isprime[0] = isprime[1] = False
sn = int(n**0.5)

for i in range(2,sn+1):
    if isprime:
        for j in range(i*2, n+1, i):
            isprime[j] = False

x = [x for x in range(m,n) if isprime[x]]

print(x)

# =================================================================================================
