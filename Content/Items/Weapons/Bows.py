from .Weapons import Bow

class OakBow(Bow):
    def __init__(self, name="Oak Bow", value=10, weight=1,
                 strBuff=0, agiBuff=3, intBuff=0, damage=2, actionCost=1, scaleValue=0.2, tier=1):
        super().__init__(name, value, weight, strBuff, agiBuff, intBuff, damage, actionCost, scaleValue, tier)
        self.setStats([0, 1, 0])
        self.setDamage(0, 2)
        self.setWeight(-0.2, 0.5)


class WillowBow(Bow):
    def __init__(self, name="Willow Bow", value=20, weight=4,
                 strBuff=1, agiBuff=4, intBuff=0, damage=5, actionCost=2, scaleValue=0.3, tier=2):
        super().__init__(name, value, weight, strBuff, agiBuff, intBuff, damage, actionCost, scaleValue, tier)
        self.setStats([0, 1, 0])
        self.setDamage(0, 1)
        self.setWeight(-0.4, 0.4)


class MapleBow(Bow):
    def __init__(self, name="Maple Bow", value=25, weight=5,
                 strBuff=2, agiBuff=7, intBuff=2, damage=9, actionCost=4, scaleValue=0.4, tier=4):
        super().__init__(name, value, weight, strBuff, agiBuff, intBuff, damage, actionCost, scaleValue, tier)
        self.setStats([0, 3, 0])
        self.setDamage(-1, 2)
        self.setWeight(-0.4, 0.4)


class YewBow(Bow):
    def __init__(self, name="Yew Bow", value=30, weight=9,
                 strBuff=1, agiBuff=10, intBuff=2, damage=14, actionCost=5, scaleValue=0.7, tier=5):
        super().__init__(name, value, weight, strBuff, agiBuff, intBuff, damage, actionCost, scaleValue, tier)
        self.setStats([1, 8, 1])
        self.setDamage(0, 5)
        self.setWeight(-0.3, 0.5)


class MagicBow(Bow):
    def __init__(self, name="Magic Bow", value=40, weight=2,
                 strBuff=4, agiBuff=20, intBuff=10, damage=20, actionCost=7, scaleValue=1.0, tier=6):
        super().__init__(name, value, weight, strBuff, agiBuff, intBuff, damage, actionCost, scaleValue, tier)
        self.setStats([1, 15, 6])
        self.setDamage(-2, 8)
        self.setWeight(-0.4, 0.4)
