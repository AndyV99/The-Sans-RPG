from .Armor import TorsoArmor

class BronzeTorso(TorsoArmor):
    def __init__(self, name="Bronze Torso", value=20, weight=5, strBuff=3, agiBuff=0, intBuff=0, defense=5, hp=0, ap=0, hpR=0, apR=0, tier=1):
        super().__init__(name, value, weight, strBuff, agiBuff, intBuff, defense, hp, ap, hpR, apR, tier)
        self.setStats([1, 0, 0])
        self.setWeight(-1, 1)


class IronTorso(TorsoArmor):
    def __init__(self, name="Iron Torso", value=30, weight=8, strBuff=6, agiBuff=0, intBuff=0, defense=9, hp=0, ap=0, hpR=0, apR=0, tier=2):
        super().__init__(name, value, weight, strBuff, agiBuff, intBuff, defense, hp, ap, hpR, apR, tier)
        self.setStats([4, 0, 0])
        self.setWeight(-1.1, 1.1)


class SteelTorso(TorsoArmor):
    def __init__(self, name="Steel Torso", value=45, weight=10, strBuff=8, agiBuff=0, intBuff=0, defense=11, hp=0, ap=0, hpR=0, apR=0, tier=3):
        super().__init__(name, value, weight, strBuff, agiBuff, intBuff, defense, hp, ap, hpR, apR, tier)
        self.setStats([4, 0, 0])
        self.setWeight(-1.5, 1.5)


class PlatinumTorso(TorsoArmor):
    def __init__(self, name="Platinum Torso", value=55, weight=12, strBuff=10, agiBuff=0, intBuff=0, defense=15, hp=0, ap=0, hpR=0, apR=0, tier=4):
        super().__init__(name, value, weight, strBuff, agiBuff, intBuff, defense, hp, ap, hpR, apR, tier)
        self.setStats([5, 0, 0])
        self.setWeight(-1.9, 1.2)


class AdamantineTorso(TorsoArmor):
    def __init__(self, name="Adamantine Torso", value=65, weight=15, strBuff=15, agiBuff=5, intBuff=5, defense=20, hp=4, ap=4, hpR=2, apR=0, tier=5):
        super().__init__(name, value, weight, strBuff, agiBuff, intBuff, defense, hp, ap, hpR, apR, tier)
        self.setStats([9, 0, 0])
        self.setWeight(-2, 2)


class VibraniumTorso(TorsoArmor):
    def __init__(self, name="Vibranium Torso", value=75, weight=19, strBuff=25, agiBuff=10, intBuff=10, defense=10, hp=5, ap=6, hpR=4, apR=0, tier=6):
        super().__init__(name, value, weight, strBuff, agiBuff, intBuff, defense, hp, ap, hpR, apR, tier)
        self.setStats([19, 5, 5])
        self.setWeight(-3, 3)

#-------------------------------

class LightLeatherShirt(TorsoArmor):
    def __init__(self, name="Light-Leather Shirt", value=17, weight=3, strBuff=0, agiBuff=2, intBuff=0, defense=2, hp=0, ap=2, hpR=0, apR=0, tier=1):
        super().__init__(name, value, weight, strBuff, agiBuff, intBuff, defense, hp, ap, hpR, apR, tier)
        self.setStats([0, 1, 0])
        self.setWeight(-0.6, 0.2)


class HeavyLeatherShirt(TorsoArmor):
    def __init__(self, name="Heavy-Leather Shirt", value=27, weight=5, strBuff=0, agiBuff=4, intBuff=0, defense=4, hp=0, ap=3, hpR=0, apR=1, tier=2):
        super().__init__(name, value, weight, strBuff, agiBuff, intBuff, defense, hp, ap, hpR, apR, tier)
        self.setStats([0, 2, 0])
        self.setWeight(-0.4, 0.4)


class StuddedLeatherShirt(TorsoArmor):
    def __init__(self, name="Studded Leather Shirt", value=42, weight=8, strBuff=0, agiBuff=6, intBuff=0, defense=6, hp=0, ap=4, hpR=0, apR=1, tier=3):
        super().__init__(name, value, weight, strBuff, agiBuff, intBuff, defense, hp, ap, hpR, apR, tier)
        self.setStats([0, 3, 0])
        self.setWeight(-0.5, 0.3)


class WolfFurShirt(TorsoArmor):
    def __init__(self, name="Wolf Fur Shirt", value=52, weight=9, strBuff=0, agiBuff=10, intBuff=0, defense=9, hp=0, ap=5, hpR=0, apR=2, tier=4):
        super().__init__(name, value, weight, strBuff, agiBuff, intBuff, defense, hp, ap, hpR, apR, tier)
        self.setStats([0, 5, 0])
        self.setWeight(-0.9, 0.9)


class SnakeSkinShirt(TorsoArmor):
    def __init__(self, name="Snake Skin Shirt", value=62, weight=4, strBuff=2, agiBuff=14, intBuff=2, defense=10, hp=0, ap=7, hpR=0, apR=2, tier=5):
        super().__init__(name, value, weight, strBuff, agiBuff, intBuff, defense, hp, ap, hpR, apR, tier)
        self.setStats([1, 8, 0])
        self.setWeight(-1.5, 1.5)


class CloakingShirt(TorsoArmor):
    def __init__(self, name="Cloaking Shirt", value=72, weight=7, strBuff=4, agiBuff=20, intBuff=4, defense=15, hp=2, ap=10, hpR=2, apR=5, tier=6):
        super().__init__(name, value, weight, strBuff, agiBuff, intBuff, defense, hp, ap, hpR, apR, tier)
        self.setStats([2, 12, 2])
        self.setWeight(-1, 1.2)

#-------------------------------

class BeginnerRobe(TorsoArmor):
    def __init__(self, name="Beginner Robe", value=15, weight=4, strBuff=0, agiBuff=0, intBuff=4, defense=2, hp=0, ap=3, hpR=0, apR=1, tier=1):
        super().__init__(name, value, weight, strBuff, agiBuff, intBuff, defense, hp, ap, hpR, apR, tier)
        self.setStats([0, 0, 1])
        self.setWeight(-0.5, 0.5)


class NoviceRobe(TorsoArmor):
    def __init__(self, name="Novice Robe", value=4, weight=25, strBuff=0, agiBuff=0, intBuff=6, defense=3, hp=0, ap=4, hpR=0, apR=3, tier=2):
        super().__init__(name, value, weight, strBuff, agiBuff, intBuff, defense, hp, ap, hpR, apR, tier)
        self.setStats([0, 0, 2])
        self.setWeight(-0.7, 0.8)


class ApprenticeRobe(TorsoArmor):
    def __init__(self, name="Apprentice Robe", value=6, weight=40, strBuff=0, agiBuff=0, intBuff=9, defense=4, hp=0, ap=6, hpR=0, apR=4, tier=3):
        super().__init__(name, value, weight, strBuff, agiBuff, intBuff, defense, hp, ap, hpR, apR, tier)
        self.setStats([0, 0, 3])
        self.setWeight(-0.5, 0.5)


class WizardRobe(TorsoArmor):
    def __init__(self, name="Wizard Robe", value=50, weight=5, strBuff=2, agiBuff=2, intBuff=14, defense=6, hp=0, ap=9, hpR=0, apR=6, tier=4):
        super().__init__(name, value, weight, strBuff, agiBuff, intBuff, defense, hp, ap, hpR, apR, tier)
        self.setStats([0, 0, 9])
        self.setWeight(-0.7, 0.7)


class MasterRobe(TorsoArmor):
    def __init__(self, name="Master Robe", value=70, weight=4, strBuff=4, agiBuff=6, intBuff=20, defense=8, hp=0, ap=14, hpR=0, apR=8, tier=5):
        super().__init__(name, value, weight, strBuff, agiBuff, intBuff, defense, hp, ap, hpR, apR, tier)
        self.setStats([1, 2, 15])
        self.setWeight(-0.7, 0.8)
