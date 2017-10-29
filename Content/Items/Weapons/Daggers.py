from .Weapons import Dagger

class WoodenDagger(Dagger):
    def __init__(self, name="Wooden Dagger", value=10, weight=1,
                 strBuff=0, agiBuff=1, intBuff=1, damage=3, actionCost=1, scaleValue=0.8, tier=1):
        super().__init__(name, value, weight, strBuff, agiBuff, intBuff, damage, actionCost, scaleValue, tier)
        self.setStats([0, 0, 0])
        self.setDamage(-1, 1)
        self.setWeight(-0.3, 0.3)


class StoneDagger(Dagger):
    def __init__(self, name="Stone Dagger", value=25, weight=1,
                 strBuff=0, agiBuff=3, intBuff=2, damage=3, actionCost=1, scaleValue=1.3, tier=2):
        super().__init__(name, value, weight, strBuff, agiBuff, intBuff, damage, actionCost, scaleValue, tier)
        self.setStats([0, 1, 0])
        self.setDamage(-1, 1)
        self.setWeight(-0.5, 0.5)


class BronzeDagger(Dagger):
    def __init__(self, name="Bronze Dagger", value=35, weight=2,
                 strBuff=0, agiBuff=4, intBuff=2, damage=4, actionCost=2, scaleValue=1.6, tier=3):
        super().__init__(name, value, weight, strBuff, agiBuff, intBuff, damage, actionCost, scaleValue, tier)
        self.setStats([0, 1, 1])
        self.setDamage(0, 2)
        self.setWeight(-0.5, 0.5)


class SteelDagger(Dagger):
    def __init__(self, name="Steel Dagger", value=45, weight=3,
                 strBuff=0, agiBuff=6, intBuff=4, damage=5, actionCost=3, scaleValue=2.0, tier=4):
        super().__init__(name, value, weight, strBuff, agiBuff, intBuff, damage, actionCost, scaleValue, tier)
        self.setStats([0, 3, 1])
        self.setDamage(-1, 4)
        self.setWeight(-0.1, 0.9)


class PlatinumDagger(Dagger):
    def __init__(self, name="Platinum Dagger", value=55, weight=5,
                 strBuff=1, agiBuff=7, intBuff=5, damage=5, actionCost=4, scaleValue=2.3, tier=5):
        super().__init__(name, value, weight, strBuff, agiBuff, intBuff, damage, actionCost, scaleValue, tier)
        self.setStats([0, 5, 3])
        self.setDamage(-2, 3)
        self.setWeight(-0.2, 0.2)


class AdamantineDagger(Dagger):
    def __init__(self, name="Adamantine Dagger", value=65, weight=5,
                 strBuff=1, agiBuff=8, intBuff=5, damage=5, actionCost=3, scaleValue=2.6, tier=6):
        super().__init__(name, value, weight, strBuff, agiBuff, intBuff, damage, actionCost, scaleValue, tier)
        self.setStats([0, 6, 4])
        self.setDamage(-1, 1)
        self.setWeight(-1.1, 1.5)


class VibraniumDagger(Dagger):
    def __init__(self, name="Vibranium Dagger", value=75, weight=6,
                 strBuff=2, agiBuff=12, intBuff=7, damage=7, actionCost=4, scaleValue=3.0, tier=7):
        super().__init__(name, value, weight, strBuff, agiBuff, intBuff, damage, actionCost, scaleValue, tier)
        self.setStats([0, 10, 6])
        self.setDamage(0, 3)
        self.setWeight(-4, 2)
