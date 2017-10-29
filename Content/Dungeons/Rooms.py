import random
from ..Beings import Enemy
from ..Enemies import Enemies
from ..Items import Tiers
import math

ENEMIES = [Enemies.Rat, Enemies.Bat, Enemies.Spider, Enemies.Goblin,
                     Enemies.Wolf, Enemies.Skeleton, Enemies.Orc, Enemies.Giant, Enemies.Demon]

class Room(object):
    def __init__(self, game, roomLevel=1, enemyLevel=1, numOfEnemies=5):
        self.game = game
        self.level= round(random.uniform(roomLevel-0.2, roomLevel+0.2), 1)
        self.enemyLevel = round(random.uniform(enemyLevel-0.5, enemyLevel+0.5), 1)
        self.numOfEnemies = numOfEnemies
        self.possibleEnemies = []
        self.currentEnemy = 0
        self.enemies = []
        self.possibleLoot = []
        self.loot = []
        self.generateEnemies()
        self.generateLoot()


    def generateEnemies(self):
        for i in range(len(ENEMIES)):
            if(i == int(round(self.level, 0)-1)):
                for j in range(3):
                    self.possibleEnemies.append(ENEMIES[i])
            elif(round(abs(i-(self.level-1))) == 1):
                for j in range(2):
                    self.possibleEnemies.append(ENEMIES[i])
            elif(round(abs(i-(self.level-1))) == 2):
                self.possibleEnemies.append(ENEMIES[i])
            else:
                pass

        for i in range(self.numOfEnemies):
            self.enemies.append(random.choice(self.possibleEnemies)(level=self.enemyLevel))


    def generateLoot(self):
        tiers = []
        for i in range(Tiers.maxTierWep):
            if(i == int(round(self.level, 0)-1)):
                for j in range(3):
                    tiers.append(i)
            elif(round(abs(i-(self.level-1))) == 1):
                for j in range(2):
                    tiers.append(i)
            elif(round(abs(i-(self.level-1))) == 2):
                tiers.append(i)
            else:
                pass


        for p in range(20):
            tierNum = random.choice(tiers)
            r = random.randint(0, 2)
            if(r == 0):
                tier = Tiers.weaponTiers[max(min(Tiers.maxTierWep-1, tierNum), 0)]
                weapon = random.choice(tier)
                self.possibleLoot.append(weapon)
            elif(r == 1):
                tier = Tiers.armorTiers[max(min(Tiers.maxTierArm-1, tierNum), 0)]
                armor = random.choice(tier)
                self.possibleLoot.append(armor)
            else:
                food = random.choice(Tiers.allFood)
                self.possibleLoot.append(food)


    def getPossibleEnemies(self):
        returnArray = []
        for enemyCls in self.possibleEnemies:
            if(not enemyCls.__name__ in returnArray):
                returnArray.append(enemyCls.__name__)
        return returnArray

    def getPossibleLoot(self):
        returnArray = []
        for itemCls in self.possibleLoot:
            if(not itemCls.__name__ in returnArray):
                returnArray.append(itemCls.__name__)
        return returnArray

    def getLoot(self):
        loot = random.choice(self.possibleLoot)()
        loot.generateModifiers(7)
        loot.addModifiers()
        return loot
