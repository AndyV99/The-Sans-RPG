from tkinter import *
from tkinter import font
from ..Beings import Player
from .GUIIndexes import *

class CharacterCreation(Tk):
    def __init__(self, game):
        Tk.__init__(self)
        self.wm_title("Character Creation")
        self.titleFont = font.Font(family="Comic Sans MS", size=35, weight=font.BOLD)
        self.generalFont = font.Font(family="Comic Sans MS", size=22)
        self.game = game
        self.geometry('%dx%d+%d+%d' % self.game.guiHandler.windowInfo)
        self.minsize(1000, 600)
        self.addLabels()
        self.addEntries()
        self.addButtons()
        self.organizeGrid()
        self.updateButtons()


    def addLabels(self):
        self.titleText = Label(self, text="New Character", font=self.titleFont)

        self.nameBoxLabel = Label(self, text="Enter Name: ", anchor=W, font=self.generalFont)

        self.statPointsLeft = Label(self, text="Stat Points Left: ", anchor=W, font=self.generalFont)
        self.points = StringVar()
        self.points.set("5")
        self.statPoints = Label(self, textvariable=self.points, anchor=E, font=self.generalFont)

        self.dividerStart = Label(self, text=("-")*50, font=self.generalFont)

        self.strength = Label(self, text="Strength: ", anchor=W, font=self.generalFont)

        self.strAmount = StringVar()
        self.strAmount.set("0")
        self.strengthAmount = Label(self, textvariable=self.strAmount, font=self.generalFont, anchor=N)

        self.agility = Label(self, text="Agility: ", anchor=W, font=self.generalFont)

        self.agiAmount = StringVar()
        self.agiAmount.set("0")
        self.agilityAmount = Label(self, textvariable=self.agiAmount, font=self.generalFont, anchor=N)

        self.intelligence = Label(self, text="Intelligence: ", anchor=W, font=self.generalFont)

        self.intAmount = StringVar()
        self.intAmount.set("0")
        self.intelligenceAmount = Label(self, textvariable=self.intAmount, font=self.generalFont, anchor=N)


    def addEntries(self):
        self.nameEntry = StringVar()
        self.nameBoxEntry = Entry(self, textvariable=self.nameEntry, justify=LEFT, font=self.generalFont)


    def addButtons(self):
        self.subStrength = Button(self, text="-", relief=GROOVE, justify=RIGHT, command=self.subStr, font=self.generalFont)
        self.addStrength = Button(self, text="+", relief=GROOVE, justify=RIGHT, command=self.addStr, font=self.generalFont)

        self.subAgility = Button(self, text="-", relief=GROOVE, justify=RIGHT, command=self.subAgi, font=self.generalFont)
        self.addAgility = Button(self, text="+", relief=GROOVE, justify=RIGHT, command=self.addAgi, font=self.generalFont)

        self.subIntelligence = Button(self, text="-", relief=GROOVE, justify=RIGHT, command=self.subInt, font=self.generalFont)
        self.addIntelligence = Button(self, text="+", relief=GROOVE, justify=RIGHT, command=self.addInt, font=self.generalFont)

        self.createButton = Button(self, text="Create Character", relief=GROOVE, command=self.createCharacter, font=self.generalFont)
        self.backButton = Button(self, text="Back", relief=GROOVE, command=self.back, font=self.generalFont)

    def updateButtons(self):
        if(int(self.strAmount.get()) == 0):
            self.subStrength.config(state=DISABLED)
        else:
            self.subStrength.config(state=ACTIVE)


        if(int(self.agiAmount.get()) == 0):
            self.subAgility.config(state=DISABLED)
        else:
            self.subAgility.config(state=ACTIVE)


        if(int(self.intAmount.get()) == 0):
            self.subIntelligence.config(state=DISABLED)
        else:
            self.subIntelligence.config(state=ACTIVE)


        if((int(self.points.get())) == 0):
            self.addStrength.config(state=DISABLED)
            self.addAgility.config(state=DISABLED)
            self.addIntelligence.config(state=DISABLED)
            self.createButton.config(state=ACTIVE)
        else:
            self.addStrength.config(state=ACTIVE)
            self.addAgility.config(state=ACTIVE)
            self.addIntelligence.config(state=ACTIVE)
            self.createButton.config(state=DISABLED)


    def addStr(self):
        amnt = int(self.strAmount.get())
        amnt += 1
        self.strAmount.set(amnt)

        points = int(self.points.get())
        points -= 1
        self.points.set(points)

        self.updateButtons()

    def subStr(self):
        amnt = int(self.strAmount.get())
        amnt -= 1
        self.strAmount.set(amnt)

        points = int(self.points.get())
        points += 1
        self.points.set(points)

        self.updateButtons()


    def addAgi(self):
        amnt = int(self.agiAmount.get())
        amnt += 1
        self.agiAmount.set(amnt)

        points = int(self.points.get())
        points -= 1
        self.points.set(points)

        self.updateButtons()

    def subAgi(self):
        amnt = int(self.agiAmount.get())
        amnt -= 1
        self.agiAmount.set(amnt)

        points = int(self.points.get())
        points += 1
        self.points.set(points)

        self.updateButtons()


    def addInt(self):
        amnt = int(self.intAmount.get())
        amnt += 1
        self.intAmount.set(amnt)

        points = int(self.points.get())
        points -= 1
        self.points.set(points)

        self.updateButtons()

    def subInt(self):
        amnt = int(self.intAmount.get())
        amnt -= 1
        self.intAmount.set(amnt)

        points = int(self.points.get())
        points += 1
        self.points.set(points)

        self.updateButtons()


    def organizeGrid(self):
        self.grid()

        self.titleText.grid(columnspan=4, sticky="NSEW")

        self.nameBoxLabel.grid(row=1, sticky="NSEW")
        self.nameBoxEntry.grid(row=1, column=1, columnspan=3, sticky="E")

        self.statPointsLeft.grid(row=2, sticky="NSEW")
        self.statPoints.grid(row=2, column=1, columnspan=3, sticky="NSEW")

        self.dividerStart.grid(row=3, columnspan=4)

        self.strength.grid(row=4, column=0, sticky="NEW")
        self.subStrength.grid(row=4, column=1, sticky="NEW")
        self.strengthAmount.grid(row=4, column=2)
        self.addStrength.grid(row=4, column=3, sticky="NEW")

        self.agility.grid(row=5, column=0, sticky="NEW")
        self.subAgility.grid(row=5, column=1, sticky="NEW")
        self.agilityAmount.grid(row=5, column=2)
        self.addAgility.grid(row=5, column=3, sticky="NEW")

        self.intelligence.grid(row=6, column=0, sticky="NEW")
        self.subIntelligence.grid(row=6, column=1, sticky="NEW")
        self.intelligenceAmount.grid(row=6, column=2)
        self.addIntelligence.grid(row=6, column=3, sticky="NEW")

        self.createButton.grid(row=7, column=1, columnspan=3, sticky="SEW")
        self.backButton.grid(row=7, column=0, sticky="SEW")

        for i in range(4):
            self.grid_columnconfigure(i, weight=1)

        for j in range(7):
            self.grid_rowconfigure(j, weight=1)


    def createCharacter(self):
        self.game.player = Player(name=self.nameEntry.get(), inStrength=int(self.strAmount.get()), inAgility=int(self.agiAmount.get()), inIntelligence=int(self.intAmount.get()))
        self.game.guiHandler.swapGUI(TOWN_SCREEN)


    def back(self):
        self.game.guiHandler.back()
