from tkinter import *
from .GUIIndexes import *

class MainMenu(Tk):
    def __init__(self, game):
        Tk.__init__(self)
        self.game = game
        self.titleFont = font.Font(family="Comic Sans MS", size=35, weight=font.BOLD)
        self.buttonFont = font.Font(family="Comic Sans MS", size=22)
        self.geometry('%dx%d+%d+%d' % self.game.guiHandler.windowInfo)
        self.minsize(1000, 600)
        self.wm_title("Procedrual RPG")
        self.addLabels()
        self.addButtons()

        self.organizeGrid()


    def addLabels(self):
        self.titleText = Label(self, text="THE SANS RPG\nPROCEDURAL RPG", font=self.titleFont)

    def addButtons(self):
        self.newButton = Button(self, text="New Game", relief=GROOVE, command=self.openCharCreation, font=self.buttonFont)
        self.loadButton = Button(self, text="Load Game", relief=GROOVE, command=self.openLoad, font=self.buttonFont)
        self.optionsButton = Button(self, text="Options", relief=GROOVE, font=self.buttonFont)
        self.exitButton = Button(self, text="Exit", relief=GROOVE, command=self.closeApp, font=self.buttonFont)


    def organizeGrid(self):
        self.grid()
        self.titleText.grid(columnspan=2, sticky="NSEW")
        self.newButton.grid(row=1, sticky="NSEW")
        self.loadButton.grid(row=2, sticky="NSEW")
        self.optionsButton.grid(row=1, column=1, sticky="NSEW")
        self.exitButton.grid(row=2, column=1, sticky="NSEW")

        self.grid_columnconfigure(0,weight=1)
        self.grid_columnconfigure(1,weight=1)
        self.grid_rowconfigure(0,weight=5)
        self.grid_rowconfigure(1,weight=1)
        self.grid_rowconfigure(2,weight=1)


    def openCharCreation(self):
        self.game.guiHandler.swapGUI(CHARACTER_CREATION)

    def openLoad(self):
        self.game.guiHandler.swapGUI(LOAD_SCREEN)


    def closeApp(self):
        self.destroy()
