from tkinter import *
from tkinter import font
from . import CharacterCreation, MainMenu, TownScreen, PlayerInventory, LevelUp, LoadScreen
from .ShopGUIs import StoreScreen, BlacksmithScreen, ChallengeScreen
from .DungeonGUIs import DungeonScreen, RoomScreen, GameOver
from ..Items.Inventory import Empty
from .. import ArtHandler

from .GUIIndexes import *
MM = MainMenu
CC = CharacterCreation
TS = TownScreen
SS = StoreScreen
PI = PlayerInventory
BS = BlacksmithScreen
LU = LevelUp
CS = ChallengeScreen
LS = LoadScreen
DS = DungeonScreen
RS = RoomScreen
GO = GameOver
del CharacterCreation, MainMenu, TownScreen, StoreScreen, PlayerInventory, BlacksmithScreen, LevelUp, ChallengeScreen, LoadScreen, DungeonScreen, RoomScreen, GameOver


class GUIHandler(object):
    def __init__(self, game):
        self.game = game
        self.windowInfo = (1000, 600, 150, 150)
        self.GUIs = [MM.MainMenu, CC.CharacterCreation, TS.TownScreen, SS.StoreScreen, PI.PlayerInventory, BS.BlacksmithScreen, LU.LevelUp, CS.ChallengeScreen, LS.LoadScreen,
                            DS.DungeonScreen, RS.RoomScreen, GO.GameOver]
        self.previousIndex = 0

    def start(self):
        self.previousIndex = 0
        self.currentGUI = self.GUIs[MAIN_MENU](self.game)
        self.currentGUI.mainloop()

    def unloadGUIs(self):
        g = self.GUIs.index(self.currentGUI.__class__)
        self.currentGUI.destroy()
        self.GUIs = []
        self.currentGUI = 0
        return g

    def loadGUIs(self, gui):
        self.GUIs = [MM.MainMenu, CC.CharacterCreation, TS.TownScreen, SS.StoreScreen, PI.PlayerInventory, BS.BlacksmithScreen, LU.LevelUp, CS.ChallengeScreen, LS.LoadScreen,
                            DS.DungeonScreen, RS.RoomScreen, GO.GameOver]
        self.currentGUI = self.GUIs[gui](self.game)


    def swapGUI(self, new, flag=0):
        if(flag==0):
            self.updateWInfo()
        self.previousIndex = self.GUIs.index(self.currentGUI.__class__)
        self.currentGUI.destroy()
        self.currentGUI = self.GUIs[new](self.game)
        self.currentGUI.mainloop()

    def back(self, update=0):
        if(update==0):
            self.updateWInfo()
        self.currentGUI.destroy()
        self.currentGUI = self.GUIs[self.previousIndex](self.game)
        self.currentGUI.mainloop()

    def updateWInfo(self):
        self.windowInfo = (self.currentGUI.winfo_width(), self.currentGUI.winfo_height(), self.currentGUI.winfo_x(), self.currentGUI.winfo_y())

    def addPlayerInfo(self, app, flag=0):
        if(flag==0):
            player = app.game.player
        else:
            player = app.selectedGame.player

        app.playerInfo = Frame()

        app.coin = PhotoImage(file=ArtHandler.Coin).subsample(5, 5)
        app.xp = PhotoImage(file=ArtHandler.XP).subsample(5, 5)
        app.hp = PhotoImage(file=ArtHandler.HP).subsample(5, 5)
        app.ap = PhotoImage(file=ArtHandler.AP).subsample(5, 5)

        app.nameLabel = Label(app.playerInfo, text="{} lvl {}".format(player.name, player.level), font=app.nameFont, anchor=SW)
        app.moneyLabel = Label(app.playerInfo, image=app.coin, compound=RIGHT, text="{} ".format(player.money), font=app.generalFont, anchor=SE, pady=10)
        app.moneyLabel.image = app.coin

        BAR_HEIGHT = 20
        BAR_WIDTH = 150

        app.hpFrame = Frame(app.playerInfo)

        app.healthBar = Canvas(app.hpFrame, height=BAR_HEIGHT, width=BAR_WIDTH, bd=5, relief=RAISED)
        app.healthBar.create_rectangle(5, 5, ((player.currentHealth/player.totalHealth)*BAR_WIDTH)+7, BAR_HEIGHT+10, fill="green")
        app.healthLabel = Label(app.hpFrame, text="HP : {}/{}".format(player.currentHealth, player.totalHealth), font=app.generalFont)

        app.hpSymbol = Label(app.hpFrame, image=app.hp)

        app.healthBar.grid(row=0, column=0, sticky="W")
        app.healthLabel.grid(row=0, column=2, sticky="NES")
        app.hpSymbol.grid(row=0, column=1, sticky="NES")

        app.hpFrame.grid(row=1, column=0, columnspan=2, sticky="NEWS")

        app.hpFrame.grid_columnconfigure(0, weight=1)
        app.hpFrame.grid_columnconfigure(1, weight=1)
        app.hpFrame.grid_columnconfigure(2, weight=1)

        app.apFrame = Frame(app.playerInfo)

        app.apBar = Canvas(app.apFrame, height=BAR_HEIGHT, width=BAR_WIDTH, bd=5, relief=RAISED)
        app.apBar.create_rectangle(5, 5, ((player.currentActionPoints/player.totalActionPoints)*BAR_WIDTH)+7, BAR_HEIGHT+10, fill="yellow")
        app.apLabel = Label(app.apFrame, text="AP : {}/{}".format(player.currentActionPoints, player.totalActionPoints), font=app.generalFont)

        app.apSymbol = Label(app.apFrame, image=app.ap)

        app.apBar.grid(row=0, column=0, sticky="W")
        app.apLabel.grid(row=0, column=2, sticky="NES")
        app.apSymbol.grid(row=0, column=1, sticky="NES")

        app.apFrame.grid(row=2, column=0, columnspan=2, sticky="NEWS")

        app.apFrame.grid_columnconfigure(0, weight=1)
        app.apFrame.grid_columnconfigure(1, weight=1)
        app.apFrame.grid_columnconfigure(2, weight=1)


        app.xpFrame = Frame(app.playerInfo)

        app.xpBar = Canvas(app.xpFrame, height=BAR_HEIGHT-10, width=BAR_WIDTH, bd=5, relief=RAISED)
        app.xpBar.create_rectangle(5, 5, ((player.xp/player.xpToNext)*BAR_WIDTH)+7, BAR_HEIGHT, fill="blue")
        app.xpLabel = Label(app.xpFrame, text="XP : {}/{}".format(player.xp, player.xpToNext), font=app.generalFont)

        app.xpSymbol = Label(app.xpFrame, image=app.xp)

        app.xpBar.grid(row=0, column=0, sticky="W")
        app.xpLabel.grid(row=0, column=2, sticky="NES")
        app.xpSymbol.grid(row=0, column=1, sticky="NES")

        app.xpFrame.grid(row=3, column=0, columnspan=2, sticky="NEWS")

        app.xpFrame.grid_columnconfigure(0, weight=1)
        app.xpFrame.grid_columnconfigure(1, weight=1)
        app.xpFrame.grid_columnconfigure(2, weight=1)

        app.strLabel = Label(app.playerInfo, text="Strength", font=app.generalFont, anchor=SW)
        app.strNumber = Label(app.playerInfo, text="{}".format(player.strength), font=app.generalFont, anchor=SE)

        app.agiLabel = Label(app.playerInfo, text="Agility", font=app.generalFont, anchor=SW)
        app.agiNumber = Label(app.playerInfo, text="{}".format(player.agility), font=app.generalFont, anchor=SE)

        app.intLabel = Label(app.playerInfo, text="Intelligence", font=app.generalFont, anchor=SW)
        app.intNumber = Label(app.playerInfo, text="{}".format(player.intelligence), font=app.generalFont, anchor=SE)

        app.damageLabel = Label(app.playerInfo, text="Damage", font=app.generalFont, anchor=SW)
        app.damageAmount = Label(app.playerInfo, text=player.equipment.slots[0].item.getDamageForLabel(player), font=app.generalFont, anchor=SE)

        app.defenseLabel = Label(app.playerInfo, text="Defense", font=app.generalFont, anchor=SW)
        app.defenseAmount = Label(app.playerInfo, text=player.equipment.defense, font=app.generalFont, anchor=SE)

        app.hpRegenLabel = Label(app.playerInfo, text="HP Regen", font=app.generalFont, anchor=SW)
        app.hpRegenAmount = Label(app.playerInfo, text=player.healthRegen, font=app.generalFont, anchor=SE)

        app.apRegenLabel = Label(app.playerInfo, text="AP Regen", font=app.generalFont, anchor=SW)
        app.apRegenAmount = Label(app.playerInfo, text=player.actionPointRegen, font=app.generalFont, anchor=SE)

        app.speedLabel = Label(app.playerInfo, text="Speed", font=app.generalFont, anchor=SW)
        app.speedAmount = Label(app.playerInfo, text=player.speed, font=app.generalFont, anchor=SE)

        app.weightLabel = Label(app.playerInfo, text="Weight", font=app.generalFont, anchor=SW)
        app.weightAmount = Label(app.playerInfo, text=player.weight, font=app.generalFont, anchor=SE)


        app.nameLabel.grid(row=0, sticky=NW)
        app.moneyLabel.grid(row=0, column=1, sticky="NES")

        app.strLabel.grid(row=3+1, column=0, sticky=NW)
        app.strNumber.grid(row=3+1, column=1, sticky="NES")

        app.agiLabel.grid(row=4+1, column=0, sticky=NW)
        app.agiNumber.grid(row=4+1, column=1, sticky="NES")

        app.intLabel.grid(row=5+1, column=0, sticky=NW)
        app.intNumber.grid(row=5+1, column=1, sticky="NES")

        app.damageLabel.grid(row=7+1, column=0, sticky=NW)
        app.damageAmount.grid(row=7+1, column=1, sticky="NES")

        app.defenseLabel.grid(row=8+1, column=0, sticky=NW)
        app.defenseAmount.grid(row=8+1, column=1, sticky="NES")

        app.hpRegenLabel.grid(row=9+1, column=0, sticky=NW)
        app.hpRegenAmount.grid(row=9+1, column=1, sticky="NES")

        app.apRegenLabel.grid(row=10+1, column=0, sticky=NW)
        app.apRegenAmount.grid(row=10+1, column=1, sticky="NES")

        app.speedLabel.grid(row=11+1, column=0, sticky=NW)
        app.speedAmount.grid(row=11+1, column=1, sticky="NES")

        app.weightLabel.grid(row=12+1, column=0, sticky=NW)
        app.weightAmount.grid(row=12+1, column=1, sticky="NES")

        for i in range(13):
            app.playerInfo.grid_rowconfigure(i, weight=1, minsize=15)
        app.playerInfo.grid_columnconfigure(0, weight=1)
        app.playerInfo.grid_columnconfigure(1, weight=1)
