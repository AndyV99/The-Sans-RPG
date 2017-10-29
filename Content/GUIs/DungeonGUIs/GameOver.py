from tkinter import *
from ..GUIIndexes import *
from tkinter import font

class GameOver(Tk):
    def __init__(self, game):
        Tk.__init__(self)
        self.game = game
        self.geometry('%dx%d+%d+%d' % self.game.guiHandler.windowInfo)
        self.minsize(1000, 600)
        self.wm_title("YOU DIED")

        self.fontFont = font.Font(family="Comic Sans MS", size=36)
        self.buttonFont = font.Font(family="Comic Sans MS", size=20)

        self.gameOverLabel = Label(text="GAME OVER", font=self.fontFont)
        self.gameOverLabel.grid(row=0, column=0, sticky="NEWS")

        self.mainMenuButton = Button(text="Main Menu", font=self.buttonFont, command=self.mainMenu)
        self.mainMenuButton.grid(row=1, column=0, sticky="NS")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=5)
        self.grid_rowconfigure(1, weight=1)

    def mainMenu(self):
        self.game.guiHandler.swapGUI(MAIN_MENU)
