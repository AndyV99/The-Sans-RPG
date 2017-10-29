from .Weapons import Sword

class WoodenSword(Sword):
    def __init__(self, name="Wooden Sword", value=10, weight=2,
                 strBuff=1, agiBuff=1, intBuff=0, damage=2, actionCost=1, scaleValue=0.5, tier=1):
        super().__init__(name, value, weight, strBuff, agiBuff, intBuff, damage, actionCost, scaleValue, tier)
        self.setStats([0, 0, 0])
        self.setDamage(0, 1)
        self.setWeight(-0.2, 0.5)


class StoneSword(Sword):
    def __init__(self, name="Stone Sword", value=20, weight=3,
                 strBuff=2, agiBuff=2, intBuff=1, damage=5, actionCost=3, scaleValue=0.7, tier=2):
        super().__init__(name, value, weight, strBuff, agiBuff, intBuff, damage, actionCost, scaleValue, tier)
        self.setStats([1, 0, 0])
        self.setDamage(-1, 1)
        self.setWeight(-0.5, 0.5)


class BronzeSword(Sword):
    def __init__(self, name="Bronze Sword", value=25, weight=5,
                 strBuff=3, agiBuff=2, intBuff=0, damage=7, actionCost=3, scaleValue=0.8, tier=3):
        super().__init__(name, value, weight, strBuff, agiBuff, intBuff, damage, actionCost, scaleValue, tier)
        self.setStats([1, 0, 0])
        self.setDamage(0, 2)
        self.setWeight(-0.9, 0.2)


class SteelSword(Sword):
    def __init__(self, name="Steel Sword", value=35, weight=9,
                 strBuff=5, agiBuff=2, intBuff=2, damage=10, actionCost=4, scaleValue=1.1, tier=4):
        super().__init__(name, value, weight, strBuff, agiBuff, intBuff, damage, actionCost, scaleValue, tier)
        self.setStats([2, 1, 0])
        self.setDamage(-1, 3)
        self.setWeight(-0.2, 0.8)


class PlatinumSword(Sword):
    def __init__(self, name="Platinum Sword", value=45, weight=14,
                 strBuff=9, agiBuff=3, intBuff=0, damage=18, actionCost=5, scaleValue=1.5, tier=5):
        super().__init__(name, value, weight, strBuff, agiBuff, intBuff, damage, actionCost, scaleValue, tier)
        self.setStats([4, 1, 0])
        self.setDamage(-1, 3)
        self.setWeight(-1, 1)


class AdamantineSword(Sword):
    def __init__(self, name="Adamantine Sword", value=55, weight=17,
                 strBuff=11, agiBuff=4, intBuff=0, damage=23, actionCost=8, scaleValue=1.9, tier=6):
        super().__init__(name, value, weight, strBuff, agiBuff, intBuff, damage, actionCost, scaleValue, tier)
        self.setStats([5, 2, 0])
        self.setDamage(-2, 2)
        self.setWeight(-1.1, 1.5)


class VibraniumSword(Sword):
    def __init__(self, name="Vibranium Sword", value=65, weight=19,
                 strBuff=15, agiBuff=9, intBuff=0, damage=28, actionCost=10, scaleValue=2.0, tier=7):
        super().__init__(name, value, weight, strBuff, agiBuff, intBuff, damage, actionCost, scaleValue, tier)
        self.setStats([7, 6, 0])
        self.setDamage(-2, 2)
        self.setWeight(-1, 1)
