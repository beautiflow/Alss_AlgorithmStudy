
def d(n):
    if n == 1:
        return False

    for j in range(2,int(n**0.5)+1):
        if n % j == 0:
            return False
    return True

t = int(input())

for _ in range(t):
    a = int(input())

    z,x = a//2 , a//2
    while a>0:
        if d(z) and d(x):
            print(z,x)
            break
        else:
            z -= 1
            x += 1
    #
    
        