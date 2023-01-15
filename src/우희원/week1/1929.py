def is_prime(n) :
    if n == 1 :
        return False
    else :
        for i in range(2, int(n/2)+1) :
            if n%i == 0 :
                return False
        return True

m, n = map(int, input().split())

for i in range(m, n+1) :
    if is_prime(i) == True :
        print(i)