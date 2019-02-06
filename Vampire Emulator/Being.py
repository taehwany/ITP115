class Being(object):
    Quarts = 0
    # we'll be defining the being's name and quarts
    def __init__(self, Name, Quarts):
        self.__mName = Name
        self.__Quarts = int(Quarts)
    # a way to get quarts from other files
    def getQuarts(self):
        return self.__Quarts
    def setQuarts(self):
        return self.__Quarts
    # a way to get names from other files
    def getName(self):
        return self.__mName
    def setName(self):
        return self.__mName
    def increaseQuarts(self):
        self.__Quarts = self.__Quarts + 1
    def decreaseQuarts(self):
        self.__Quarts = self.__Quarts - 1

