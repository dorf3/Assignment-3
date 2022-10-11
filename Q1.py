#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 19:17:51 2022

@author: ml
"""

marks = {'Andy':88, 'Amy':66, 'James':90, 'Jules':55, 'Arthur': 77}

def func_name(name):
    try:
        return marks[name]
    except:
        print(name, 'not found')
        
func_name("James")
print(func_name("James"))
