N = int(input())
prime = list(map(int, input().split()))
prime_new = []
for i in range(N):
    if prime[i] == 1:
        continue
    for j in range(2, prime[i]):
        if prime[i] % j == 0:
            break
    else: 
        prime_new.append(prime[i])
print(len(prime_new))