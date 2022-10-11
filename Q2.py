#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 20:00:19 2022

@author: ml
"""

def less_than(num):
    n = 0
    while n < num:
        print(n, n**2)
        n += 1
    else:
        print("Greater than", num)
            
less_than(8)
    
        
