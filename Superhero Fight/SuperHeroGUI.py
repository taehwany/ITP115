# SuperHeroGUI

from tkinter import *
from Application import Application

def main():
    root = Tk()
    root.title("Superhero Battle")
    root.geometry("520x400")
    root.configure(background="black")

    # Create the Frame and add components
    app = Application(root)

    # Run mainloop
    root.mainloop()

main()