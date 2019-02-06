from Function import Scrabble
def main():
    scrabble = Scrabble("Scrabble.txt")
    # The Menu!
    menuChoice = "-123109810298131"
    while menuChoice != "8":
        print("Welcome to the Scrabble Finder 3000!")
        print("Main Menu:")
        print("1) All letters that start with Q and doesn't have U next.")
        print("2) Display all two letter words.")
        print("3) Show all three letter words with your input.")
        print("4) Word Verify!")
        print("5) End checker with your input.")
        print("6) Beginning checker with your input.")
        print("7) Your input with X's or Z's.")
        print("8) Exit.")
        # The input
        menuChoice = input("Please choose an option: ")
        while menuChoice > "8" or menuChoice < "1":
            menuChoice = input("Please choose a correct option: ")
        if menuChoice == "1":
            scrabble.qAndU()
        elif menuChoice == "2":
            scrabble.twoLetter()
        elif menuChoice == "3":
            scrabble.threeLetter()
        elif menuChoice == "4":
            scrabble.wordVerify()
        elif menuChoice == "5":
            scrabble.checkEnd()
        elif menuChoice == "6":
            scrabble.checkBeginning()
        elif menuChoice == "7":
            scrabble.xOrZ()
    # Goodbye!
    print("Thank you for using the Scrabble Finder 3000!")
main()