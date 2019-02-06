from Human import Human
from Vampire import Vampire
# list of all humans (choice 1)
def printHumans(humanList):
    for index in range(len(humanList)):
        print (index,")", humanList[index])
# feeding on humans (choice 2)
def performFeeding(humanList, vampire):
    print("Please choose which human!")
    printHumans(humanList)
    choice = int(input("< "))
    while choice < 0 or choice >= len(humanList):
        printHumans(humanList)
        print("Please choose again!")
        choice = int(input("< "))
    if not humanList[choice].isAlive():
        print(humanList[choice].getName(), "is dead! Cannot have they're blood sucked anymore!")
    elif vampire.isStuffed():
        print(vampire)
        print(vampire.getName(), "is stuffed and cannot take anymore blood!" )
    elif humanList[choice].isAlive():
        vampire.suckBlood(humanList[choice])
        print(humanList[choice])
        print(vampire)
def main():
    # all the humans
    human1 = Human("Eric", 5,"A-")
    human2 = Human("Mina", 7,"O+")
    human3 = Human("Louis",4,"O+")
    human4 = Human("Annie",3,"B-")
    humanList = [human1, human2, human3, human4]
    # vampire description
    print("Please choose a name and animal")
    vampireName = input("Name: ")
    vampireAnimal = input("Animal: ")
    vampire1 = Vampire(vampireName, 0, vampireAnimal)
    # menu
    menuChoice = 5
    while menuChoice != 3:
        print("Menu...")
        print("1 Print all Humans")
        print("2 Suck Blood")
        print("3 Quit ")
        menuChoice = int(input("< "))
        while menuChoice != 1 and menuChoice != 2 and menuChoice != 3:
            print("Please choose a correct option!")
            menuChoice = int(input("< "))
        if menuChoice == 1:
            printHumans(humanList)
        if menuChoice == 2:
            performFeeding(humanList, vampire1)
    # exit
    print(vampireName, "transformed into a", (vampireAnimal))
main()


