from ..Items import *
from random import *
from ...Beings import *
from math import *


class Hammer(Weapon):
    def __init__(self, name="", value=0, weight=0.0,
                 strBuff=0, agiBuff=0, intBuff=0, damage=0, actionCost=0, scaleValue=0, tier=1):
        super().__init__(name, value, weight, strBuff, agiBuff, intBuff, damage, actionCost, scaleValue, tier)


    def getDamage(self, Player):
        variance = randint(0, Player.strength//2)
        scaling = ceil(self.scaleValue*Player.strength)
        return int(scaling + variance + self.damage)


    def getDamageForLabel(self, Player):
        scaling = ceil(self.scaleValue*Player.strength)
        dmg = self.damage+scaling
        if(Player.strength//2==0):
            return "{}".format(dmg)
        else:
            return "{} to {}".format(dmg, dmg+Player.strength//2)


class Sword(Weapon):
    def __init__(self, name="", value=0, weight=0.0,
                 strBuff=0, agiBuff=0, intBuff=0, damage=0, actionCost=0, scaleValue=0, tier=0):
        super().__init__(name, value, weight, strBuff, agiBuff, intBuff, damage, actionCost, scaleValue, tier)


    def getDamage(self, Player):
        variance = randint(0, Player.strength//2)
        scaling = (ceil(self.scaleValue*Player.strength*0.6))+(ceil(self.scaleValue*Player.agility*0.4))
        return int(scaling + variance + self.damage)

    def getDamageForLabel(self, Player):
        scaling = ceil(self.scaleValue*Player.strength*0.6)+ceil(self.scaleValue*Player.agility*0.4)
        dmg = self.damage+scaling
        if(Player.strength//2==0):
            return "{}".format(dmg)
        else:
            return "{} to {}".format(dmg, dmg+Player.strength//2)


class Bow(Weapon):
    def __init__(self, name="", value=0, weight=0.0,
                 strBuff=0, agiBuff=0, intBuff=0, damage=0, actionCost=0, scaleValue=0, tier=0):
        super().__init__(name, value, weight, strBuff, agiBuff, intBuff, damage, actionCost, scaleValue, tier)


    def getDamage(self, Player):
        variance = randint(0, Player.agility//2)
        scaling = ceil(self.scaleValue*Player.agility)
        return int(scaling + variance + self.damage)


    def getDamageForLabel(self, Player):
        scaling = ceil(self.scaleValue*Player.agility)
        dmg = self.damage + scaling
        if(Player.agility//2==0):
            return "{}".format(dmg)
        else:
            return "{} to {}".format(dmg, dmg+Player.agility//2)


class Dagger(Weapon):
    def __init__(self, name="", value=0, weight=0.0,
                 strBuff=0, agiBuff=0, intBuff=0, damage=0, actionCost=0, scaleValue=0, tier=0):
        super().__init__(name, value, weight, strBuff, agiBuff, intBuff, damage, actionCost, scaleValue, tier)


    def getDamage(self, Player):
        variance = randint(0, Player.agility//2)
        scaling = ceil((self.scaleValue*Player.agility*.8) + (self.scaleValue*Player.intelligence*.2))
        return int(scaling + variance + self.damage)

    def getDamageForLabel(self, Player):
        scaling = ceil((self.scaleValue*Player.agility*.8) + (self.scaleValue*Player.intelligence*.2))
        dmg = self.damage+scaling
        if(Player.agility//2==0):
            return "{}".format(dmg)
        else:
            return "{} to {}".format(dmg, dmg+Player.agility//2)



class Wand(Weapon):
    def __init__(self, name="", value=0, weight=0.0,
                 strBuff=0, agiBuff=0, intBuff=0, damage=0, actionCost=0, scaleValue=0, tier=0):
        super().__init__(name, value, weight, strBuff, agiBuff, intBuff, damage, actionCost, scaleValue, tier)


    def getDamage(self, Player):
        variance = randint(0, Player.intelligence//2)
        scaling = ceil((self.scaleValue*Player.intelligence*.9) + (self.scaleValue*Player.agility*.1))
        return int(scaling + variance + self.damage)

    def getDamageForLabel(self, Player):
        scaling = ceil((self.scaleValue*Player.intelligence*.9) + (self.scaleValue*Player.agility*.1))
        dmg = self.damage + scaling
        if(Player.intelligence//2==0):
            return "{}".format(dmg)
        else:
            return "{} to {}".format(dmg, dmg+Player.intelligence//2)


class Staff(Weapon):
    def __init__(self, name="", value=0, weight=0.0,
                 strBuff=0, agiBuff=0, intBuff=0, damage=0, actionCost=0, scaleValue=0, tier=0):
        super().__init__(name, value, weight, strBuff, agiBuff, intBuff, damage, actionCost, scaleValue, tier)


    def getDamage(self, Player):
        variance = randint(0, Player.intelligence//2)
        scaling = ceil(self.scaleValue*Player.intelligence)
        return int(scaling + variance + self.damage)

    def getDamageForLabel(self, Player):
        scaling = ceil(self.scaleValue*Player.intelligence)
        dmg = self.damage + scaling
        if(Player.intelligence//2==0):
            return "{}".format(dmg)
        else:
            return "{} to {}".format(dmg, dmg+Player.intelligence//2)


class BattleStaff(Weapon):
    def __init__(self, name="", value=0, weight=0.0,
                 strBuff=0, agiBuff=0, intBuff=0, damage=0, actionCost=0, scaleValue=0, tier=0):
        super().__init__(name, value, weight, strBuff, agiBuff, intBuff, damage, actionCost, scaleValue, tier)


    def getDamage(self, Player):
        variance = randint(0, Player.intelligence//2)
        scaling = ceil((self.scaleValue*Player.intelligence*.6) + (self.scaleValue*Player.strength*.4))
        return int(scaling + variance + self.damage)

    def getDamageForLabel(self, Player):
        scaling = ceil((self.scaleValue*Player.intelligence*.6) + (self.scaleValue*Player.strength*.4))
        dmg = self.damage + scaling
        if(Player.strength//2==0):
            return "{}".format(dmg)
        else:
            return "{} to {}".format(dmg, dmg+Player.strength//2)
