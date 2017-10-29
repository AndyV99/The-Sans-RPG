from .Modifiers import *

# ----BEGIN WEAPON MODIFIERS----
MOD_WEP_RUSTY = WeaponModifier(prefix="Rusty", valueBuff=-2, inDamageBuff=-1, inActionPointCostBuff=1, chance=10)
MOD_WEP_SHINY = WeaponModifier(prefix="Shiny", valueBuff=2, inDamageBuff=1, chance=10)

MOD_WEP_OLD = WeaponModifier(prefix="Old",   valueBuff=-3, weightBuff=1, inDamageBuff=-1, inActionPointCostBuff=1, chance=11)
MOD_WEP_NEW = WeaponModifier(prefix="New", valueBuff=3, strBuff=1, intBuff=1, inDamageBuff=1, chance=11)

MOD_WEP_DAMAGED = WeaponModifier(prefix="Damaged", valueBuff=-3, weightBuff=-1, agiBuff=-1, inDamageBuff=-2, inActionPointCostBuff=2, chance=15)
MOD_WEP_USED = WeaponModifier(prefix="Used", valueBuff=-1, inDamageBuff=-1, chance=15)

MOD_WEP_LIGHT = WeaponModifier(prefix="Light", valueBuff=1, weightBuff=-3, agiBuff=2, inDamageBuff=-1, inActionPointCostBuff=-2, chance=20)
MOD_WEP_HEAVY = WeaponModifier(prefix="Heavy", valueBuff=1, weightBuff=3, strBuff=2, inDamageBuff=1, inActionPointCostBuff=2, chance=20)

MOD_WEP_GODLY = WeaponModifier(prefix="Godly", valueBuff=20, weightBuff=-4, strBuff=3, agiBuff=3, intBuff=3, inDamageBuff=5, chance=1)
MOD_WEP_SHITTY = WeaponModifier(prefix="Shitty", valueBuff=-20, weightBuff=4, strBuff=-1, agiBuff=-1, intBuff=-1, inDamageBuff=-3, inActionPointCostBuff=5, chance=1)

MOD_WEP_SMART = WeaponModifier(prefix="Smart", valueBuff=1, intBuff=2, inDamageBuff=1, inActionPointCostBuff=1, chance=16)
MOD_WEP_STRONG = WeaponModifier(prefix="Strong", valueBuff=1, weightBuff=0.5, strBuff=2, inDamageBuff=2, inActionPointCostBuff=2, chance=16)
MOD_WEP_SWIFT = WeaponModifier(prefix="Swift", valueBuff=1, weightBuff=-0.5, agiBuff=2, inActionPointCostBuff=-2, chance=16)

MOD_WEP_DUMB = WeaponModifier(prefix="Dumb", valueBuff=-1, strBuff=1, intBuff=-2, inActionPointCostBuff=1, chance=14)
MOD_WEP_SLOW = WeaponModifier(prefix="Slow", valueBuff=-1, weightBuff=1, strBuff=1, agiBuff=-2, inDamageBuff=-1, inActionPointCostBuff=1, chance=14)
MOD_WEP_WEAK = WeaponModifier(prefix="Weak", valueBuff=-1, weightBuff=-1, strBuff=-2, agiBuff=1, inDamageBuff=-2, inActionPointCostBuff=1, chance=14)

MOD_WEP_PREMIUM = WeaponModifier(prefix="Premium", valueBuff=4, strBuff=2, agiBuff=1, intBuff=1, inDamageBuff=3, inActionPointCostBuff=-1, chance=6)
MOD_WEP_DISCOUNT = WeaponModifier(prefix="Discount", valueBuff=-4, strBuff=-2, agiBuff=-1, intBuff=3, inDamageBuff=-3, inActionPointCostBuff=1, chance=6)

MOD_WEP_GOLDEN = WeaponModifier(prefix="Golden", valueBuff=10, weightBuff=2, inDamageBuff=-2, chance=5)
MOD_WEP_CARDBOARD = WeaponModifier(prefix="Cardboard", valueBuff=10, weightBuff=-2, intBuff=-3, inDamageBuff=-8, inActionPointCostBuff=-3, chance=5)

MOD_WEP_GENIUS = WeaponModifier(prefix="Genius", valueBuff=5, intBuff=10, inDamageBuff=4, inActionPointCostBuff=2, chance=3)
MOD_WEP_NINJA = WeaponModifier(prefix="Ninja", valueBuff=5, weightBuff=-1.5, agiBuff=10, inDamageBuff=4, inActionPointCostBuff=2, chance=3)
MOD_WEP_MIGHTY = WeaponModifier(prefix="Mighty", valueBuff=5, weightBuff=1.5, strBuff=10, inDamageBuff=4, inActionPointCostBuff=2, chance=3)

WEAPON_MODIFIERS = [MOD_WEP_RUSTY, MOD_WEP_SHINY,
                   MOD_WEP_OLD, MOD_WEP_NEW,
                   MOD_WEP_DAMAGED, MOD_WEP_USED,
                   MOD_WEP_LIGHT, MOD_WEP_HEAVY,
                   MOD_WEP_GODLY, MOD_WEP_SHITTY,
                   MOD_WEP_SMART, MOD_WEP_STRONG, MOD_WEP_SWIFT,
                   MOD_WEP_DUMB, MOD_WEP_SLOW, MOD_WEP_WEAK,
                   MOD_WEP_PREMIUM, MOD_WEP_DISCOUNT,
                   MOD_WEP_GOLDEN, MOD_WEP_CARDBOARD,
                   MOD_WEP_GENIUS, MOD_WEP_NINJA, MOD_WEP_MIGHTY]
