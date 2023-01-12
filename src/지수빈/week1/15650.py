# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 15:20:20 2023

@author: user
"""
# =============================================================================
# 1부터 N까지의 수로 길이가 M인 수열
# 가능한 경우를 사전순으로 증가하게 출력
# =============================================================================
import re
from itertools import combinations



'''
1부터 N까지의 모든 수로 리스트 생성
앞에서부터 조합해서 출력
'''

n,m = map(int,input().split())

li = []
for i in range(n):
    li.append(i+1)
# print(li)
'''
m이 2라면
[i:i+2]까지 가져오는 것 필요
근데 i+2가 list의 총개수를 초과하지 않아야
i는 n-2까지만 돌아야//i의 최대한계
'''




# 리스트에서 가능한 모든 조합 구하기
a= list(combinations(li,m))


# 리스트 요소 하나씩 출력
for i in a:
    ans = str(i)[1:-1]
    ans = re.sub(",","",ans)
    print(ans)
    
    

    