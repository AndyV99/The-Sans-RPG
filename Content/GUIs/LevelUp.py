from tkinter import *
from tkinter import font

class LevelUp(Tk):
    def __init__(self, game):
        Tk.__init__(self)
        self.game = game
        self.generalFont = font.Font(family="Comic Sans MS", size=22)
        self.geometry('400x500+{}+{}'.format(self.game.guiHandler.windowInfo[2]+300, self.game.guiHandler.windowInfo[3]))
        self.minsize(400, 500)
        self.wm_title("Congratz!  You Leveled Up!")
        self.addStatPointsFrame()
        self.addStrengthFrame()
        self.addAgilityFrame()
        self.addIntelligenceFrame()
        self.addButton()
        self.configureGrid()
        self.minusClicked = 0


    def addStatPointsFrame(self):
        self.statPointsFrame = Frame()

        self.statPointsLeft = Label(self.statPointsFrame, text="Stat Points Left: ", anchor=W, font=self.generalFont)
        self.points = IntVar()
        self.points.set(1)
        self.statPoints = Label(self.statPointsFrame, textvariable=self.points, anchor=E, font=self.generalFont)

        self.statPointsLeft.grid(row=0, column=0, sticky="NEWS")
        self.statPoints.grid(row=0, column=1, sticky="NEWS")

        self.statPointsFrame.grid_columnconfigure(0, weight=1)
        self.statPointsFrame.grid_columnconfigure(1, weight=1)

        self.statPointsFrame.grid_rowconfigure(0, weight=1)

        self.statPointsFrame.grid(row=0, column=0, sticky="NEWS")


    def addStrengthFrame(self):
        self.strengthFrame = Frame()

        self.strength = Label(self.strengthFrame, text="Strength: ", anchor=W, font=self.generalFont, width=10)
        self.strAmount = IntVar()
        self.strAmount.set(self.game.player.strength)
        self.strengthAmount = Label(self.strengthFrame, textvariable=self.strAmount, font=self.generalFont, anchor=N)

        self.addStrength = Button(self.strengthFrame, text="+", relief=GROOVE, justify=RIGHT, command=lambda : self.chngStr(1), font=self.generalFont)
        self.subStrength = Button(self.strengthFrame, text="-", relief=GROOVE, justify=RIGHT, command=lambda : self.chngStr(-1), font=self.generalFont)

        self.strength.grid(row=0, column=0, sticky="NWS")
        self.subStrength.grid(row=0, column=1, sticky="NWS")
        self.strengthAmount.grid(row=0, column=2)
        self.addStrength.grid(row=0, column=3, sticky="NWS")

        self.strengthFrame.grid_columnconfigure(0, weight=1)
        self.strengthFrame.grid_columnconfigure(1, weight=1)
        self.strengthFrame.grid_columnconfigure(2, weight=1)
        self.strengthFrame.grid_columnconfigure(3, weight=1)

        self.strengthFrame.grid_columnconfigure(0, minsize=300)

        self.strengthFrame.grid(row=1, column=0, sticky="NEWS")


    def addAgilityFrame(self):
        self.agilityFrame = Frame()

        self.agility = Label(self.agilityFrame, text="Agility: ", anchor=W, font=self.generalFont, width=10)

        self.agiAmount = IntVar()
        self.agiAmount.set(self.game.player.agility)
        self.agilityAmount = Label(self.agilityFrame, textvariable=self.agiAmount, font=self.generalFont, anchor=N)

        self.subAgility = Button(self.agilityFrame, text="-", relief=GROOVE, justify=RIGHT, command=lambda : self.chngAgi(-1), font=self.generalFont)
        self.addAgility = Button(self.agilityFrame, text="+", relief=GROOVE, justify=RIGHT, command=lambda : self.chngAgi(1), font=self.generalFont)

        self.agility.grid(row=0, column=0, sticky="NWS")
        self.subAgility.grid(row=0, column=1, sticky="NWS")
        self.agilityAmount.grid(row=0, column=2)
        self.addAgility.grid(row=0, column=3, sticky="NWS")

        self.agilityFrame.grid_columnconfigure(0, minsize=300)

        self.agilityFrame.grid(row=2, column=0, sticky="NEWS")


    def addIntelligenceFrame(self):
        self.intelligenceFrame = Frame()

        self.intelligence = Label(self.intelligenceFrame, text="Intelligence: ", anchor=W, font=self.generalFont, width=10)

        self.intAmount = IntVar()
        self.intAmount.set(self.game.player.intelligence)
        self.intelligenceAmount = Label(self.intelligenceFrame, textvariable=self.intAmount, font=self.generalFont, anchor=N)

        self.subIntelligence = Button(self.intelligenceFrame, text="-", relief=GROOVE, justify=RIGHT, command=lambda : self.chngInt(-1), font=self.generalFont)
        self.addIntelligence = Button(self.intelligenceFrame, text="+", relief=GROOVE, justify=RIGHT, command=lambda : self.chngInt(1), font=self.generalFont)

        self.intelligence.grid(row=0, column=0, sticky="NWS")
        self.subIntelligence.grid(row=0, column=1, sticky="NWS")
        self.intelligenceAmount.grid(row=0, column=2)
        self.addIntelligence.grid(row=0, column=3, sticky="NWS")

        self.intelligenceFrame.grid_columnconfigure(0, minsize=300)

        self.intelligenceFrame.grid(row=3, column=0, sticky="NEWS")


    def chngStr(self, amount):
        self.points.set(self.points.get()-amount)
        self.strAmount.set(self.strAmount.get()+amount)
        if(amount == -1):
            self.minusClicked += 1
        self.updateButtons()

    def chngAgi(self, amount):
        self.points.set(self.points.get()-amount)
        self.agiAmount.set(self.agiAmount.get()+amount)
        if(amount == -1):
            self.minusClicked += 1
        self.updateButtons()

    def chngInt(self, amount):
        self.points.set(self.points.get()-amount)
        self.intAmount.set(self.intAmount.get()+amount)
        if(amount == -1):
            self.minusClicked += 1
        self.updateButtons()


    def updateButtons(self):
        if(self.strAmount.get() == 0 or self.minusClicked >= 3):
            self.subStrength.config(state=DISABLED)
        else:
            self.subStrength.config(state=ACTIVE)

        if(self.agiAmount.get() == 0 or self.minusClicked >= 3):
            self.subAgility.config(state=DISABLED)
        else:
            self.subAgility.config(state=ACTIVE)

        if(self.intAmount.get() == 0 or self.minusClicked >= 3):
            self.subIntelligence.config(state=DISABLED)
        else:
            self.subIntelligence.config(state=ACTIVE)

        if(self.points.get() == 0):
            self.addStrength.config(state=DISABLED)
            self.addAgility.config(state=DISABLED)
            self.addIntelligence.config(state=DISABLED)
        else:
            self.addStrength.config(state=ACTIVE)
            self.addAgility.config(state=ACTIVE)
            self.addIntelligence.config(state=ACTIVE)


    def configureGrid(self):
        for i in range(4):
            self.grid_rowconfigure(i, weight=1)

        self.grid_rowconfigure(4, minsize=100)

        self.grid_columnconfigure(0, weight=1, minsize=400)


    def addButton(self):
        self.doneButton = Button(text="Done", relief=GROOVE, command=self.done, font=self.generalFont)
        self.doneButton.grid(row=5, sticky="NEWS")


    def done(self):
        self.game.player.strength = self.strAmount.get()
        self.game.player.agility = self.agiAmount.get()
        self.game.player.intelligence = self.intAmount.get()
        self.game.guiHandler.back(1)
