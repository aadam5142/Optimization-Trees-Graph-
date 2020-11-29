# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 18:48:29 2020

@author: anwar
"""

# Greedy Algorithms

# Class - Food

class Food(object):
    def _init_(self, n, v, w):
        self.name = n
        self.value = v
        self.calories = w
        
    def getValue(self):
        return self.value
    
    def getCost(self):
        return self.calories
    
    def density(self):
        return self.getValue()/self.getCost()
    
    def _str_(self):
        return self.name + ': <' + str(self.value)\
                + ', ' + str(self.calories) + '>'
                
# Build Menu of Foods

def buildMenu(names, values, calories):
    """names, values, calories lsits of same length.
        name a list of strings
        values and calories lists of numbers
        returns list of Foods"""
    menu = []
    for i in range(len(values)):
        menu.append(Food(names[i], values[i],
                         calories[i]))
    return menu

# Implementation of Flexibile Greedy

def greedy(items, maxCost, keyFunction):
    """Assumes items a list, maxCost >= 0,
    keyFunction maps elements of items to numbers"""
    itemsCopy = sorted(items, key = keyFunction,
                       reverse = True)
    result = []
    totalValue, totalCost = 0.0, 0.0
    
    for i in range(len(itemsCopy)):
        if (totalCost + itemsCopy[i].getCost()) <= maxCost:
            result.append(itemsCopy[i])
            totalCost += itemsCopy[i].getCost()
            totalValue += itemsCopy[i].getValue()
            
    return (result, totalValue)

# Algorithmic Efficiency

def greedy(items, maxCost, keyFunction):
    itemsCopy = sorted(items, key = keyFunction,
                       reverse = True)
    result = []
    totalValue, totalCost = 0.0, 0.0
    
    for i in range(len(itemsCopy)):
        if (totalCost + itemsCopy[i].getCost() <= maxCost:
            result.append(itemsCopy[i])
            totalCost += itemsCopy[i].getCost()
            totalValue = itemsCopy[i].getValue()
            
    return (result, totalValue)

# Using greedy

def testGreedys(maxUnits):
    print('Use greedy by value to allocate', maxUnits,
          'calories')
    testGreedys(foods, maxUnits, Food.getValue)
    print('\nUse greedy by cost to allocate', maxUnits,
          'calories')
    # Lambda
    # lambda used to create anonymous functions
        #lambda <id1, id2,...idn>: <expression>
        # returns a function of n arguments
    testGreedy(foods, maxUnits,
               lambda x: 1/Food.getCost(x))
    print('\nUse greedy by density to allocate', maxUnits,
          'calories')
    testGreedy(foods, maxUnits, Food.density)

testGreedys(800)  

names = ['wine', 'beer', 'pizza', 'burger', 'fries',
         'cola', 'apple', 'donut', 'cake']
values = [89,90,95,100,90,79,50,10]
calories = [123,154,258,354,365,150,95,195]
foods = buildMenu(names, values, calories)
testGreedys(foods, 750)
                          