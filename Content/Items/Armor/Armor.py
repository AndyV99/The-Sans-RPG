from ..Items import *
from random import *
from math import *

class HeadArmor(Armor):
    def __init__(self, name="Empty Helmet", value=0, weight=0, strBuff=0, agiBuff=0, intBuff=0,
                 defense=0, healthBuff=0, actionPointBuff=0, healthRegenBuff=0, actionPointRegenBuff=0, tier=1):
        super().__init__(name, value, weight, strBuff, agiBuff, intBuff, defense, healthBuff, actionPointBuff, healthRegenBuff, actionPointBuff, tier)


    def getBlock(self):
        return randint(defense-1, defense)


class TorsoArmor(Armor):
    def __init__(self, name="Empty Torso", value=0, weight=0, strBuff=0, agiBuff=0, intBuff=0,
                 defense=0, healthBuff=0, actionPointBuff=0, healthRegenBuff=0, actionPointRegenBuff=0, tier=0):
        super().__init__(name, value, weight, strBuff, agiBuff, intBuff, defense, healthBuff, actionPointBuff, healthRegenBuff, actionPointBuff, tier)
        self.setWeight(-2, 1.5)


    def getBlock(self):
        return randint(defense-2, defense+3)


class LegArmor(Armor):
    def __init__(self, name="Empty Pants", value=0, weight=0, strBuff=0, agiBuff=0, intBuff=0,
                 defense=0, healthBuff=0, actionPointBuff=0, healthRegenBuff=0, actionPointRegenBuff=0, tier=0):
        super().__init__(name, value, weight, strBuff, agiBuff, intBuff, defense, healthBuff, actionPointBuff, healthRegenBuff, actionPointBuff, tier)
        self.setWeight(-0.9, 2)


    def getBlock(self):
        return randint(defense-1, defense+1)
