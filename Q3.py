#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 20:15:46 2022

@author: ml
"""

def func_sum(num):
    n = 1
    sum = 0
    while n < num:
        sum = sum+n
        n = n+1
    print(sum)
        
func_sum(10)