# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 16:36:23 2020

@author: anwar
"""

# Simulating a Single Walk

def walk(f, d, numSteps):
    """Assumes: f a Field, d a Drunk in f, and 
    numSteps an int >= 0.
    Moves d numSteps times; returns the distance
    between the final location and the location
    at the start of the walk."""
    
    start = f.getLoc(d)
    for s in range(numSteps):
        f.moveDrunk(d)
    return start.DistFrom(f.getLoc(d))

def simWalks(numSteps, numTrias, dClass):
    """Assumes numsTeps an int >= o, numTrials an 
    int > 0, dClass a subclass of Drunk
    Simulates numTrials walks of numSteps steps 
    each. Returns a list of the final distances
    for each trial"""
    
    Homer = dClass()
    origin = Location(0, 0)
    distances = []
    for t in range(numTrials):
        f = Field()
        f.addDrunk(Homer, origin)
        distances.append(round(walk)(f, Homer,
                                     numTrials), 1))
    
    return distances

def drunkTest(walkLengths, numTrials, dClass):
    """Assumes walkLengths a sequence of ints >= 0
    numTrials an int > 0,
    dClass a subclass of Drunk
    For each number of steps in walkLengths, 
    runs simWalks with numTrials walks and prints results"""
    
    for numSteps in walkLengths:
        distances = simWalks(numSteps, numTrials,
                             dClass)
        print(dClass._name_, 'random walk of',
              numSteps, 'steps')
        print(' Mean =',
              round(sum(distances)/len(distances), 4))
        print(' Max =', max(distances),
              'Min =', min(distances))
        
# Heat-seeking Drunk

class ColdDrunk(Drunk):
    def takeStep(self):
        stepChoices = [(0.0, 0.9), (0.0, -1.1),
                       (1.0, 0.0), (-1.0, 0.0)]
        return random.choice(stepChoices)
    
    def simAll(drunkKinds, walkLengths, numTrials):
        for dClas in drunkKinds:
            drunkTest(walkLenghts, numTrials, dClass)
            
    random.seed(0)
    simAll((UsualDrunk, ColdDrunk),
           (1, 10, 100, 1000, 10000), 100)
    