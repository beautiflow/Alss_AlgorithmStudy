# n = int(input())
# ns = list(map(int, input().split()))

# res = []

# for i in ns:
#     s = 1
#     cnt = 0
#     while i >= s:
#         if i % s == 0:
#             cnt += 1
#         s += 1

#     if cnt == 2:
#         res.append(i)
# print(len(res))


def d(n):
    isprime = [True] * (n+1)
    isprime[0] = isprime[1] = False
    sn = int(n**0.5)

    for i in range(2,sn):
        if isprime[i]:
            for j in range(i*2, n+1, i):
                isprime[j] = False
    return isprime


int(input())
res = list(map(int,input().split()))
arr = d(1000)
cnt = 0


for x in res:
    if arr[x]:
        cnt += 1
print(cnt)