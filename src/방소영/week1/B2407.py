# 함수만들기
# factorial
# dp


# # 내 풀이1 -> 틀림 왜? : 나눗셈에서 오차발생
# import sys ; input = sys.stdin.readline
# n , m = map(int, input().strip().split())
# x = m
# k = n - m
# z = n
# if n == m :
#     print(1)
# else:
#     while n != k+1:
#         z = z * (n-1)
#         n -= 1
#     while m != 1:
#         x = x * (m-1)
#         m -= 1
#     print(int(z/x))

# 함수만들기 -> 나눗셈에서 오차 발생 -> 몫으로 구함
import sys ; input = sys.stdin.readline
n, m = map(int, input().split())
def fac(a):
    num = 1
    if a == 0:
        num = 1
    else:
        for i in range(1, a+1):
            num = num * i
    return num

print(fac(n)//(fac(n-m)*fac(m)))


# 문제 조건에 나오는 히든을 내가 찾아야 하고 그 조건 속에서의 히든도 찾아야 함.