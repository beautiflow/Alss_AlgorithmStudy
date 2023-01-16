# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 16:45:52 2023

@author: user
"""

c = int(input())
stack = []

for i in range(c):
    num = int(input())
    
    if num !=0:
        stack.append(num)
    else:
        stack.pop()
        
print(sum(stack))