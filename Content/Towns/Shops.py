from ..Items import Items, Food, Armor, Weapons, Inventory, Tiers
import random
import math


class Shop(object):
    def __init__(self, level, game):
        self.level = level
        self.game = game
        self.x1 = 0
        self.y1 = 0
        self.x2 = 0
        self.y2 = 0
        self.color='white'

    def setRectangle(self, rect=[0, 0, 0, 0]):
        self.x1 = rect[0]
        self.y1 = rect[1]
        self.x2 = self.x1 + rect[2]
        self.y2 = self.y1 + rect[3]


SHOP_KEEPER_NAMES = ["Ricky", "Bob", "Jim", "Stan", "Phil", "Carl", "Gerald", "Steve", "Nalgene", "Armene", "Angille", "Onillo",
                     "Barry", "Andy", "Ponti", "Figore", "Dellos", "Viro", "Quislo", "Kanopi", "Yinmo", "Zarro", "Nagor", "Matt",
                     "Micheal", "Westo", "Horti", "Amnopi", "Xynoris", "Terammos", "Garrett", "Colin", "Robert", "Dvoni", "Fommick",
                     "Kilnor", "Pieorro", "Unolsho", "Chortus", "Uunaris", "Na\'ar", "Ga\'rron", "Opo\'nor"]

def resetKeeperNames():
    global SHOP_KEEPER_NAMES
    SHOP_KEEPER_NAMES = ["Ricky", "Bob", "Jim", "Stan", "Phil", "Carl", "Gerald", "Steve", "Nalgene", "Armene", "Angille", "Onillo",
                         "Barry", "Andy", "Ponti", "Figore", "Dellos", "Viro", "Quislo", "Kanopi", "Yinmo", "Zarro", "Nagor", "Matt",
                         "Micheal", "Westo", "Horti", "Amnopi", "Xynoris", "Terammos", "Garrett", "Colin", "Robert", "Dvoni", "Fommick",
                         "Kilnor", "Pieorro", "Unolsho", "Chortus", "Uunaris", "Na\'ar", "Ga\'rron", "Opo\'nor"]

#--------------------------------------------------------------------

class Store(Shop):
    def __init__(self, level=1.0, game=0, shopType=""):
        super().__init__(level, game)
        keeperName = random.choice(SHOP_KEEPER_NAMES)
        SHOP_KEEPER_NAMES.remove(keeperName)
        self.vendorName= keeperName
        self.shopName = "{}\'s {}".format(self.vendorName, shopType)
        self.inventory = Inventory.Inventory()
        self.money = int(level*10)
        self.money += random.randint(0, self.money)
        self.color = ''


    def generateInventory(self):
        pass


    def sellToPlayer(self, item, amount=1):
        if(self.game.player.money >= item.value*amount):
            self.game.player.money -= item.value*amount
            self.game.player.inventory.addItem(item, amount)
            self.inventory.removeItem(item, amount)
            self.money += item.value*amount
            return "You bought {}x{} for {} gold.".format(item.name, amount, item.value*amount)
        else:
            return "You don't have enough money."


    def buyFromPlayer(self, item, amount=1):
        if(self.money >= (amount*item.value)//2):
            self.game.player.money += amount*item.value//2
            self.game.player.inventory.removeItem(item, amount)
            self.inventory.addItem(item, amount)
            self.money -= amount*item.value//2
            return "You sold {}x{} for {} gold.".format(item.name, amount, (amount*(item.value)//2))
        else:
            return "{} doesn't have enough money.".format(self.vendorName)


class GeneralStore(Store):
    def __init__(self, level=1.0, game=0, shopType="General Store"):
        super().__init__(level, game, shopType)
        self.generateInventory()

    def generateInventory(self):
        low = 12
        for i in range(3):
            items = random.randint(6, 12)
            if(items < low):
                low = items
        for p in range(low):
            tierNum = random.choice(getTierDistribution(self.level))
            r = random.randint(0, 2)
            if(r == 0):
                tier = Tiers.weaponTiers[min(Tiers.maxTierWep, tierNum)]
                weapon = random.choice(tier)
                self.inventory.addItem(weapon())
            elif(r == 1):
                tier = Tiers.armorTiers[min(Tiers.maxTierArm, tierNum)]
                armor = random.choice(tier)
                self.inventory.addItem(armor())
            else:
                food = random.choice(Tiers.allFood)
                self.inventory.addItem(food(), random.randint(3, 12))


class Market(Store):
    def __init__(self, level=1.0, game=0, shopType="Market"):
        super().__init__(level, game, shopType)
        self.generateInventory()


    def generateInventory(self):
        items = random.randint(3, 9)
        for i in range(0, items):
            item = random.choice(Tiers.allFood)
            food = item()
            food.generateModifiers(5)
            food.addModifiers()
            self.inventory.addItem(food, random.randint(3, 12))


class WeaponShop(Store):
    def __init__(self, level=1.0, game=0, shopType="Weapon Shop"):
        super().__init__(level, game, shopType)
        self.generateInventory()


    def generateInventory(self):
        items = random.randint(3, 8)
        for i in range(items):
            tierNum = random.choice(getTierDistribution(self.level))
            tier = Tiers.weaponTiers[min(Tiers.maxTierWep, tierNum)]
            weapon = random.choice(tier)()
            weapon.generateModifiers(3)
            weapon.addModifiers()
            self.inventory.addItem(weapon)


class ArmorShop(Store):
    def __init__(self, level=1.0, game=0, shopType="Armor Shop"):
        super().__init__(level, game, shopType)
        self.generateInventory()


    def generateInventory(self):
        items = random.randint(3, 8)
        for i in range(items):
            tierNum = random.choice(getTierDistribution(self.level))
            tier = Tiers.armorTiers[min(Tiers.maxTierArm, tierNum)]
            armor = random.choice(tier)()
            armor.generateModifiers(3)
            armor.addModifiers()
            self.inventory.addItem(armor)


def getTierDistribution(level):
    tiers = []
    for i in range(Tiers.maxTierWep):
        if(i == int(round(level, 0)-1)):
            for j in range(3):
                tiers.append(i)
        elif(round(abs(i-(level-1))) == 1):
            for j in range(1):
                tiers.append(i)
        elif(round(abs(i-(level-1))) == 2):
            tiers.append(i)
        else:
            pass
    return tiers

#-------------------------------------------------------------------

class Service(Shop):
    def __init__(self, level=1.0, game=0):
        super().__init__(level, game)
        keeperName = random.choice(SHOP_KEEPER_NAMES)
        SHOP_KEEPER_NAMES.remove(keeperName)
        self.vendorName= keeperName

    def serve(self):
        pass


class Inn(Service):
    def __init__(self, level=1.0, game=0):
        super().__init__(level, game)
        self.shopName = "{}\'s Inn".format(self.vendorName)
        self.cost = int(level*15)


    def serve(self):
        self.game.player.money -= self.cost
        self.game.player.currentActionPoints = self.game.player.totalActionPoints
        self.game.player.currentHealth = self.game.player.totalHealth


class Healer(Service):
    def __init__(self, level=1.0, game=0):
        super().__init__(level, game)
        self.shopName = "{} the healer".format(self.vendorName)
        self.pointsToHeal = 0
        self.totalCost = 0
        self.cost = int(level)
        self.setPointsToHeal()

    def setPointsToHeal(self):
        self.pointsToHeal = self.game.player.totalHealth - self.game.player.currentHealth
        if(self.pointsToHeal*self.cost > self.game.player.money):
            self.pointsToHeal = self.game.player.money//self.cost

    def setTotalCost(self):
        self.totalCost = self.pointsToHeal * self.cost

    def updateValues(self):
        self.setPointsToHeal()
        self.setTotalCost()

    def serve(self):
        self.game.player.money -= self.pointsToHeal*self.cost
        self.game.player.currentHealth += self.pointsToHeal
        return "You healed {} health for {} gold.".format(self.pointsToHeal, self.pointsToHeal*self.cost)


class Blacksmith(Service):
    def __init__(self, level=1.0, game=0):
        super().__init__(level, game)
        self.shopName = "{} the blacksmith".format(self.vendorName)
        self.cost = int(level*12)
        self.slot = Inventory.Inventory(1)
        self.chances = 1

    def serve(self):
        self.game.player.money -= self.cost*self.chances
        initItem = self.slot.slots[0].item.name
        self.slot.slots[0].item.generateModifiers(self.chances)
        self.slot.slots[0].item.addModifiers()
        finalItem = self.slot.slots[0].item.name
        return "Your {} is now a {}".format(initItem, finalItem)

#------------------------------------------------------------------

class Challenge(Shop):
    def __init__(self, level=1.0, game=0):
        super().__init__(level, game)
        self.scale = self.level/2

    def doChallenge(self):
        pass


class Arena(Challenge):
    def __init__(self, level=1.0, game=0):
        super().__init__(level, game)
        self.shopName = "Arena"

    def doChallenge(self):
        endScale = self.scale + random.uniform(-0.4, 0.5)
        moneyGive = int(endScale*self.game.player.strength)
        self.game.player.money += moneyGive

        endScale = self.scale + random.uniform(-0.4, 0.5)
        xpGive = int(endScale*self.game.player.strength)
        self.game.addXPToPlayer(xpGive)

        endScale = self.scale + random.uniform(-0.5, 0.5)
        healthCost = int(max(min(endScale*(self.game.player.totalHealth/3), self.game.player.totalHealth-10), 1))
        self.game.player.currentHealth -= healthCost

        endScale = self.scale + random.uniform(-0.5, 0.5)
        apCost = int(max(min(endScale*(self.game.player.totalActionPoints/3), self.game.player.totalActionPoints-10), 1))
        self.game.player.currentActionPoints -= apCost
        return [moneyGive, xpGive, healthCost, apCost]


class ArcheryRange(Challenge):
    def __init__(self, level=1.0, game=0):
        super().__init__(level, game)
        self.shopName = "Archery Range"


    def doChallenge(self):
        endScale = self.scale + random.uniform(-0.5, 0.5)
        moneyGive = int(endScale*self.game.player.agility)
        self.game.player.money += moneyGive

        endScale = self.scale + random.uniform(-0.5, 0.5)
        xpGive = int(endScale*self.game.player.agility)
        self.game.addXPToPlayer(xpGive)

        apCost = int(max(min(endScale*(self.game.player.totalActionPoints/2), self.game.player.totalActionPoints-10), 1))
        self.game.player.currentActionPoints -= apCost
        return [moneyGive, xpGive, 0, apCost]


class Library(Challenge):
    def __init__(self, level=1.0, game=0):
        super().__init__(level, game)
        self.shopName = "Library"

    def doChallenge(self):
        endScale = self.scale + random.uniform(-0.5, 0.5)
        moneyGive = int(endScale*self.game.player.intelligence)
        self.game.player.money += moneyGive

        endScale = self.scale + random.uniform(-0.5, 0.5)
        xpGive = int(endScale*self.game.player.intelligence)
        self.game.addXPToPlayer(xpGive)

        apCost = int(max(min(endScale*(self.game.player.totalActionPoints/2), self.game.player.totalActionPoints-10), 1))
        self.game.player.currentActionPoints -= apCost
        return [moneyGive, xpGive, 0, apCost]
