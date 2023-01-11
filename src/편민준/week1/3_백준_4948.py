def d(n):
    isprime = [True] * (2*n +1)
    sn = int((2* n )** 0.5)

    for i in range(2,sn+1):
        if isprime:
            for j in range(i*2, 2*n+1, i):
                isprime[j] = False
    return [x for x in range(n+1, (2*n)+1) if isprime[x]]


while True:
    a = int(input())
    if a == 0:
        break
    print(len(d(a)))

   
    

