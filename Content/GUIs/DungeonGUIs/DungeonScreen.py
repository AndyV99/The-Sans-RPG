from tkinter import *
from tkinter import font
from ..GUIIndexes import *


class DungeonScreen(Tk):
    def __init__(self, game):
        Tk.__init__(self)
        self.game = game
        self.dungeon = self.game.getCurrentTown().dungeon

        self.titleFont = font.Font(family="Comic Sans MS", size=24)
        self.buttonFont = font.Font(family="Comic Sans MS", size=18)
        self.generalFont = font.Font(family="Comic Sans MS", size=18)
        self.nameFont = font.Font(family="Comic Sans MS", size=20, weight=font.BOLD)

        self.geometry('%dx%d+%d+%d' % self.game.guiHandler.windowInfo)
        self.minsize(1000, 600)
        self.wm_title(self.dungeon.name)

        self.addPlayerInfo()
        self.addDungeonInfoPanel()


    def addPlayerInfo(self):
        self.game.guiHandler.addPlayerInfo(self)
        self.inventoryButton = Button(self.playerInfo, text="Inventory", font=self.generalFont, command=self.openInventory)
        self.inventoryButton.grid(row=14, column=0, columnspan=2, rowspan=3, sticky="NEWS")

        self.playerInfo.grid(row=0, column=0)


    def openInventory(self):
        self.game.guiHandler.swapGUI(PLAYER_INVENTORY)


    def backToTown(self):
        self.game.guiHandler.swapGUI(TOWN_SCREEN)


    def addDungeonInfoPanel(self):
        self.dungeonInfoFrame = Frame()

        roomsLeft = len(self.dungeon.rooms) - (self.dungeon.currentRoom)
        self.dungeonNameLabel = Label(self.dungeonInfoFrame, text="{} lvl {}  {} Rooms Left".format(self.dungeon.name, self.dungeon.level, roomsLeft), font=self.titleFont, anchor=W)
        self.dungeonNameLabel.grid(row=0, column=0, columnspan=2, sticky="NEWS")

        room = self.dungeon.rooms[self.dungeon.currentRoom]
        self.roomInfoLabel = Label(self.dungeonInfoFrame, text="Next Room: ", font=self.buttonFont, anchor=W)
        self.roomInfoLabel.grid(row=1, column=0, columnspan=2, sticky="NEWS")


        enemies = room.getPossibleEnemies()
        enemyList = ", ".join(enemies)

        self.possibleEnemiesLabel = Label(self.dungeonInfoFrame, text="    Possible Enemies: {}".format(enemyList), font=self.buttonFont, anchor=W)
        self.possibleEnemiesLabel.grid(row=2, column=0, sticky="NEWS")

        self.enemyLevelLabel = Label(self.dungeonInfoFrame, text="    Enemy Level: {}".format(self.dungeon.level), font=self.buttonFont, anchor=W)
        self.enemyLevelLabel.grid(row=3, column=0, sticky="NEWS")

        self.numOfEnemiesLabel = Label(self.dungeonInfoFrame, text="    Number of Enemies: {}".format(room.numOfEnemies), font=self.buttonFont, anchor=W)
        self.numOfEnemiesLabel.grid(row=4, column=0, sticky="NEWS")

        loot = room.getPossibleLoot()
        lootList = ", ".join(loot)
        #self.possibleLootLabel = Label(self.dungeonInfoFrame, text="    Possible Loot: {}".format(lootList), wraplength=700, font=self.buttonFont, anchor=W, justify=LEFT)
        #self.possibleLootLabel.grid(row=5, column=0, sticky="NEWS")

        self.enterRoomButton = Button(self.dungeonInfoFrame, text="Enter Room", font=self.generalFont, command=self.nextRoom)
        self.enterRoomButton.grid(row=6, column=0, sticky="NEWS")

        self.backToTownButton = Button(self.dungeonInfoFrame, text="Back to Town", font=self.generalFont, command=self.backToTown)
        self.backToTownButton.grid(row=7, column=0, sticky="NEWS")

        self.dungeonInfoFrame.grid(row=0, column=1, columnspan=2, sticky="NEWS")

    def nextRoom(self):
        self.game.guiHandler.swapGUI(ROOM_SCREEN)

    def configureGrid(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
