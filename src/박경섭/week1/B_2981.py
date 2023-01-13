n = int(input())

arr = []

for i in range(n):
    arr.append(int(input()))

arr.sort()
min_num = arr[0]

for i in range(n):
    arr[i] -= min_num

def get_gcd(a, b):
    if b == 0:
        return a
    c = a % b
    return get_gcd(b,c) 

gcd = 0
for i in range(n-1):
    gcd = get_gcd(gcd, arr[i+1])
def divisor(n):
    
    divisors = []
    divisors_back = []

    for i in range(1,int(n**(1/2))+1):
        if n % i == 0:
            if i != 1:
                divisors.append(i)
            if i != n//i:
                divisors_back.append(n//i)
    return divisors+divisors_back[::-1]

answers = divisor(gcd)
print(" ".join(map(str,answers)))
