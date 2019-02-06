# Creating the frame and all the components

from tkinter import *
from superhero import Superhero

class Application(Frame):
    # constructor
    def __init__(self, window):
        super().__init__(window)
        self.config(background="#ffcc00")
        self.grid()

        self.startButton = Button(self, text="Start Game", bg="#990000", command=self.startGame)
        self.startButton.grid(row=0, column=1)

        self.p1StringVar = StringVar()
        self.p1StringVar.set("")
        self.p1Entry = Entry(self, textvariable=self.p1StringVar, state=DISABLED)
        self.p1Entry.grid(row=1, column=0)

        self.playerLabel = Label(self, text="Enter Player Names", state=DISABLED)
        self.playerLabel.grid(row=1, column=1)

        self.p2StringVar = StringVar()
        self.p2StringVar.set("")
        self.p2Entry = Entry(self, textvariable=self.p2StringVar, state=DISABLED)
        self.p2Entry.grid(row=1, column=2)

        self.hero1Text = Text(self, width=20, height=20, state=DISABLED)
        self.hero1Text.grid(row=2, column=0)

        self.heroLabel = Label(self, text="Hero Stats", state=DISABLED)
        self.heroLabel.grid(row=2, column=1)

        self.hero2Text = Text(self, width=20, height=20, state=DISABLED)
        self.hero2Text.grid(row=2, column=2)

        self.fightButton = Button(self, text="Fight!", state=DISABLED, command=self.fight)
        self.fightButton.grid(row=3, column=1)

        # Superhero objects
        self.p1 = Superhero()
        self.p2 = Superhero()

    def startGame(self):
        self.playerLabel.config(state=NORMAL)
        self.p1StringVar.set("Superhero 1")
        self.p2StringVar.set("Superhero 2")
        self.p1Entry.config(state=NORMAL)
        self.p2Entry.config(state=NORMAL)
        self.heroLabel.config(state=NORMAL)
        self.fightButton.config(state=NORMAL)

        self.hero1Text.config(state=NORMAL)
        self.hero1Text.delete(0.0, END)
        self.hero1Text.config(state=DISABLED)
        self.hero2Text.config(state=NORMAL)
        self.hero2Text.delete(0.0, END)
        self.hero2Text.config(state=DISABLED)

        # Reset the health and attack points for our super heros
        self.p1.reset()
        self.p2.reset()

    def fight(self):
        # Disable components
        self.p1Entry.config(state=DISABLED)
        self.p2Entry.config(state=DISABLED)
        self.fightButton.config(state=DISABLED)

        # Get the names of the heroes
        self.p1.setName(self.p1Entry.get())
        self.p2.setName(self.p2Entry.get())

        # display info about each hero
        self.hero1Text.config(state=NORMAL)
        self.hero1Text.insert(0.0, self.p1)
        self.hero1Text.config(state=DISABLED)

        self.hero2Text.config(state=NORMAL)
        self.hero2Text.insert(0.0, self.p2)
        self.hero2Text.config(state=DISABLED)

        # loop while both players are alive
        while self.p1.isAlive() and self.p2.isAlive():

            # fight
            self.p1.loseHealthPoints(self.p2.attackValue)
            self.p2.loseHealthPoints(self.p1.attackValue)

            # display stats
            self.hero1Text.config(state=NORMAL)
            self.hero1Text.insert(END, self.p1.getStats())
            self.hero1Text.config(state=DISABLED)

            self.hero2Text.config(state=NORMAL)
            self.hero2Text.insert(END, self.p2.getStats())
            self.hero2Text.config(state=DISABLED)

        # Display winner
        if self.p1.isAlive():
            self.hero1Text.config(state=NORMAL)
            self.hero1Text.insert(END, "\nWINNER!")
            self.hero1Text.config(state=DISABLED)
            self.hero2Text.config(state=NORMAL)
            self.hero2Text.insert(END, "\nDEAD")
            self.hero2Text.config(state=DISABLED)
        elif self.p2.isAlive():
            self.hero1Text.config(state=NORMAL)
            self.hero1Text.insert(END, "\nDEAD")
            self.hero1Text.config(state=DISABLED)
            self.hero2Text.config(state=NORMAL)
            self.hero2Text.insert(END, "\nWINNER!")
            self.hero2Text.config(state=DISABLED)
        else:
            self.hero1Text.config(state=NORMAL)
            self.hero1Text.insert(END, "\nDEAD")
            self.hero1Text.config(state=DISABLED)
            self.hero2Text.config(state=NORMAL)
            self.hero2Text.insert(END, "\nDEAD")
            self.hero2Text.config(state=DISABLED)