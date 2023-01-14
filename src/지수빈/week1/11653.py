# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 20:52:35 2023

@author: user



N = int(input())
m = 2
while N!=1:  # N과m을 나눴을때 몫이 1이 되면 멈춤.
  if N%m==0: 
    print(m) 
    N = N//m
  else:
    m += 1

