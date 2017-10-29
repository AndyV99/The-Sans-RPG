from .Weapons import BattleStaff

class OakBattleStaff(BattleStaff):
    def __init__(self, name="Oak Battle Staff", value=10, weight=5,
                 strBuff=3, agiBuff=0, intBuff=3, damage=3, actionCost=2, scaleValue=0.8, tier=1):
        super().__init__(name, value, weight, strBuff, agiBuff, intBuff, damage, actionCost, scaleValue, tier)
        self.setStats([1, 0, 1])
        self.setDamage(-1, 1)
        self.setWeight(-0.5, 0.5)


class BirchBattleStaff(BattleStaff):
    def __init__(self, name="Birch Battle Staff", value=25, weight=6,
                 strBuff=4, agiBuff=0, intBuff=6, damage=5, actionCost=3, scaleValue=1.3, tier=2):
        super().__init__(name, value, weight, strBuff, agiBuff, intBuff, damage, actionCost, scaleValue, tier)
        self.setStats([1, 0, 3])
        self.setDamage(-1, 3)
        self.setWeight(-0.5, 0.5)


class DogwoodBattleStaff(BattleStaff):
    def __init__(self, name="Dogwood Battle Staff", value=35, weight=5,
                 strBuff=3, agiBuff=0, intBuff=8, damage=6, actionCost=3, scaleValue=1.6, tier=3):
        super().__init__(name, value, weight, strBuff, agiBuff, intBuff, damage, actionCost, scaleValue, tier)
        self.setStats([1, 0, 5])
        self.setDamage(-1, 3)
        self.setWeight(-0.6, 0.6)


class HemlockBattleStaff(BattleStaff):
    def __init__(self, name="Hemlock BattleStaff", value=45, weight=8,
                 strBuff=6, agiBuff=5, intBuff=10, damage=9, actionCost=5, scaleValue=2.0, tier=4):
        super().__init__(name, value, weight, strBuff, agiBuff, intBuff, damage, actionCost, scaleValue, tier)
        self.setStats([3, 2, 6])
        self.setDamage(-1, 4)
        self.setWeight(-0.5, 0.9)


class WalnutBattleStaff(BattleStaff):
    def __init__(self, name="Walnut Battle Staff", value=55, weight=9,
                 strBuff=10, agiBuff=2, intBuff=15, damage=12, actionCost=8, scaleValue=2.5, tier=5):
        super().__init__(name, value, weight, strBuff, agiBuff, intBuff, damage, actionCost, scaleValue, tier)
        self.setStats([5, 1, 10])
        self.setDamage(-1, 4)
        self.setWeight(-0.5, 0.5)

class SycamoreBattleStaff(BattleStaff):
    def __init__(self, name="Sycamore Battle Staff", value=65, weight=10,
                 strBuff=14, agiBuff=4, intBuff=19, damage=18, actionCost=11, scaleValue=3.0, tier=6):
        super().__init__(name, value, weight, strBuff, agiBuff, intBuff, damage, actionCost, scaleValue, tier)
        self.setStats([10, 2, 12])
        self.setDamage(-2, 5)
        self.setWeight(-0.5, 0.5)

class ElderBattleStaff(BattleStaff):
    def __init__(self, name="Elder Battle Staff", value=75, weight=12,
                 strBuff=18, agiBuff=6, intBuff=28, damage=25, actionCost=12, scaleValue=4.0, tier=7):
        super().__init__(name, value, weight, strBuff, agiBuff, intBuff, damage, actionCost, scaleValue, tier)
        self.setStats([12, 4, 20])
        self.setDamage(-5, 10)
        self.setWeight(-2, 3)
