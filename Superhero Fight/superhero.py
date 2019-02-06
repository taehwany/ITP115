#initially one file--
# separate class from main

import random

class Superhero:
    MAX_HEALTHPOINTS = 100  #static since this is the same
    MAX_ATTACKVALUE = 20    # for EVERY superhero object

    # constructor method
    def __init__(self, inputName="No name"):
        self.name = inputName
        #self.healthPoints = Superhero.MAX_HEALTHPOINTS
        self.healthPoints = random.randrange(50, Superhero.MAX_HEALTHPOINTS)
        self.attackValue = random.randrange(1, Superhero.MAX_ATTACKVALUE)

    def setName(self, name):
        self.name = name

    def __str__(self):
        tempStr = self.name
        tempStr += "\nHealth Points: " + str(self.healthPoints)
        tempStr += "\nAttack Value: " + str(self.attackValue)
        tempStr += "\n"
        return tempStr

    def getStats(self):
        tempStr = "\nHealth Points: " + str(self.healthPoints) + "\n"
        return tempStr

    def isAlive(self):
        if self.healthPoints > 0:
            return True
        else:
            return False

    def loseHealthPoints(self, deductHP):
        if deductHP > self.healthPoints:
            self.healthPoints = 0
        else:
            self.healthPoints -= deductHP

    def reset(self):
        self.healthPoints = random.randrange(50, Superhero.MAX_HEALTHPOINTS)
        self.attackValue = random.randrange(1, Superhero.MAX_ATTACKVALUE)


