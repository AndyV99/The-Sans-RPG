from ..Modifiers import WeaponModifiers, ArmorModifiers, FoodModifiers
from ..Beings import *
from random import *
from .. import ArtHandler

class Item(object):
    def __init__(self, inName="Item", inValue=0, inWeight=0.0):
        self.name = inName
        self.value = inValue
        self.weight = round(inWeight, 1)
        self.stackable = False
        self.image = eval("ArtHandler.{}".format(self.__class__.__name__))
        if(issubclass(self.__class__, Food)):
            self.stackable = True


class Equipable(Item):
    def __init__(self, name="", value=0, weight=0.0,
                inStrBuff=0, inAgiBuff=0, inIntBuff=0, tier=1):
        super().__init__(name, value, weight)
        self.tier = tier
        self.strBuff = inStrBuff
        self.agiBuff = inAgiBuff
        self.intBuff = inIntBuff
        self.equipModifiers = []


    #called in each equipable's initializer
    def setStats(self, lowers=[0, 0, 0]):
        if(self.strBuff>lowers[0]):
            self.strBuff = randint(lowers[0], self.strBuff)
        if(self.agiBuff>lowers[1]):
            self.agiBuff = randint(lowers[1], self.agiBuff)
        if(self.intBuff>lowers[2]):
            self.intBuff = randint(lowers[2], self.intBuff)


    #called in each equipable's initializer
    def setWeight(self, minVar=-0.5, maxVar=0.5):
        self.weight = round(self.weight + round(uniform(minVar, maxVar), 1), 1)


    def generateModifiers(self, chances=1):
        pass


    def addModifiers(self):
        pass


class Weapon(Equipable):
    def __init__(self, name="", value=0, weight=0.0, strBuff=0, agiBuff=0, intBuff=0,
                inDamage=1, inActionCost=0, inScaleValue=0, tier=1):
        super().__init__(name, value, weight, strBuff, agiBuff, intBuff, tier)
        self.damage = inDamage
        self.actionPointCost = inActionCost
        self.scaleValue = inScaleValue
        if(name != "Fist"):
            self.setScaleValue()
            self.generateModifiers()
            self.addModifiers()


    def generateModifiers(self, chances=1):
        self.equipModifiers=[]
        for i in range(chances):
            mod = choice(WeaponModifiers.WEAPON_MODIFIERS)
            val = randint(0, 200)
            if(val <= mod.chance):
                self.equipModifiers.append(mod)


    def addModifiers(self):
        for mod in self.equipModifiers:
            self.name = "{} {}".format(mod.prefix, self.name)
            self.value += mod.valueBuff
            self.weight += mod.weightBuff
            self.strBuff += mod.strBuff
            self.agiBuff += mod.agiBuff
            self.intBuff += mod.intBuff
            self.damage += mod.damageBuff
            self.actionPointCost += mod.actionPointCostBuff
        self.value = max(0, self.value)
        self.actionPointCost = max(1, self.actionPointCost)
        self.damage = max(0, self.damage)


    def setScaleValue(self):
        self.scaleValue = round(self.scaleValue + uniform(-1/(4*self.scaleValue), 1/(4*self.scaleValue)), 1)


    def setDamage(self, minVar=-1, maxVar=1):
        self.damage = self.damage + randint(minVar, maxVar)


    def getDamage(self, Player):
        return self.damage + randint(0, Player.strength//2)

    def getDamageForLabel(self, Player):
        return "{} + 0 to {}".format(self.damage, self.damage + Player.strength//2)


class Armor(Equipable):
    def __init__(self, name="", value=0, weight=0.0, strBuff=0, agiBuff=0, intBuff=0,
                inDefense=0, inHealthBuff=0, inActionPointBuff=0, inHealthRegenBuff=0, inActionPointRegenBuff=0, tier=1):
        super().__init__(name, value, weight, strBuff, agiBuff, intBuff, tier)
        self.defense = inDefense
        self.healthBuff = inHealthBuff
        self.actionPointBuff = inActionPointBuff
        self.healthRegenBuff = inHealthRegenBuff
        self.actionPointRegenBuff = inActionPointRegenBuff


    def generateModifiers(self, chances=1):
        self.equipModifiers=[]
        for i in range(chances):
            mod = choice(ArmorModifiers.ARMOR_MODIFIERS)
            val = randint(0, 200)
            if(val <= mod.chance):
                self.equipModifiers.append(mod)


    def addModifiers(self):
        for mod in self.equipModifiers:
            self.name = "{} {}".format(mod.prefix, self.name)
            self.value += mod.valueBuff
            self.weight += mod.weightBuff
            self.strBuff += mod.strBuff
            self.agiBuff += mod.agiBuff
            self.intBuff += mod.intBuff
            self.defense += mod.defenseBuff
            self.healthBuff += mod.healthBuff
            self.actionPointBuff += mod.actionPointBuff
            self.healthRegenBuff += mod.healthRegenBuff
            self.actionPointRegenBuff += mod.actionPointRegenBuff
        self.value = max(0, self.value)


    def getBlock(self):
        return randint(defense-3, defense+1)


class Food(Item):
    def __init__(self, name="", value=0, weight=0.0,
                 inHealValue=0, inUsesLeft=0):
        super().__init__(name, value, weight)
        self.healValue = inHealValue
        self.totalUses = inUsesLeft
        self.usesLeft = self.totalUses
        self.foodModifiers = []
        self.generateModifiers()
        self.addModifiers()


    def generateModifiers(self, chances=1):
        self.foodModifiers = []
        for i in range(chances):
            mod = choice(FoodModifiers.FOOD_MODIFIERS)
            val = randint(0, 150)
            if(val <= mod.chance):
                self.foodModifiers.append(mod)


    def addModifiers(self):
        for mod in self.foodModifiers:
            self.name = "{} {}".format(mod.prefix, self.name)
            self.healValue += mod.healValueBuff
            self.totalUses += mod.usesBuff
            self.usesLeft += mod.usesBuff
            self.weight += mod.weightBuff
            self.value += mod.valueBuff
        self.usesLeft = max(1, self.usesLeft)
        self.weight = max(0.1, self.weight)
        self.value = max(0, self.value)
