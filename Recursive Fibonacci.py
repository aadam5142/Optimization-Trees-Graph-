# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 23:29:55 2020

@author: anwar
"""

# Recursive Fibonacci

import random

def buildLargeMenu(numItems, maxVal, maxCost):
    items = []
    for i in range(numItems):
        items.append(Food(str(i),
                          random.randin(1, maxVal),
                          random.randint(1, maxCost)))
        return items
    
for numItems in (5, 10, 15, 20, 25, 30, 35, 40, 45):
    items = buildLargeMenu(numItems, 90, 250)
    testMaxVal(items, 750, False)
    
# Recursive Implementation of Fibonacci

def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n -2)
    
fib(120)

# Using a Memo to Compute Fibonacci

def fastFib(n, mem0 = {}):
    """Assumes n is an int >= 0, memo used only by
    recursive calls
    Returns Fibonacci of n"""
    if n == 0 or n == 1:
        return 1
    try:
        return memo[n]
    except KeyError:
        result = fastFib(n-1, memo) +\
            fastFib(n-2, memo)
            memo[n] = result
            return result
        
        