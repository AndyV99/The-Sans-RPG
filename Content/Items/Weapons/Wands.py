from .Weapons import Wand

class OakWand(Wand):
    def __init__(self, name="Oak Wand", value=10, weight=0.5,
                 strBuff=0, agiBuff=0, intBuff=5, damage=2, actionCost=3, scaleValue=1.0, tier=1):
        super().__init__(name, value, weight, strBuff, agiBuff, intBuff, damage, actionCost, scaleValue, tier)
        self.setStats([0, 0, 2])
        self.setDamage(-1, 1)
        self.setWeight(-0.1, 0.2)


class BirchWand(Wand):
    def __init__(self, name="Birch Wand", value=25, weight=0.6,
                 strBuff=0, agiBuff=0, intBuff=7, damage=3, actionCost=3, scaleValue=1.3, tier=2):
        super().__init__(name, value, weight, strBuff, agiBuff, intBuff, damage, actionCost, scaleValue, tier)
        self.setStats([0, 0, 3])
        self.setDamage(-2, 3)
        self.setWeight(-0.2, 0.3)


class DogwoodWand(Wand):
    def __init__(self, name="Dogwood Wand", value=35, weight=0.7,
                 strBuff=0, agiBuff=2, intBuff=6, damage=2, actionCost=2, scaleValue=1.9, tier=3):
        super().__init__(name, value, weight, strBuff, agiBuff, intBuff, damage, actionCost, scaleValue, tier)
        self.setStats([0, 1, 3])
        self.setDamage(-1, 3)
        self.setWeight(-0.2, 0.3)


class HemlockWand(Wand):
    def __init__(self, name="Hemlock Wand", value=45, weight=0.4,
                 strBuff=0, agiBuff=10, intBuff=5, damage=5, actionCost=4, scaleValue=2.5, tier=4):
        super().__init__(name, value, weight, strBuff, agiBuff, intBuff, damage, actionCost, scaleValue, tier)
        self.setStats([0, 5, 3])
        self.setDamage(-1, 3)
        self.setWeight(-0.1, 0.3)


class WalnutWand(Wand):
    def __init__(self, name="Walnut Wand", value=55, weight=1.5,
                 strBuff=0, agiBuff=3, intBuff=7, damage=7, actionCost=7, scaleValue=3.0, tier=5):
        super().__init__(name, value, weight, strBuff, agiBuff, intBuff, damage, actionCost, scaleValue, tier)
        self.setStats([0, 1, 4])
        self.setDamage(-1, 4)
        self.setWeight(-0.1, 0.4)


class SycamoreWand(Wand):
    def __init__(self, name="Sycamore Wand", value=65, weight=1.5,
                 strBuff=2, agiBuff=5, intBuff=10, damage=9, actionCost=7, scaleValue=3.5, tier=6):
        super().__init__(name, value, weight, strBuff, agiBuff, intBuff, damage, actionCost, scaleValue, tier)
        self.setStats([0, 2, 7])
        self.setDamage(-1, 5)
        self.setWeight(-0.2, 0.3)


class ElderWand(Wand):
    def __init__(self, name="Elder Wand", value=75, weight=1,
                 strBuff=3, agiBuff=12, intBuff=15, damage=13, actionCost=10, scaleValue=4.0, tier=7):
        super().__init__(name, value, weight, strBuff, agiBuff, intBuff, damage, actionCost, scaleValue, tier)
        self.setStats([1, 10, 12])
        self.setDamage(-2, 5)
        self.setWeight(-0.5, 0.7)
