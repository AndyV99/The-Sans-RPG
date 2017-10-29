from tkinter import *
from tkinter import font
import os
import pickle

class LoadScreen(Tk):
    def __init__(self, game):
        Tk.__init__(self)
        self.game = game
        self.geometry('%dx%d+%d+%d' % self.game.guiHandler.windowInfo)
        self.minsize(1000, 600)
        self.titleFont = font.Font(family="Comic Sans MS", size=30, weight=font.BOLD)
        self.generalFont = font.Font(family="Comic Sans MS", size=18)
        self.nameFont = font.Font(family="Comic Sans MS", size = 22, weight=font.BOLD)

        self.currentFile = 0

        self.location = ""

        self.addLabels()
        self.addListbox()
        self.addBackButton()
        self.addLoadButton()
        self.addDeleteButton()

        self.current = None
        self.selectedGame= None

        self.poll()

    def addLabels(self):
        self.loadLabel = Label(text="Load Game", font=self.titleFont)
        self.loadLabel.grid(row=0, column=0, columnspan=3, sticky="NEWS")

    def addListbox(self):
        self.saveFileListbox = Listbox(font=self.generalFont)
        self.location, saves = self.game.getSaveFiles()
        for file in saves:
            self.saveFileListbox.insert(END, file[:-7])


        self.saveFileListbox.grid(row=1, column=0, sticky="NEWS")
        self.saveFileListbox.selection_set(0)


    def poll(self):
        now = self.saveFileListbox.get(ACTIVE)
        if now != self.current:
            self.current = now
            self.updateGameInfo()
        self.after(250, self.poll)


    def updateGameInfo(self):
        gameFile = open("{}\saves\{}.player".format(self.location, self.current), "r+b")
        self.selectedGame = pickle.load(gameFile)

        self.gameInfoFrame = Frame()
        self.selectedGame.guiHandler.addPlayerInfo(self, self.selectedGame.player)

        self.playerInfo.grid(row=1, column=1, rowspan=2, sticky="NEWS")


    def addDeleteButton(self):
        self.deleteButton = Button(text="Delete Save", font=self.generalFont, command=self.delete)
        self.deleteButton.grid(row=2, column=2, sticky="NEWS")


    def delete(self):
        os.remove("{}\saves\{}.player".format(self.location, self.current))
        self.addListbox()


    def addLoadButton(self):
        self.loadButton = Button(text="Load Game", font=self.generalFont, command=self.load)
        self.loadButton.grid(row=1, column=2, sticky="NEWS")


    def load(self):
        self.game.load(self.selectedGame)


    def addBackButton(self):
        self.backButton = Button(text="Back", font=self.generalFont, command=self.back)
        self.backButton.grid(row=2, column=0, sticky="NEWS")


    def back(self):
        self.game.guiHandler.back()
