def is_prime(n) :
    if n == 1 :
        return False
    else :
        for i in range(2, int(n/2)+1) :
            if n%i == 0 :
                return False
        return True

n = int(input())
result = 0
if n == 0 :
    pass
for i in range(n, 2*n+1) :
    if is_prime(i) == True :
        result += 1
print(result)