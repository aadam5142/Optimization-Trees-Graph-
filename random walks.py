# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 17:21:16 2020

@author: anwar
"""
# Iterating over styles

class styleIterator(object):
    def _init_(self, styles):
        self.index = 0
        self.styles = styles
        
    def nextStyle(self):
        result = self.styles[self.index]
        if self.index == len(self.styles) - 1:
            self.index = 0
            
        else:
            self.index += 1
        return result

# simDrunk

def simDrunk(numTrials, dClass, walkLengths):
    meanDistances = []
    for numSteps in walkLengths:
        print('Starting simulation of', 
              numSteps, 'steps')
        trials = simWalks(numSteps, numTrials, dClass)
        mean = sum(trials)/len(trials)
        meanDistances.append(mean)
    return meanDistances

# Plotting Ending Locations

def plotLocs(drunkKinds, numSteps, numTrials):
    styleChoice = styleIterator(('k+', 'r^', 'mo'))
    for dClass in drunkKinds:
        locs = getFinalLocs(numSteps, numTrials, dClass)
        xVals, yVals = [], []
        for loc in locs:
            xVals.append(loc.getX())
            yVals.append(loc.getY())
        xVals = pylab.array(xVals)
        yVals = pylab.array(yVals)
        meanX = sum(abs(xVals))/len(xVals)
        meanY = sum(abs(yVals))/len(yVals)
        
class OddField(Field):
    def _init_(self, numHole = 1000,
               xRange = 100, yRange = 100):
        Field._init_(self)
        self.wormholes = {}
        for w in range(numHoles):
            x = random.randint(-xRange, xRange)
            y = random.randint(-yRange, yRange)
            newX = random.randint(-xRange, xRange)
            newY = random.randint(-yRange, yRange)
            newLoc = Location(newX, newY)
            self.wormholes[(x, y)] = newLoc
            
     def moveDrunk(self, drunk):
         Field.moveDrunk(self, drunk)
         x = self.drunks[drunk].getX()
         y = self.drunks[drunk].getY()
         if (x, y) in self.wormholes:
             self.drunks[drunk] = self.wormholes[(x, y)]
             
    def traceWalk(fieldKinds, numSteps):
        styleChoice = styleIterator(('b+', 'r^', 'ko'))
        for fClass in fieldKinds:
            d = UsualDrunk()
            f = fClass()
            f.addDrunk(d, Location(0, 0))
            locs = []
            for s in range(numSteps):
                f.moveDrunk(d)
                locs.append(f.getLoc(d))
            xVals, yVals = [], []
            for loc in locs:
                xVals.append(loc.getX())
                yVals.append(loc.getY())
            curStyle = styleChoice.nextStyle()
            pylab.plot(xVals, yVals, curStyle,
                       label = fClass._name_)
            
            pylab.title('Spots Visited on Walk ('
                        + str(numSteps) + 'steps)')
            pylab.xlabel('Steps East/West of Origin')
            pylab.ylabel('Steps North/South of Origin')
            pylab.legend(loc = 'best')
            
        traceWalk((Field, OddField), 500)
        