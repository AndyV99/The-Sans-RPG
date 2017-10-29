from tkinter import *
from .Items import Items, Inventory
from random import *

class Being(object):
    def __init__(self, inName="name", inLevel=1, inWeight=1.0):
        self.name = inName
        self.level = inLevel
        self.weight = inWeight

        self.totalHealth = 0
        self.currentHealth = 0
        self.healthRegen = 0


class Player(Being):
    def __init__(self, name="Player", level=1, weight=0.0,
                 inStrength=1, inAgility=1, inIntelligence=1):
        super().__init__(name, level, weight)

        self.strength = inStrength
        self.agility = inAgility
        self.intelligence = inIntelligence

        self.totalHealth = level*10
        self.currentHealth = self.totalHealth
        self.healthRegen = 0

        self.totalActionPoints = (inStrength*2) + (inAgility*3) + (inIntelligence*5)
        self.currentActionPoints = self.totalActionPoints
        self.actionPointRegen = 0

        self.money = 20

        #empty inventory and equipment slots are 0
        #weapon, helmet, torso, legs
        self.equipment = Inventory.EquipmentInventory()

        self.inventory = Inventory.Inventory()

        self.xp = 0
        self.xpToNext = 35

        self.setSpeed()
        self.updateHPandAP()


    def updateWeight(self):
        self.weight = round(self.inventory.weight + self.equipment.weight, 1)
        self.setSpeed()


    def setSpeed(self):
        self.speed = round((self.agility*10) - (self.weight*2) + (self.level*5), 1)


    def equipItem(self, item):
        self.strength += item.strBuff
        self.agility += item.agiBuff
        self.intelligence += item.intBuff
        self.equipment.equip(item)
        self.inventory.removeItem(item)
        self.updateWeight()
        self.updateArmorBuffs()


    def unequipItem(self, item):
        self.strength -= item.strBuff
        self.agility -= item.agiBuff
        self.intelligence -= item.intBuff
        self.equipment.unequip(item)
        self.inventory.addItem(item)
        self.updateWeight()
        self.updateArmorBuffs()


    def eat(self, item):
        self.currentHealth += item.healValue
        item.usesLeft -= 1
        if(item.usesLeft == 0):
            self.inventory.removeItem(item)
            item.usesLeft = item.totalUses
        self.currentHealth = max(0, min(self.currentHealth, self.totalHealth))


    def updateArmorBuffs(self):
        self.updateHPandAP()
        self.healthRegen = self.equipment.healthRegenBuff
        self.actionPointRegen = self.equipment.actionPointRegenBuff


    def updateHPandAP(self):
        hpPercent = round(self.currentHealth/self.totalHealth, 2)
        apPercent = round(self.currentActionPoints/self.totalActionPoints, 2)
        self.totalHealth = (self.level*5) + (self.strength*3) + self.equipment.healthBuff
        self.totalActionPoints =(self.strength*2) + (self.agility*3) + (self.intelligence*5) + self.equipment.actionPointBuff
        self.currentHealth = int(self.totalHealth*hpPercent)
        self.currentActionPoints = int(self.totalActionPoints*apPercent)


    def addXP(self, amount):
        self.xp += amount
        if(self.xp >= self.xpToNext):
            return True
        else:
            return False


    def levelUp(self):
        self.level += 1
        self.xp -= self.xpToNext
        self.xpToNext = (self.level*20) + ((self.level)**2)
        self.updateHPandAP()
        self.updateWeight()


    def getBlock(self):
        defe = self.equipment.defense
        return randint((defe+1)//2, defe+1)


    def passiveEffects(self):
        initHealth = self.currentHealth
        initAP = self.currentActionPoints

        self.currentHealth += self.healthRegen
        self.currentHealth = min(self.currentHealth, self.totalHealth)
        self.currentActionPoints += self.actionPointRegen
        self.currentActionPoints = min(self.currentActionPoints, self.totalActionPoints)

        healthGain = self.currentHealth-initHealth
        apGain = self.currentActionPoints-initAP

        return healthGain, apGain



class Enemy(Being):
    def __init__(self, name="", level=1, inWeight=1.0):
        super().__init__(name, level, inWeight)
        self.damage = 1
        self.defense = 1
        self.evasiveness = 0
        self.speed = 1
        self.lootChance = 0

    def getBlock(self):
        low = 50
        for i in range(5):
            r =randint(0, round(self.defense+1))
            if(r < low):
                low = r
        return low

    def getEvade(self):
        return randint(0, round(self.evasiveness+1))

    def getLootChance(self):
        return randint(0, round(self.lootChance+1))

    def getDamage(self):
        return randint((self.damage+1)//2, self.damage+1)
