from random import *
from math import *

class Modifier(object):
    def __init__(self, inPrefix="", inValueBuff=0, inChance=0):
        self.prefix = inPrefix
        self.valueBuff = inValueBuff
        self.chance = inChance
        self.setValueBuff()


    def setValueBuff(self):
        val = abs(self.valueBuff)
        variance = val - (ceil((val*4)/7))
        final = randint(variance, val)
        if(self.valueBuff < 0):
            self.valueBuff = -final
        elif(self.valueBuff > 0):
            self.valueBuff = final



class EquipableModifier(Modifier):
    def __init__(self, prefix, valueBuff=0, chance=0,
                 inWeightBuff=0, inStrBuff=0, inAgiBuff=0, inIntBuff=0):
        super().__init__(prefix, valueBuff, chance)
        self.weightBuff = inWeightBuff
        self.strBuff = inStrBuff
        self.agiBuff = inAgiBuff
        self.intBuff = inIntBuff
        self.setStatBuffs()


    def setStatBuffs(self):
        if(self.strBuff < 0):
            self.strBuff = abs(self.strBuff)
            self.strBuff = randint(ceil((3*self.strBuff)/4), self.strBuff+1)
            self.strBuff = -self.strBuff
        else:
            self.strBuff = randint(ceil((3*self.strBuff)/4), self.strBuff+1)


        if(self.agiBuff < 0):
            self.agiBuff = abs(self.agiBuff)
            self.agiBuff = randint(ceil((3*self.agiBuff)/4), self.agiBuff+1)
            self.agiBuff = -self.agiBuff
        else:
            self.agiBuff = randint(ceil((3*self.agiBuff)/4), self.agiBuff+1)


        if(self.intBuff < 0):
            self.intBuff = abs(self.intBuff)
            self.intBuff = randint(ceil((3*self.intBuff)/4), self.intBuff+1)
            self.intBuff = -self.intBuff
        else:
            self.intBuff = randint(ceil((3*self.intBuff)/4), self.intBuff+1)

        self.weightBuff = round(self.weightBuff + uniform(-self.weightBuff/4, self.weightBuff/4), 1)



class WeaponModifier(EquipableModifier):
    def __init__(self, prefix, valueBuff=0, chance=0, weightBuff=0, strBuff=0, agiBuff=0, intBuff=0,
                inDamageBuff=0, inActionPointCostBuff=0, ):
        super().__init__(prefix, valueBuff, chance, weightBuff, strBuff, agiBuff, intBuff)
        self.damageBuff = inDamageBuff
        self.actionPointCostBuff = inActionPointCostBuff


class ArmorModifier(EquipableModifier):
    def __init__(self, prefix, valueBuff=0, chance=0, weightBuff=0, strBuff=0, agiBuff=0, intBuff=0,
                inDefenseBuff=0, inHealthBuff=0, inActionPointBuff=0, inHealthRegenBuff=0, inActionPointRegenBuff=0):
        super().__init__(prefix, valueBuff, chance, weightBuff, strBuff, agiBuff, intBuff)
        self.defenseBuff = inDefenseBuff
        self.healthBuff = inHealthBuff
        self.actionPointBuff = inActionPointBuff
        self.healthRegenBuff = inHealthRegenBuff
        self.actionPointRegenBuff = inActionPointRegenBuff


class FoodModifier(Modifier):
    def __init__(self, prefix="", valueBuff=0, chance=0,
                 inHealValueBuff=0, inUsesBuff=0, inWeightBuff=0):
        super().__init__(prefix, valueBuff, chance)
        self.healValueBuff = inHealValueBuff
        self.usesBuff = inUsesBuff
        self.weightBuff = round(inWeightBuff + uniform(-inWeightBuff/4, inWeightBuff/4), 1)
