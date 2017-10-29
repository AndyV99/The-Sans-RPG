from Content.Beings import Player, Enemy
from Content.Items.Weapons import Weapons, Swords, Wands, Staffs, Hammers, Daggers, BattleStaffs, Bows
from Content.Items.Armor import Armor, HeadArmor, TorsoArmor, LegArmor
from Content.Items import Items, Food, Tiers
from Content.Towns import Towns, Shops
from Content.Modifiers import Modifiers, WeaponModifiers
from Content.GUIs import GUI, MainMenu, CharacterCreation, TownScreen, GUIIndexes, LevelUp, PlayerInventory
from Content.GUIs.ShopGUIs import BlacksmithScreen, ChallengeScreen, StoreScreen
from Content.Enemies import Enemies
from Content.Dungeons import Dungeons, Rooms
from math import *
import pickle
import os
from os.path import dirname, abspath
import random
d = dirname(abspath(__file__))


class Game(object):
    def __init__(self):
        self.guiHandler = GUI.GUIHandler(self)

        self.player = Player()

        self.level = 1

        self.towns = [Towns.Town(game=self, level=self.level)]
        self.currentTown = 0
        self.towns[0].newDungeon()
        #self.nextTown()

        self.g = 0

        self.guiHandler.start()

    def prevTown(self):
        self.currentTown -= 1

    def nextTown(self):
        if(self.towns[self.currentTown] == self.towns[-1]):
            self.level += random.uniform(0.3, 0.8)
            self.towns.append(Towns.Town(game=self, level=self.level))
            self.towns[-1].newDungeon()
        self.currentTown += 1

    def getCurrentTown(self):
        return self.towns[self.currentTown]

    def addXPToPlayer(self, amount):
        if(self.player.addXP(amount)):
            self.player.levelUp()
            self.guiHandler.swapGUI(GUIIndexes.LEVEL_UP)

    def save(self, event):
        if(event.char == 's'):
            gameFile = open(d + "\saves\{}.player".format(self.player.name), "w+b")
            self.g = self.guiHandler.unloadGUIs()
            pickle.dump(self, gameFile)
            self.guiHandler.loadGUIs(self.g)

    def load(self, newGame):
        self.guiHandler.currentGUI.destroy()
        self = newGame
        self.guiHandler.loadGUIs(self.g)

    def getSaveFiles(self):
        files = []
        for file in os.listdir(d + "\saves"):
            if file.endswith(".player"):
                files.append(file)
        return d, files

game = Game()


"""
TESTING FUNCTIONS
"""
def swordDamage():
    #---DAMAGE OF SWORD---
    s = Swords.WoodenSword()
    four = 0
    five = 0
    six = 0
    seven = 0


    values = [0]*100


    for i in range(100):
        damage = s.getDamage(Player())
        print("{}: {}".format(i, damage))
        values[damage] += 1

    for l in range(0, len(values)):
        if(values[l] != 0):
            print("{}: {}".format(l, values[l]))


def buffsOfSwords(weapon=Swords.StoneSword):
    #---BUFFS OF RANDOM SWORDS---
    for i in range(25):
    	l = weapon()
    	print("Sword #: {}\nstr: {}\nagi: {}\nint: {}\n".format(i, l.strBuff, l.agiBuff, l.intBuff))


def modifierStats():
    #---MODIFIERS OF RANDOM SWORDS---
    vals = [0]*len(WeaponModifiers.WEAPON_MODIFIERS)
    swords = 1000

    for p in range(swords):
        m = Swords.StoneSword()
        m.equipModifiers = []
        #CHANCES = PLAYERLEVEL//3
        m.generateModifiers(4)

        for mod in m.equipModifiers:
            vals[WeaponModifiers.WEAPON_MODIFIERS.index(mod)] += 1
        m.addModifiers()
        print(m.name)

    chanceForMod=0
    for l in range(len(WeaponModifiers.WEAPON_MODIFIERS)):
        total = sum(vals)
        percent = round(100*(vals[l]/total), 2)
        totalChance = round(100*(vals[l]/swords), 2)
        chanceForMod += totalChance
        print("{}: {} | {}% of modifiers, | {}% of all chances.".format(WeaponModifiers.WEAPON_MODIFIERS[l].prefix, vals[l], percent, totalChance))
    print("Final chance for any modifier: {}".format(round(chanceForMod,2)))


def randomModifierStats():
    for mod in WeaponModifiers.WEAPON_MODIFIERS:
        print("{}: Value: {} | Weight: {} | str: {} | agi: {} | int: {}".format(mod.prefix, mod.valueBuff, mod.weightBuff, mod.strBuff, mod.agiBuff, mod.intBuff))
