from Being import Being
class Human(Being):
    # defining the human's qualities
    def __init__(self, Name, Quarts, bloodType):
        # parent quality
        super().__init__(Name, Quarts)
        self.__mbloodType = bloodType
    # obtain blood type from other files
    def getbloodType(self):
        return self.__mbloodType
    def setbloodType(self):
        return self.__mbloodType
    # whether the human is alive or not
    def isAlive(self):
        if self.getQuarts() > 0:
            return True
        else:
            return False
            print("Human", self.getName(), "is dead. Cannot suck blood!")
    # this is the human's capacity of blood and type
    def __str__(self):
        msg = ("Human " + self.getName() + " has " + str(self.getQuarts()) + " quarts of type " + self.__mbloodType)
        return msg


