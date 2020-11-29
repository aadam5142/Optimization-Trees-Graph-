# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 23:42:58 2020

@author: anwar
"""

#Write a generator that returns every arrangement of items such that each is in one or none of two different bags. Each combination should be given as a tuple of two lists, the first being the items in bag1, and the second being the items in bag2.

def yieldAllCombos(items):
    """
      Generates all combinations of N items into two bags, whereby each 
      item is in one or zero bags.

      Yields a tuple, (bag1, bag2), where each bag is represented as 
      a list of which item(s) are in each bag.
    """
#Note this generator should be pretty similar to the powerSet generator above.


#We mentioned that the number of possible combinations for N items into one bag is  2n . How many possible combinations exist when there are two bags? Think about this for a few minutes, then click the following hint to confirm if your guess is correct. Remember that a given item can only be in bag1, bag2, or neither bag -- it is not possible for an item to be present in both bags!

    items = buildRandomItems(1)
    combos = yieldAllCombos(items)
