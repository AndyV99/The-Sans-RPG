from .Weapons import Hammer


class WoodenHammer(Hammer):
    def __init__(self, name="Wooden Hammer", value=10, weight=5,
                 strBuff=2, agiBuff=0, intBuff=0, damage=3, actionCost=2, scaleValue=0.4, tier=1):
        super().__init__(name, value, weight, strBuff, agiBuff, intBuff, damage, actionCost, scaleValue, tier)
        self.setStats([0, 0, 0])
        self.setDamage(-1, 2)
        self.setWeight(-0.2, 0.3)


class StoneHammer(Hammer):
    def __init__(self, name="Stone Hammer", value=25, weight=7,
                 strBuff=4, agiBuff=0, intBuff=0, damage=6, actionCost=4, scaleValue=0.6, tier=2):
        super().__init__(name, value, weight, strBuff, agiBuff, intBuff, damage, actionCost, scaleValue, tier)
        self.setStats([1, 0, 0])
        self.setDamage(-1, 3)
        self.setWeight(-0.6, 0.2)


class BronzeHammer(Hammer):
    def __init__(self, name="Bronze Hammer", value=35, weight=10,
                 strBuff=7, agiBuff=2, intBuff=0, damage=9, actionCost=8, scaleValue=0.8, tier=3):
        super().__init__(name, value, weight, strBuff, agiBuff, intBuff, damage, actionCost, scaleValue, tier)
        self.setStats([2, 1, 0])
        self.setDamage(-2, 4)
        self.setWeight(-0.4, 0.3)


class SteelHammer(Hammer):
    def __init__(self, name="Steel Hammer", value=45, weight=15,
                 strBuff=12, agiBuff=2, intBuff=3, damage=17, actionCost=10, scaleValue=1.2, tier=4):
        super().__init__(name, value, weight, strBuff, agiBuff, intBuff, damage, actionCost, scaleValue, tier)
        self.setStats([5, 0, 1])
        self.setDamage(-2, 2)
        self.setWeight(-1, 1)


class PlatinumHammer(Hammer):
    def __init__(self, name="Platinum Hammer", value=55, weight=20,
                 strBuff=14, agiBuff=2, intBuff=0, damage=20, actionCost=12, scaleValue=1.5, tier=5):
        super().__init__(name, value, weight, strBuff, agiBuff, intBuff, damage, actionCost, scaleValue, tier)
        self.setStats([7, 0, 0])
        self.setDamage(-1, 3)
        self.setWeight(-0.5, 1.5)


class AdamantineHammer(Hammer):
    def __init__(self, name="Adamantine Hammer", value=65, weight=23,
                 strBuff=16, agiBuff=5, intBuff=2, damage=26, actionCost=14, scaleValue=1.9, tier=6):
        super().__init__(name, value, weight, strBuff, agiBuff, intBuff, damage, actionCost, scaleValue, tier)
        self.setStats([8, 2, 0])
        self.setDamage(0, 3)
        self.setWeight(-0.9, 0.5)


class VibraniumHammer(Hammer):
    def __init__(self, name="Vibranium Hammer", value=75, weight=28,
                 strBuff=20, agiBuff=6, intBuff=4, damage=30, actionCost=15, scaleValue=2.2, tier=7):
        super().__init__(name, value, weight, strBuff, agiBuff, intBuff, damage, actionCost, scaleValue, tier)
        self.setStats([10, 2, 2])
        self.setDamage(-4, 4)
        self.setWeight(-2, 2)
