from .Weapons import Weapons
from .Armor import Armor
from . import Items

"""
LIST COMPREHENSION SAVED MY LIFE HERE
REMEMBER LIST COMPREHENSION, IT'S USEFUL
"""

"""
Get all subclasses of all subclasses of Weapons, this will return 7 lists, each list containing all of each weapon (Battle Staffs, Bows, etc.)

then create an instance of each, this will allow for the getting of the tier

find the maximum tier to decide how many sub-lists to make for tiers, this will allow modding

initialize the list with enough sub-lists for each tier

add each of the classes to their respective tiers
"""

weaponLists = [p.__subclasses__() for p in Weapons.Weapon.__subclasses__()]

allWeapons = [wep() for wepList in weaponLists for wep in wepList]

maxTierWep = max(p.tier for p in allWeapons)

weaponTiers = [[] for _ in range(maxTierWep)]

for wep in allWeapons:
    weaponTiers[wep.tier-1].append(wep.__class__)


"""
This is the EXACT same algorithm used above, but this time it is used for armor instead of weapons
"""
armorLists = [r.__subclasses__() for r in Armor.Armor.__subclasses__()]

allArmor = [arm() for armList in armorLists for arm in armList]

maxTierArm = max(r.tier for r in allArmor)

armorTiers = [[] for _ in range(maxTierArm)]

for arm in allArmor:
    armorTiers[arm.tier-1].append(arm.__class__)


allFood = [r for r in Items.Food.__subclasses__()]
