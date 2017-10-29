from .Armor import HeadArmor

class BronzeHelmet(HeadArmor):
    def __init__(self, name="Bronze Helmet", value=10, weight=3, strBuff=2, agiBuff=0, intBuff=0, defense=3, hp=0, ap=0, hpR=0, apR=0, tier=1):
        super().__init__(name, value, weight, strBuff, agiBuff, intBuff, defense, hp, ap, hpR, apR, tier)
        self.setStats([0, 0, 0])
        self.setWeight(-0.2, 0.4)


class IronHelmet(HeadArmor):
    def __init__(self, name="Iron Helmet", value=20, weight=5, strBuff=4, agiBuff=0, intBuff=0, defense=4, hp=0, ap=0, hpR=0, apR=0, tier=2):
        super().__init__(name, value, weight, strBuff, agiBuff, intBuff, defense, hp, ap, hpR, apR, tier)
        self.setStats([2, 0, 0])
        self.setWeight(-0.3, 0.3)


class SteelHelmet(HeadArmor):
    def __init__(self, name="Steel Helmet", value=30, weight=5, strBuff=5, agiBuff=0, intBuff=0, defense=5, hp=0, ap=0, hpR=0, apR=0, tier=3):
        super().__init__(name, value, weight, strBuff, agiBuff, intBuff, defense, hp, ap, hpR, apR, tier)
        self.setStats([2, 0, 0])
        self.setWeight(-0.5, 0.5)


class PlatinumHelmet(HeadArmor):
    def __init__(self, name="Platinum Helmet", value=40, weight=6, strBuff=7, agiBuff=0, intBuff=0, defense=6, hp=0, ap=0, hpR=0, apR=0, tier=4):
        super().__init__(name, value, weight, strBuff, agiBuff, intBuff, defense, hp, ap, hpR, apR, tier)
        self.setStats([4, 0, 0])
        self.setWeight(-1.2, 1.4)


class AdamantineHelmet(HeadArmor):
    def __init__(self, name="Adamantine Helmet", value=50, weight=9, strBuff=10, agiBuff=2, intBuff=2, defense=9, hp=2, ap=2, hpR=1, apR=0, tier=5):
        super().__init__(name, value, weight, strBuff, agiBuff, intBuff, defense, hp, ap, hpR, apR, tier)
        self.setStats([6, 1, 1])
        self.setWeight(-1, 1.5)


class VibraniumHelmet(HeadArmor):
    def __init__(self, name="Vibranium Helmet", value=60, weight=10, strBuff=15, agiBuff=3, intBuff=3, defense=10, hp=2, ap=3, hpR=2, apR=2, tier=6):
        super().__init__(name, value, weight, strBuff, agiBuff, intBuff, defense, hp, ap, hpR, apR, tier)
        self.setStats([11, 1, 2])
        self.setWeight(-2, 1.4)

#-------------------------------

class LightLeatherCap(HeadArmor):
    def __init__(self, name="Light-Leather Cap", value=10, weight=1, strBuff=0, agiBuff=2, intBuff=0, defense=1, hp=0, ap=1, hpR=0, apR=0, tier=1):
        super().__init__(name, value, weight, strBuff, agiBuff, intBuff, defense, hp, ap, hpR, apR, tier)
        self.setStats([0, 0, 0])
        self.setWeight(-0.2, 0.2)


class HeavyLeatherCap(HeadArmor):
    def __init__(self, name="Heavy-Leather Cap", value=20, weight=3, strBuff=1, agiBuff=3, intBuff=0, defense=2, hp=0, ap=1, hpR=0, apR=0, tier=2):
        super().__init__(name, value, weight, strBuff, agiBuff, intBuff, defense, hp, ap, hpR, apR, tier)
        self.setStats([0, 0, 0])
        self.setWeight(-0.2, 0.2)


class StuddedLeatherCap(HeadArmor):
    def __init__(self, name="Studded Leather Cap", value=30, weight=3, strBuff=1, agiBuff=3, intBuff=0, defense=2, hp=0, ap=1, hpR=0, apR=0, tier=3):
        super().__init__(name, value, weight, strBuff, agiBuff, intBuff, defense, hp, ap, hpR, apR, tier)
        self.setStats([0, 1, 0])
        self.setWeight(-0.4, 0.4)


class WolfFurCap(HeadArmor):
    def __init__(self, name="Wolf Fur Cap", value=40, weight=4, strBuff=0, agiBuff=5, intBuff=0, defense=4, hp=0, ap=3, hpR=0, apR=0, tier=4):
        super().__init__(name, value, weight, strBuff, agiBuff, intBuff, defense, hp, ap, hpR, apR, tier)
        self.setStats([0, 3, 0])
        self.setWeight(-0.9, 0.9)


class SnakeSkinCap(HeadArmor):
    def __init__(self, name="Snake Skin Cap", value=50, weight=4, strBuff=1, agiBuff=6, intBuff=0, defense=5, hp=0, ap=4, hpR=0, apR=2, tier=5):
        super().__init__(name, value, weight, strBuff, agiBuff, intBuff, defense, hp, ap, hpR, apR, tier)
        self.setStats([0, 4, 0])
        self.setWeight(-1, 1)


class CloakingCap(HeadArmor):
    def __init__(self, name="Cloaking Cap", value=60, weight=3, strBuff=0, agiBuff=10, intBuff=0, defense=6, hp=0, ap=5, hpR=1, apR=4, tier=6):
        super().__init__(name, value, weight, strBuff, agiBuff, intBuff, defense, hp, ap, hpR, apR, tier)
        self.setStats([0, 7, 0])
        self.setWeight(-0.9, 1.2)

#-------------------------------

class BeginnerHood(HeadArmor):
    def __init__(self, name="Beginner Hood", value=10, weight=2, strBuff=0, agiBuff=0, intBuff=1, defense=1, hp=0, ap=2, hpR=0, apR=1, tier=1):
        super().__init__(name, value, weight, strBuff, agiBuff, intBuff, defense, hp, ap, hpR, apR, tier)
        self.setStats([0, 0, 0])
        self.setWeight(-0.5, 0.6)


class NoviceHood(HeadArmor):
    def __init__(self, name="Novice Hood", value=20, weight=2, strBuff=0, agiBuff=0, intBuff=3, defense=1, hp=0, ap=3, hpR=0, apR=2, tier=2):
        super().__init__(name, value, weight, strBuff, agiBuff, intBuff, defense, hp, ap, hpR, apR, tier)
        self.setStats([0, 0, 1])
        self.setWeight(-0.5, 0.5)


class ApprenticeHood(HeadArmor):
    def __init__(self, name="Apprentice Hood", value=30, weight=2, strBuff=0, agiBuff=0, intBuff=6, defense=1, hp=0, ap=5, hpR=0, apR=3, tier=3):
        super().__init__(name, value, weight, strBuff, agiBuff, intBuff, defense, hp, ap, hpR, apR, tier)
        self.setStats([0, 0, 3])
        self.setWeight(-0.5, 0.5)


class WizardHood(HeadArmor):
    def __init__(self, name="Wizard Hood", value=40, weight=3, strBuff=0, agiBuff=0, intBuff=9, defense=1, hp=0, ap=7, hpR=0, apR=3, tier=4):
        super().__init__(name, value, weight, strBuff, agiBuff, intBuff, defense, hp, ap, hpR, apR, tier)
        self.setStats([0, 0, 6])
        self.setWeight(-0.7, 0.7)


class MasterHood(HeadArmor):
    def __init__(self, name="Master Hood", value=50, weight=2, strBuff=2, agiBuff=2, intBuff=15, defense=2, hp=0, ap=10, hpR=0, apR=4, tier=5):
        super().__init__(name, value, weight, strBuff, agiBuff, intBuff, defense, hp, ap, hpR, apR, tier)
        self.setStats([0, 1, 11])
        self.setWeight(-0.5, 0.4)
