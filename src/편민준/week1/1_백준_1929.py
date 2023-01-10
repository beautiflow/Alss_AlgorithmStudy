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


