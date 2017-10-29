from os.path import dirname, abspath
d = dirname(abspath(__file__))


Coin = d + "/Art/Coin.gif"
XP = d + "/Art/XP.gif"
HP = d + "/Art/HP.gif"
AP = d + "/Art/AP.gif"

Items = d + "/Art/Items/{}.gif"
Food= d + "/Art/Items/Food/{}.gif"
HeadArmors = d + "/Art/Items/Armor/HeadArmor/{}.gif"
TorsoArmors = d + "/Art/Items/Armor/TorsoArmor/{}.gif"
LegArmors = d + "/Art/Items/Armor/LegArmor/{}.gif"

Battlestaff = d+"/Art/Items/Weapons/BattleStaffs/{}BattleStaff.gif"
Bow = d+"/Art/Items/Weapons/Bows/{}Bow.gif"
Dagger = d+"/Art/Items/Weapons/Daggers/{}Dagger.gif"
Hammer = d+"/Art/Items/Weapons/Hammers/{}Hammer.gif"
Staff = d+"/Art/Items/Weapons/Staffs/{}Staff.gif"
Sword = d+"/Art/Items/Weapons/Swords/{}Sword.gif"
Wand = d+"/Art/Items/Weapons/Wands/{}Wand.gif"

Item = Items.format("Empty")
HeadArmor = HeadArmors.format("EmptyHelmet")
TorsoArmor = TorsoArmors.format("EmptyTorso")
LegArmor = LegArmors.format("EmptyPants")
Weapon = d + "/Art/Items/Weapons/Fist.gif"

#START FOOD
Apple = Food.format("Apple")
Berries = Food.format("Berries")
FrogLeg = Food.format("FrogLeg")
HealthPotion = Food.format("HealthPotion")
JarOfJam = Food.format("JarOfJam")
JarOfWater = Food.format("JarOfWater")
LoafOfBread = Food.format("LoafOfBread")
Pheasant = Food.format("Pheasant")
Potato = Food.format("Potato")
Rabbit = Food.format("Rabbit")
SweetRoll = Food.format("SweetRoll")
#END FOOD

#START BATTLESTAFFS
BirchBattleStaff = Battlestaff.format("Birch")
DogwoodBattleStaff = Battlestaff.format("Dogwood")
ElderBattleStaff = Battlestaff.format("Elder")
HemlockBattleStaff = Battlestaff.format("Hemlock")
OakBattleStaff = Battlestaff.format("Oak")
SycamoreBattleStaff = Battlestaff.format("Sycamore")
WalnutBattleStaff = Battlestaff.format("Walnut")
#END BATTLESTAFFS

#START BOWS
MagicBow = Bow.format("Magic")
MapleBow = Bow.format("Maple")
OakBow = Bow.format("Oak")
WillowBow = Bow.format("Willow")
YewBow = Bow.format("Yew")
#END BOWS

#START DAGGERS
AdamantineDagger = Dagger.format("Adamantine")
BronzeDagger = Dagger.format("Bronze")
PlatinumDagger = Dagger.format("Platinum")
SteelDagger = Dagger.format("Steel")
StoneDagger = Dagger.format("Stone")
VibraniumDagger = Dagger.format("Vibranium")
WoodenDagger = Dagger.format("Wooden")
#END DAGGERS

#START HAMMERS
AdamantineHammer = Hammer.format("Adamantine")
BronzeHammer = Hammer.format("Bronze")
PlatinumHammer = Hammer.format("Platinum")
SteelHammer = Hammer.format("Steel")
StoneHammer = Hammer.format("Stone")
VibraniumHammer = Hammer.format("Vibranium")
WoodenHammer = Hammer.format("Wooden")
#END HAMMERS

#START STAFFS
BirchStaff = Staff.format("Birch")
DogwoodStaff = Staff.format("Dogwood")
ElderStaff = Staff.format("Elder")
HemlockStaff = Staff.format("Hemlock")
OakStaff = Staff.format("Oak")
SycamoreStaff = Staff.format("Sycamore")
WalnutStaff = Staff.format("Walnut")
#END STAFFS

#START SWORDS
AdamantineSword = Sword.format("Adamantine")
BronzeSword = Sword.format("Bronze")
PlatinumSword = Sword.format("Platinum")
SteelSword = Sword.format("Steel")
StoneSword = Sword.format("Stone")
VibraniumSword = Sword.format("Vibranium")
WoodenSword = Sword.format("Wooden")
#END SWORDS

#START WANDS
BirchWand = Wand.format("Birch")
DogwoodWand = Wand.format("Dogwood")
ElderWand = Wand.format("Elder")
HemlockWand = Wand.format("Hemlock")
OakWand = Wand.format("Oak")
SycamoreWand = Wand.format("Sycamore")
WalnutWand = Wand.format("Walnut")
#END WANDS

#START HEAD AROMR
AdamantineHelmet = HeadArmors.format("AdamantineHelmet")
BronzeHelmet = HeadArmors.format("BronzeHelmet")
IronHelmet = HeadArmors.format("IronHelmet")
PlatinumHelmet = HeadArmors.format("PlatinumHelmet")
SteelHelmet = HeadArmors.format("SteelHelmet")
VibraniumHelmet = HeadArmors.format("VibraniumHelmet")

ApprenticeHood = HeadArmors.format("ApprenticeHood")
BeginnerHood = HeadArmors.format("BeginnerHood")
MasterHood = HeadArmors.format("MasterHood")
NoviceHood = HeadArmors.format("NoviceHood")
WizardHood = HeadArmors.format("WizardHood")

CloakingCap = HeadArmors.format("CloakingCap")
HeavyLeatherCap = HeadArmors.format("HeavyLeatherCap")
LightLeatherCap = HeadArmors.format("LightLeatherCap")
SnakeSkinCap = HeadArmors.format("SnakeSkinCap")
StuddedLeatherCap = HeadArmors.format("StuddedLeatherCap")
WolfFurCap = HeadArmors.format("WolfFurCap")
#END HEAD ARMOR

#START TORSO ARMOR
AdamantineTorso = TorsoArmors.format("AdamantineTorso")
BronzeTorso = TorsoArmors.format("BronzeTorso")
IronTorso = TorsoArmors.format("IronTorso")
PlatinumTorso = TorsoArmors.format("PlatinumTorso")
SteelTorso = TorsoArmors.format("SteelTorso")
VibraniumTorso = TorsoArmors.format("VibraniumTorso")

CloakingShirt = TorsoArmors.format("CloakingShirt")
HeavyLeatherShirt = TorsoArmors.format("HeavyLeatherShirt")
LightLeatherShirt = TorsoArmors.format("LightLeatherShirt")
SnakeSkinShirt = TorsoArmors.format("SnakeSkinShirt")
StuddedLeatherShirt = TorsoArmors.format("StuddedLeatherShirt")
WolfFurShirt = TorsoArmors.format("WolfFurShirt")

ApprenticeRobe = TorsoArmors.format("ApprenticeRobe")
BeginnerRobe = TorsoArmors.format("BeginnerRobe")
MasterRobe = TorsoArmors.format("MasterRobe")
NoviceRobe = TorsoArmors.format("NoviceRobe")
WizardRobe = TorsoArmors.format("WizardRobe")
#END TORSO ARMOR

#START LEG ARMOR
AdamantinePants = LegArmors.format("AdamantinePants")
BronzePants = LegArmors.format("BronzePants")
IronPants = LegArmors.format("IronPants")
PlatinumPants = LegArmors.format("PlatinumPants")
SteelPants = LegArmors.format("SteelPants")
VibraniumPants = LegArmors.format("VibraniumPants")

CloakingPants = LegArmors.format("CloakingPants")
HeavyLeatherPants = LegArmors.format("HeavyLeatherPants")
LightLeatherPants = LegArmors.format("LightLeatherPants")
SnakeSkinPants = LegArmors.format("SnakeSkinPants")
StuddedLeatherPants = LegArmors.format("StuddedLeatherPants")
WolfFurPants = LegArmors.format("WolfFurPants")

ApprenticePants = LegArmors.format("ApprenticePants")
BeginnerPants = LegArmors.format("BeginnerPants")
MasterPants = LegArmors.format("MasterPants")
NovicePants = LegArmors.format("NovicePants")
WizardPants = LegArmors.format("WizardPants")
#END LEG ARMOR
