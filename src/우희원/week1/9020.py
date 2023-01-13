def is_prime(n) :
    if n == 1 :
        return False
    else :
        for i in range(2, int(n**0.5)+1) :
            if n%i == 0 :
                return False
        return True

T = int(input())

for _ in range(T):
    n = int(input())
    for a in range(n // 2, 0, -1):
        if is_prime(a) and is_prime(n - a):
            print(a, n - a)
            break