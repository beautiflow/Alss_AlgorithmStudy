# 시간초과 
# 12 line 에서 i**0.5 를 math를 import해서 sqrt로 바꿔줘서 해결
import sys ; input = sys.stdin.readline
import math

n = int(input())
a = []
while n != 0:
    for i in range(n+1,(2*n)+1):
        if i==1: #1 제외
            continue
        for j in range(2,int(math.sqrt(i))+1):
            if i%j==0: # 약수 존재 -> 소수 아님
                break  
        else: # for -else 문
            a.append(i)
    print(len(a))
    n = int(input())
    a = []
