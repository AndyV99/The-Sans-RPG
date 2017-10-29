from .Weapons import Staff

class OakStaff(Staff):
    def __init__(self, name="Oak Staff", value=10, weight=3,
                 strBuff=0, agiBuff=0, intBuff=4, damage=3, actionCost=3, scaleValue=1.4, tier=1):
        super().__init__(name, value, weight, strBuff, agiBuff, intBuff, damage, actionCost, scaleValue)
        self.setStats([0, 0, 2])
        self.setDamage(-1, 2)
        self.setWeight(-0.5, 0.5)


class BirchStaff(Staff):
    def __init__(self, name="Birch Staff", value=20, weight=3,
                 strBuff=2, agiBuff=0, intBuff=4, damage=4, actionCost=3, scaleValue=1.9, tier=2):
        super().__init__(name, value, weight, strBuff, agiBuff, intBuff, damage, actionCost, scaleValue, tier)
        self.setStats([1, 0, 2])
        self.setDamage(-2, 4)
        self.setWeight(-1, 0.8)


class DogwoodStaff(Staff):
    def __init__(self, name="Dogwood Staff", value=35, weight=2,
                 strBuff=0, agiBuff=8, intBuff=5, damage=6, actionCost=3, scaleValue=2.3, tier=3):
        super().__init__(name, value, weight, strBuff, agiBuff, intBuff, damage, actionCost, scaleValue, tier)
        self.setStats([0, 5, 3])
        self.setDamage(-2, 3)
        self.setWeight(-1, 1)


class HemlockStaff(Staff):
    def __init__(self, name="Hemlock Staff", value=45, weight=4,
                 strBuff=0, agiBuff=7, intBuff=8, damage=9, actionCost=6, scaleValue=2.6, tier=4):
        super().__init__(name, value, weight, strBuff, agiBuff, intBuff, damage, actionCost, scaleValue, tier)
        self.setStats([0, 5, 5])
        self.setDamage(-1, 4)
        self.setWeight(-1.5, 0.5)


class WalnutStaff(Staff):
    def __init__(self, name="Walnut Staff", value=55, weight=6,
                 strBuff=0, agiBuff=2, intBuff=10, damage=10, actionCost=9, scaleValue=3.3, tier=5):
        super().__init__(name, value, weight, strBuff, agiBuff, intBuff, damage, actionCost, scaleValue, tier)
        self.setStats([0, 1, 4])
        self.setDamage(-1, 4)
        self.setWeight(-0.1, 0.4)


class SycamoreStaff(Staff):
    def __init__(self, name="Sycamore Staff", value=65, weight=1.5,
                 strBuff=2, agiBuff=5, intBuff=10, damage=12, actionCost=7, scaleValue=3.8, tier=6):
        super().__init__(name, value, weight, strBuff, agiBuff, intBuff, damage, actionCost, scaleValue, tier)
        self.setStats([1, 3, 7])
        self.setDamage(-1, 5)
        self.setWeight(-0.2, 0.3)


class ElderStaff(Staff):
    def __init__(self, name="Elder Staff", value=75, weight=10,
                 strBuff=3, agiBuff=5, intBuff=20, damage=18, actionCost=12, scaleValue=4.0, tier=7):
        super().__init__(name, value, weight, strBuff, agiBuff, intBuff, damage, actionCost, scaleValue, tier)
        self.setStats([1, 4, 15])
        self.setDamage(-5, 10)
        self.setWeight(-1, 1)
