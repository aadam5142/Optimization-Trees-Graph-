# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 16:24:30 2020

@author: anwar
"""

# class Location

class Location(object):
    def _init_(self, x, y):
        """x and y are floats"""
        self.x = x
        self.y = y
        
    def move(self, deltaX, deltaY):
        """deltaX and deltaY are floats"""
        return Location(self.x + deltaX,
                        self.y + deltaY)
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def distFrom(self, other):
        ox = other.x
        oy = other.y
        xDist = self.x - ox
        yDist = self.y - oy
        return (xDist**2 + yDist**2)**0.5
    
    def _str_(self):
        return '<' + str(self.x) + ', '\
            + str(self.y) + '>'
            
# Class Field

class Field(object):
    def _init_(self):
        self.drunks = {}
        
    def addDrunk(self, drunk, loc):
        if drunk in self.drunks:
            raise ValueError('Duplicate drunk')
        else:
            self.drunks[drunk] = loc
            
    def getLoc(self, drunk):
        if drunk not in self.drunks:
            raise ValueError('Drunk not in field')
        return self.drunks[drunk]
    
    def moveDrunk(self, drunk):
        if drunk not in self.drunks:
            raise ValueError('Drunk not in field')
        xDist, yDist = drunk.takeStep()
        currentLocation =self.drunks[drunks]
        #use move method of Location to get new location
        self.drunks[drunk] = \
            currentLcoation.move(xDist, yDist)

# Class Drunk

class Drunk(object):
    def _init_(self, name):
        self.name = name
    def _str_(self):
        return 'This drunk is named ' + self.name
    
import random

class UsualDrunk(Drunk):
    def takeStep(self):
        stepChoices =\
            [(0.0, 1.0),(0.0, -1.0), (1.0, 0.0),(-1.0, 0.0)]
        return random.choice(stepChoices)
    
class ColdDrunk(Drunk):
    def takeStep(self):
        stepChoices =\
            [(0.0, 0.9), (0.0, -1.1), (1.0, 0.0), (-1.0, 0.0)]
        return random.choice(stepChoices)
    
            