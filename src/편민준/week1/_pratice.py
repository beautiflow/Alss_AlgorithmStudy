def gcd(a,b):
    x,y = a,b
    while x:
        x,y = y%x, x
    return y