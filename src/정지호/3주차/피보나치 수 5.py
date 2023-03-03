n = int(input())
a = 0
b = 1

while n>=0:
    if n == 0:
        print(0)
        break
    elif n == 1:
        print(1)
        break
    else:
        a, b = b, a+b
        n -= 1
        if n == 1:
            print(b)
            break