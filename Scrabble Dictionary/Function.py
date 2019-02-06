class Scrabble(object):
    # Scrabble Class, input: file
    def __init__(self, scrabbleFileName):
        # Word List
        self.__wordList = []
        # Open the file and reading it
        fileIn = open(scrabbleFileName, "r")
        # For ever word in the file...
        for words in fileIn:
            # Separate by sentences
            words = words.strip()
            # Every word is added into the wordList
            self.__wordList.append(words)
        fileIn.close()
        # Word List's Value
        self.wordValue()
    # Q's and no U's
    def qAndU (self):
        for words in self.__wordList:
            # Letters
            # First Letter
            first_letter = words[0]
            # Second Letter
            second_letter = words[1]
            if first_letter == "q":
                if second_letter != "u":
                    print(words, self.__newDictionary[words])
    # Shows every two letters
    def twoLetter (self):
        for words in self.__wordList:
            # Gets the length of each word
            (length) = int(len(words))
            if length == 2:
                print(words, self.__newDictionary[words])
    # Shows every three letters with the user input letter.
    def threeLetter (self):
        # User's input
        print("Please enter a letter:")
        firstLetterChoice = input("< ")
        firstLetterChoice = firstLetterChoice.lower()
        for words in self.__wordList:
            first_letter = words[0]
            if first_letter == firstLetterChoice:
                length = int(len(words))
                # Obtains all the 3 length words
                if length == 3:
                    print(words, self.__newDictionary[words])
    # Word checker
    def wordVerify (self):
        # User's input
        print("Please write a word to check:")
        choice = input("< ")
        choice = choice.lower()
        # If it's in the list
        if choice in self.__wordList:
            print(choice, "is in the word list!")
        # If it's not in the list
        else:
            print(choice, "is not in the word list!")
    # The end checker
    def checkEnd (self):
        # User's input
        print("Please enter letters:")
        choice = input("< ")
        choice = choice.lower()
        for words in self.__wordList:
            # Get's the length of the word and starts from the back
            if words[-len(choice):] == choice:
                print(words, self.__newDictionary[words])
    # The beginning checker
    def checkBeginning (self):
        # User input
        print("Please enter letters:")
        choice = input("< ")
        choice = choice.lower()
        for words in self.__wordList:
            # Get's the length of the word and starts from the beginning
            if words[0:len(choice)] == choice:
                print(words, self.__newDictionary[words])
    # It has "X" or "Z"
    def xOrZ (self):
        # User's input
        print("Please enter letters:")
        choice = input("< ")
        choice = choice.lower()
        for words in self.__wordList:
            # Obtains all words with x or z with user input
            if "x" in words or  "z" in words:
                if choice in words:
                    print(words, self.__newDictionary[words])
    # The word value
    def wordValue (self):
        # Values
        myDictionary = {"a": 1, "b": 3, "c": 3, "d": 2, "e": 1, "f": 4, "g": 2, "h": 4, "i": 1, "j": 8, "k": 5, "l": 1,
                        "m": 3, "n": 1, "o": 1, "p": 3, "q": 10, "r": 1, "s": 1, "t": 1, "u": 1, "v": 4, "w": 4, "x": 8,
                        "y": 4, "z": 10}
        self.__newDictionary = {}
        for words in self.__wordList:
            # Value
            total = 0
            for letters in words:
                value = myDictionary[letters]
                # Adds up the value
                total += int(value)
            # the value
            self.__newDictionary[words] = total