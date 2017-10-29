from .Armor import LegArmor

class BronzePants(LegArmor):
    def __init__(self, name="Bronze Pants", value=10, weight=4, strBuff=2, agiBuff=0, intBuff=0, defense=3, hp=0, ap=0, hpR=0, apR=0, tier=1):
        super().__init__(name, value, weight, strBuff, agiBuff, intBuff, defense, hp, ap, hpR, apR, tier)
        self.setStats([0, 0, 0])
        self.setWeight(-1, 1)


class IronPants(LegArmor):
    def __init__(self, name="Iron Pants", value=20, weight=6, strBuff=4, agiBuff=0, intBuff=0, defense=4, hp=0, ap=0, hpR=0, apR=0, tier=2):
        super().__init__(name, value, weight, strBuff, agiBuff, intBuff, defense, hp, ap, hpR, apR, tier)
        self.setStats([1, 0, 0])
        self.setWeight(-2.1, 1.1)


class SteelPants(LegArmor):
    def __init__(self, name="Steel Pants", value=30, weight=6, strBuff=5, agiBuff=0, intBuff=0, defense=5, hp=0, ap=0, hpR=0, apR=0, tier=3):
        super().__init__(name, value, weight, strBuff, agiBuff, intBuff, defense, hp, ap, hpR, apR, tier)
        self.setStats([2, 0, 0])
        self.setWeight(-2.5, 2.5)


class PlatinumPants(LegArmor):
    def __init__(self, name="Platinum Pants", value=40, weight=7, strBuff=7, agiBuff=0, intBuff=0, defense=6, hp=0, ap=0, hpR=0, apR=0, tier=4):
        super().__init__(name, value, weight, strBuff, agiBuff, intBuff, defense, hp, ap, hpR, apR, tier)
        self.setStats([2, 0, 0])
        self.setWeight(-1.9, 1.2)


class AdamantinePants(LegArmor):
    def __init__(self, name="Adamantine Pants", value=50, weight=10, strBuff=10, agiBuff=2, intBuff=2, defense=9, hp=2, ap=2, hpR=1, apR=0, tier=5):
        super().__init__(name, value, weight, strBuff, agiBuff, intBuff, defense, hp, ap, hpR, apR, tier)
        self.setStats([4, 1, 0])
        self.setWeight(-2, 2)


class VibraniumPants(LegArmor):
    def __init__(self, name="Vibranium Pants", value=50, weight=11, strBuff=15, agiBuff=3, intBuff=3, defense=10, hp=2, ap=3, hpR=2, apR=2, tier=6):
        super().__init__(name, value, weight, strBuff, agiBuff, intBuff, defense, hp, ap, hpR, apR, tier)
        self.setStats([9, 1, 0])
        self.setWeight(-3, 3)

#-------------------------------

class LightLeatherPants(LegArmor):
    def __init__(self, name="Light-Leather Pants", value=10, weight=2, strBuff=0, agiBuff=2, intBuff=0, defense=1, hp=0, ap=1, hpR=0, apR=0, tier=1):
        super().__init__(name, value, weight, strBuff, agiBuff, intBuff, defense, hp, ap, hpR, apR, tier)
        self.setStats([0, 0, 0])
        self.setWeight(-0.5, 0.2)


class HeavyLeatherPants(LegArmor):
    def __init__(self, name="Heavy-Leather Pants", value=20, weight=4, strBuff=1, agiBuff=3, intBuff=0, defense=2, hp=0, ap=1, hpR=0, apR=0, tier=2):
        super().__init__(name, value, weight, strBuff, agiBuff, intBuff, defense, hp, ap, hpR, apR, tier)
        self.setStats([0, 1, 0])
        self.setWeight(-0.6, 0.6)


class StuddedLeatherPants(LegArmor):
    def __init__(self, name="Studded Leather Pants", value=30, weight=6, strBuff=2, agiBuff=4, intBuff=0, defense=3, hp=0, ap=2, hpR=0, apR=0, tier=3):
        super().__init__(name, value, weight, strBuff, agiBuff, intBuff, defense, hp, ap, hpR, apR, tier)
        self.setStats([0, 1, 0])
        self.setWeight(-0.5, 0.3)


class WolfFurPants(LegArmor):
    def __init__(self, name="Wolf Fur Pants", value=40, weight=5, strBuff=0, agiBuff=5, intBuff=0, defense=4, hp=0, ap=3, hpR=0, apR=0, tier=4):
        super().__init__(name, value, weight, strBuff, agiBuff, intBuff, defense, hp, ap, hpR, apR, tier)
        self.setStats([0, 2, 0])
        self.setWeight(-0.8, 0.8)


class SnakeSkinPants(LegArmor):
    def __init__(self, name="Snake Skin Pants", value=50, weight=5, strBuff=1, agiBuff=6, intBuff=0, defense=5, hp=0, ap=4, hpR=0, apR=2, tier=5):
        super().__init__(name, value, weight, strBuff, agiBuff, intBuff, defense, hp, ap, hpR, apR, tier)
        self.setStats([0, 3, 0])
        self.setWeight(-1.5, 1.5)


class CloakingPants(LegArmor):
    def __init__(self, name="Cloaking Pants", value=60, weight=4, strBuff=0, agiBuff=10, intBuff=0, defense=6, hp=0, ap=5, hpR=1, apR=4, tier=6):
        super().__init__(name, value, weight, strBuff, agiBuff, intBuff, defense, hp, ap, hpR, apR, tier)
        self.setStats([0, 7, 0])
        self.setWeight(-1, 1.2)

#-------------------------------

class BeginnerPants(LegArmor):
    def __init__(self, name="Beginner Pants", value=10, weight=3, strBuff=0, agiBuff=0, intBuff=1, defense=1, hp=0, ap=2, hpR=0, apR=1, tier=1):
        super().__init__(name, value, weight, strBuff, agiBuff, intBuff, defense, hp, ap, hpR, apR, tier)
        self.setStats([0, 0, 0])
        self.setWeight(-0.5, 0.5)


class NovicePants(LegArmor):
    def __init__(self, name="Novice Pants", value=20, weight=3, strBuff=0, agiBuff=0, intBuff=3, defense=2, hp=0, ap=3, hpR=0, apR=2, tier=2):
        super().__init__(name, value, weight, strBuff, agiBuff, intBuff, defense, hp, ap, hpR, apR, tier)
        self.setStats([0, 0, 1])
        self.setWeight(-0.7, 0.8)


class ApprenticePants(LegArmor):
    def __init__(self, name="Apprentice Pants", value=30, weight=3, strBuff=0, agiBuff=0, intBuff=6, defense=3, hp=0, ap=5, hpR=0, apR=3, tier=3):
        super().__init__(name, value, weight, strBuff, agiBuff, intBuff, defense, hp, ap, hpR, apR, tier)
        self.setStats([0, 0, 2])
        self.setWeight(-0.5, 0.5)

class WizardPants(LegArmor):
    def __init__(self, name="Wizard Pants", value=40, weight=4, strBuff=0, agiBuff=0, intBuff=9, defense=5, hp=0, ap=7, hpR=0, apR=4, tier=4):
        super().__init__(name, value, weight, strBuff, agiBuff, intBuff, defense, hp, ap, hpR, apR, tier)
        self.setStats([0, 0, 6])
        self.setWeight(-0.7, 0.7)


class MasterPants(LegArmor):
    def __init__(self, name="Master Pants", value=50, weight=3, strBuff=2, agiBuff=2, intBuff=15, defense=7, hp=0, ap=10, hpR=0, apR=5, tier=5):
        super().__init__(name, value, weight, strBuff, agiBuff, intBuff, defense, hp, ap, hpR, apR, tier)
        self.setStats([0, 0, 9])
        self.setWeight(-0.7, 0.8)
