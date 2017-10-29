from tkinter import *
from tkinter import font
from ... import ArtHandler
from ...Towns import Shops
from ..GUIIndexes import *

class ChallengeScreen(Tk):
    def __init__(self, game):
        Tk.__init__(self)
        self.game = game
        self.player = self.game.player
        self.shop = game.getCurrentTown().shops[game.getCurrentTown().index]

        self.geometry('650x600+{}+{}'.format(self.game.guiHandler.windowInfo[2]+300, self.game.guiHandler.windowInfo[3]))
        self.minsize(650, 600)
        self.wm_title("{}".format(self.shop.shopName))

        self.bind("<Key>", self.game.save)

        self.generalFont = font.Font(family="Comic Sans MS", size=18)
        self.biggerFont = font.Font(family="Comic Sans MS", size=22)
        self.nameFont = font.Font(family="Comic Sans MS", size = 24, weight=font.BOLD)

        self.coinImage = PhotoImage(file=ArtHandler.Coin).subsample(5, 5)
        self.hpImage = PhotoImage(file=ArtHandler.HP).subsample(5, 5)
        self.apImage = PhotoImage(file=ArtHandler.AP).subsample(5, 5)
        self.xpImage = PhotoImage(file=ArtHandler.XP).subsample(5, 5)

        self.results = []

        self.addPlayerInformationPanel()
        self.addBackButton()
        if(self.shop.__class__ == Shops.Arena):
            self.addArena()
        elif(self.shop.__class__ == Shops.ArcheryRange):
            self.addArcheryRange()
        elif(self.shop.__class__ == Shops.Library):
            self.addLibrary()
        self.configureGrid()
        self.updateButton()


    def addPlayerInformationPanel(self):
        self.game.guiHandler.addPlayerInfo(self)
        self.playerInfo.grid(row=0, column=0, rowspan=2, sticky="NSEW")

    def addBackButton(self):
        self.backButton = Button(text="Back", font=self.generalFont, command=self.back)
        self.backButton.grid(row=2, column=0, sticky="NEWS")

    def back(self):
        self.game.guiHandler.swapGUI(TOWN_SCREEN, 1)

    def addArena(self):
        moneyRange = "{} to {}".format(int(self.player.strength*(self.shop.scale-0.5)), int(self.player.strength*(self.shop.scale+0.5)))
        xpRange = "{} to {}".format(int(self.player.strength*(self.shop.scale-0.5)), int(self.player.strength*(self.shop.scale+0.5)))
        hpRange = "{} to {}".format(int(max(min((self.shop.scale-0.5)*(self.player.totalHealth/3), self.game.player.totalHealth-10), 1)), int(max(min((self.shop.scale+0.5)*(self.player.totalHealth/3), self.game.player.totalHealth-10), 1)))
        apRange = "{} to {}".format(int(max(min((self.shop.scale-0.5)*(self.player.totalActionPoints/3), self.game.player.totalActionPoints-10), 1)), int(max(min((self.shop.scale+0.5)*(self.player.totalActionPoints/3), self.game.player.totalActionPoints-10), 1)))

        self.gainsAndLosses = Frame()

        self.explanationLabel = Label(self.gainsAndLosses, text="You could gain:", font=self.biggerFont)
        self.moneyLabel = Label(self.gainsAndLosses, image=self.coinImage, text=moneyRange, compound=RIGHT, font=self.generalFont)
        self.xpLabel = Label(self.gainsAndLosses, image=self.xpImage, text=xpRange, compound=RIGHT, font=self.generalFont)

        self.explanationLabel.grid(row=0, column=0, rowspan=2, sticky="NEWS")
        self.moneyLabel.grid(row=0, column=1, sticky="NEWS")
        self.xpLabel.grid(row=1, column=1, sticky="NEWS")

        self.explanationLabel2 = Label(self.gainsAndLosses, text="You could lose:", font=self.biggerFont)
        self.hpLabel = Label(self.gainsAndLosses, image=self.hpImage, text=hpRange, compound=RIGHT, font=self.generalFont)
        self.apLabel = Label(self.gainsAndLosses, image=self.apImage, text=apRange, compound=RIGHT, font=self.generalFont)

        self.explanationLabel2.grid(row=3, column=0, rowspan=2, sticky="NEWS")
        self.hpLabel.grid(row=3, column=1, sticky="NEWS")
        self.apLabel.grid(row=4, column=1, sticky="NEWS")

        self.competeButton = Button(self.gainsAndLosses, text="Compete", font=self.biggerFont, command=self.doChallenge)
        self.competeButton.grid(row=5, column=0, columnspan=2, sticky="NEWS")


        self.gainsAndLosses.grid_rowconfigure(0, minsize=35, weight=1)
        self.gainsAndLosses.grid_rowconfigure(1, minsize=35, weight=1)
        self.gainsAndLosses.grid_rowconfigure(2, minsize=25, weight=1)
        self.gainsAndLosses.grid_rowconfigure(3, minsize=35, weight=1)
        self.gainsAndLosses.grid_rowconfigure(4, minsize=35, weight=1)
        self.gainsAndLosses.grid_rowconfigure(5, minsize=20, weight=1)

        self.gainsAndLosses.grid_columnconfigure(0, weight=1)
        self.gainsAndLosses.grid_columnconfigure(1, weight=1)

        self.gainsAndLosses.grid(row=0, column=1, sticky="NEWS")

        self.updateButton()


    def addArcheryRange(self):
        moneyRange = "{} to {}".format(int(self.player.agility*(self.shop.scale-0.5)), int(self.player.agility*(self.shop.scale+0.5)))
        xpRange = "{} to {}".format(int(self.player.agility*(self.shop.scale-0.5)), int(self.player.agility*(self.shop.scale+0.5)))
        apRange = "{} to {}".format(int(max(min((self.shop.scale-0.5)*(self.player.totalActionPoints/3), self.game.player.totalActionPoints-10), 1)), int(max(min((self.shop.scale+0.5)*(self.player.totalActionPoints/3), self.game.player.totalActionPoints-10), 1)))

        self.gainsAndLosses = Frame()

        self.explanationLabel = Label(self.gainsAndLosses, text="You could gain:", font=self.biggerFont)
        self.moneyLabel = Label(self.gainsAndLosses, image=self.coinImage, text=moneyRange, compound=RIGHT, font=self.generalFont)
        self.xpLabel = Label(self.gainsAndLosses, image=self.xpImage, text=xpRange, compound=RIGHT, font=self.generalFont)

        self.explanationLabel.grid(row=0, column=0, rowspan=2, sticky="NEWS")
        self.moneyLabel.grid(row=0, column=1, sticky="NEWS")
        self.xpLabel.grid(row=1, column=1, sticky="NEWS")

        self.explanationLabel2 = Label(self.gainsAndLosses, text="You could lose:", font=self.biggerFont)
        self.apLabel = Label(self.gainsAndLosses, image=self.apImage, text=apRange, compound=RIGHT, font=self.generalFont)

        self.explanationLabel2.grid(row=3, column=0, rowspan=2, sticky="NEWS")
        self.apLabel.grid(row=3, column=1, rowspan=2, sticky="NEWS")

        self.competeButton = Button(self.gainsAndLosses, text="Compete", font=self.biggerFont, command=self.doChallenge)
        self.competeButton.grid(row=5, column=0, columnspan=2, sticky="NEWS")


        self.gainsAndLosses.grid_rowconfigure(0, minsize=35, weight=1)
        self.gainsAndLosses.grid_rowconfigure(1, minsize=35, weight=1)
        self.gainsAndLosses.grid_rowconfigure(2, minsize=25, weight=1)
        self.gainsAndLosses.grid_rowconfigure(3, minsize=35, weight=1)
        self.gainsAndLosses.grid_rowconfigure(4, minsize=35, weight=1)
        self.gainsAndLosses.grid_rowconfigure(5, minsize=20, weight=1)

        self.gainsAndLosses.grid_columnconfigure(0, weight=1)
        self.gainsAndLosses.grid_columnconfigure(1, weight=1)

        self.gainsAndLosses.grid(row=0, column=1, sticky="NEWS")

        self.updateButton()


    def addLibrary(self):
        moneyRange = "{} to {}".format(int(self.player.intelligence*(self.shop.scale-0.5)), int(self.player.intelligence*(self.shop.scale+0.5)))
        xpRange = "{} to {}".format(int(self.player.intelligence*(self.shop.scale-0.5)), int(self.player.intelligence*(self.shop.scale+0.5)))
        apRange = "{} to {}".format(int(max(min((self.shop.scale-0.5)*(self.player.totalActionPoints/3), self.game.player.totalActionPoints-10), 1)), int(max(min((self.shop.scale+0.5)*(self.player.totalActionPoints/3), self.game.player.totalActionPoints-10), 1)))

        self.gainsAndLosses = Frame()

        self.explanationLabel = Label(self.gainsAndLosses, text="You could gain:", font=self.biggerFont)
        self.moneyLabel = Label(self.gainsAndLosses, image=self.coinImage, text=moneyRange, compound=RIGHT, font=self.generalFont)
        self.xpLabel = Label(self.gainsAndLosses, image=self.xpImage, text=xpRange, compound=RIGHT, font=self.generalFont)

        self.explanationLabel.grid(row=0, column=0, rowspan=2, sticky="NEWS")
        self.moneyLabel.grid(row=0, column=1, sticky="NEWS")
        self.xpLabel.grid(row=1, column=1, sticky="NEWS")

        self.explanationLabel2 = Label(self.gainsAndLosses, text="You could lose:", font=self.biggerFont)
        self.apLabel = Label(self.gainsAndLosses, image=self.apImage, text=apRange, compound=RIGHT, font=self.generalFont)

        self.explanationLabel2.grid(row=3, column=0, rowspan=2, sticky="NEWS")
        self.apLabel.grid(row=3, column=1, rowspan=2, sticky="NEWS")

        self.competeButton = Button(self.gainsAndLosses, text="Compete", font=self.biggerFont, command=self.doChallenge)
        self.competeButton.grid(row=5, column=0, columnspan=2, sticky="NEWS")


        self.gainsAndLosses.grid_rowconfigure(0, minsize=35, weight=1)
        self.gainsAndLosses.grid_rowconfigure(1, minsize=35, weight=1)
        self.gainsAndLosses.grid_rowconfigure(2, minsize=25, weight=1)
        self.gainsAndLosses.grid_rowconfigure(3, minsize=35, weight=1)
        self.gainsAndLosses.grid_rowconfigure(4, minsize=35, weight=1)
        self.gainsAndLosses.grid_rowconfigure(5, minsize=20, weight=1)

        self.gainsAndLosses.grid_columnconfigure(0, weight=1)
        self.gainsAndLosses.grid_columnconfigure(1, weight=1)

        self.gainsAndLosses.grid(row=0, column=1, sticky="NEWS")

        self.updateButton()


    def updateButton(self):
        if(self.player.currentHealth < self.player.totalHealth//2 or self.player.currentActionPoints < self.player.totalActionPoints//2):
            self.competeButton.config(state=DISABLED)
        else:
            self.competeButton.config(state=NORMAL)


    def doChallenge(self):
        self. results = self.shop.doChallenge()
        self.addResults()
        self.addPlayerInformationPanel()
        self.updateButton()


    def addResults(self):
        self.resultsFrame = Frame()
        self.resultsLabel = Label(self.resultsFrame, text="Results:", font=self.biggerFont)
        self.resultsLabel.grid(row=0, column=0, rowspan=4)

        self.moneyResult = Label(self.resultsFrame, image=self.coinImage, text="+{}".format(self.results[0]), font=self.generalFont, compound=RIGHT)
        self.xpResult = Label(self.resultsFrame, image=self.xpImage, text="+{}".format(self.results[1]), font=self.generalFont, compound=RIGHT)
        self.hpResult = Label(self.resultsFrame, image=self.hpImage, text="-{}".format(self.results[2]), font=self.generalFont, compound=RIGHT)
        self.apResult = Label(self.resultsFrame, image=self.apImage, text="-{}".format(self.results[3]), font=self.generalFont, compound=RIGHT)

        self.moneyResult.grid(row=0, column=1, sticky="NEWS")
        self.xpResult.grid(row=1, column=1, sticky="NEWS")
        self.hpResult.grid(row=2, column=1, sticky="NEWS")
        self.apResult.grid(row=3, column=1, sticky="NEWS")

        self.resultsFrame.grid_columnconfigure(0, weight=1)
        self.resultsFrame.grid_columnconfigure(1, weight=1)

        self.resultsFrame.grid_rowconfigure(0, weight=1)
        self.resultsFrame.grid_rowconfigure(1, weight=1)
        self.resultsFrame.grid_rowconfigure(2, weight=1)
        self.resultsFrame.grid_rowconfigure(3, weight=1)

        self.resultsFrame.grid(row=1, column=1, sticky="NEWS")

    def configureGrid(self):
        self.grid_columnconfigure(0, weight=1, minsize=300)
        self.grid_columnconfigure(1, weight=1, minsize=350)

        self.grid_rowconfigure(0, weight=1, minsize=250)
        self.grid_rowconfigure(1, weight=1, minsize=250)
        self.grid_rowconfigure(2, weight=1, minsize=100)
