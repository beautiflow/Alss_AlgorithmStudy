import sys

input =sys.stdin.readline

n = int(input())
ns = list(map(int, input().split()))

isn = int(input())
isns = list(map(int, input().split()))

ns.sort()
def bs(target):
    st = 0
    en = n-1
    while(st <= en):
        mid = (st+en) // 2
        if ns[mid] < target:
            st = mid + 1
        elif ns[mid] > target:
            en = mid -1
        else:
            return 1
    else:
        return 0
    

for i in isns:
    print(bs(i))                



# 방법 2
# # 입력
# N = int(input())
# A = set(map(int, input().split()))	# 탐색 시간을 줄이기 위해 set으로 받음
# M = int(input())
# arr = list(map(int, input().split()))

# for num in arr:				# arr의 각 원소별로 탐색
#     print(1) if num in A else print(0)	# num이 A 안에 있으면 1, 없으면 0 출력







# for i in isns:
#     for j in range(n):
#         if i == ns[j]:
#             print(1)
#             break
#     else:
#         print(0)

        