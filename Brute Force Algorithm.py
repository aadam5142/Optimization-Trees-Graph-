# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 19:42:59 2020

@author: anwar
"""

# Brute Force Algorithms

# Enumerate all possibe combinations of items.
# Remove all of the combinations whose total units
# exceeds the allowed weight
# From the remaining combinations choose any one whose value 
# is the largest

# Header for Decision Tree Implementation

def maxVal(toConsider, avail):
    """Assumes toConsider a lsit of items,
        avail a weight
        Returns a tuple of the total value of a 
        solution to 0/1 knapsack problem and 
        the items of that solution."""
        
# Body of maxVal 
    
    if toConsider == [] or avail == 0:
        result = (0, ())
    elif toConsider[0].getUnits() > avail:
        result = maxVal(toConsider[1:], avail)
    else:
        nextItem = toConsider[0]
        withVal, withToTake = maxVal(toConsider[1:],
                                     avail - nextItem.getUnits())
        withVal += nextItem.getValue()
        withoutVal, withoutToTake = maxVal(toConsider[1:], avail)
    if withVal > withoutVal:
        result = (withVal, withToTake + (nextItem,))
    else:
        result = (withoutVal, withoutToTake)
    return result

