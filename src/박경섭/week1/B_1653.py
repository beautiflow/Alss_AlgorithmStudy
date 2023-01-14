a = int(input())
b = 2

if a == 1:
    pass

while b <= a:
    
    if a % b == 0:
        print(b)
        a = a/b

    else:
        b += 1
