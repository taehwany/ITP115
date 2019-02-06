from Being import Being
# setting boundaries of the vampire
MAX_BLOOD = 5
# the hunger levels
HUNGER_LEVELS = ["starving", "hangry", "hungry", "content", "full", "stuffed"]
# vampire class
class Vampire(Being):
    def __init__(self, Name, Quarts, animalForm):
        # parent class
        super().__init__(Name, Quarts)
        self.__mAnimalForm = animalForm
    # obtain its animal form from other files
    def getanimalForm(self):
        return self.__mAnimalForm
    def setanimalForm(self):
        return self.__mAnimalForm
    # obtain its hunger level from other files
    def getHunger(self):
        return HUNGER_LEVELS[self.getQuarts()]
    def isStuffed(self):
        if self.getQuarts() == MAX_BLOOD:
            return True
        else:
            return False
    # vampire sucking mechanic
    def suckBlood(self, Human):
        Human.decreaseQuarts()
        self.increaseQuarts()
    # this is the vampire's level of hunger
    def __str__(self):
        msg = (self.getName() + " is " + self.getHunger())
        return msg


