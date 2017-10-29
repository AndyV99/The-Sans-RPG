import random
from . import Rooms
from ..GUIs.GUIIndexes import *

class Dungeon(object):
    def __init__(self, game, level=1):
        self.game = game
        self.town = self.game.getCurrentTown()
        self.name = "{} Dungeon".format(self.town.name)
        self.level = round(random.uniform(level-0.5, level+0.5), 1)
        self.numOfRooms = random.randint(round((level*3)-1), round((level*4)))
        self.currentRoom = 0
        self.rooms = []

        self.generateRooms()

    def generateRooms(self):
        for i in range(self.numOfRooms):
            self.rooms.append(Rooms.Room(self.game, roomLevel=(i+1)/2, enemyLevel=self.level, numOfEnemies=random.randint((i+1), (i+1)*2)))

    def getCurrentRoom(self):
        return self.rooms[self.currentRoom]

    def nextRoom(self):
        if(self.currentRoom+1 == len(self.rooms)):
            self.town.isDungeonDone = True
            self.game.guiHandler.swapGUI(TOWN_SCREEN)
        else:
            self.currentRoom += 1
