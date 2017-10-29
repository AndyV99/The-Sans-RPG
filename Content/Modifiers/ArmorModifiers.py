from .Modifiers import *

MOD_ARM_RUSTY = ArmorModifier(prefix="Rusty", valueBuff=-1, weightBuff=-1, inDefenseBuff=-1, chance=10)
MOD_ARM_SHINY = ArmorModifier(prefix="Shiny", valueBuff=1, inDefenseBuff=1, chance=10)

MOD_ARM_OLD = ArmorModifier(prefix="Old", valueBuff=-2, inDefenseBuff=-2, chance=11)
MOD_ARM_NEW = ArmorModifier(prefix="New", valueBuff=2, strBuff=2, intBuff=1, inDefenseBuff=3, chance=11)

MOD_ARM_LIGHT = ArmorModifier(prefix="Light", valueBuff=1, weightBuff=-2, chance=20)
MOD_ARM_HEAVY = ArmorModifier(prefix="Heavy", valueBuff=1, weightBuff=2, strBuff=1, inDefenseBuff=1, chance=20)

MOD_ARM_GODLY = ArmorModifier(prefix="Godly", valueBuff=20, weightBuff=-2, strBuff=10, agiBuff=10, intBuff=10, inDefenseBuff=5, inHealthBuff=2, inActionPointBuff=2, inHealthRegenBuff=1, inActionPointRegenBuff=1, chance=2)
MOD_ARM_SHITTY = ArmorModifier(prefix="Shitty", valueBuff=-20, weightBuff=2, strBuff=-10, agiBuff=-10, intBuff=-10, inDefenseBuff=-5, inHealthBuff=-2, inActionPointBuff=-2, inHealthRegenBuff=-1, inActionPointRegenBuff=-1, chance=2)

MOD_ARM_HEALTHY = ArmorModifier(prefix="Healthy", valueBuff=12, strBuff=5, inDefenseBuff=3, inHealthBuff=10, inActionPointBuff=2, inHealthRegenBuff=5, inActionPointRegenBuff=1, chance=6)
MOD_ARM_PARASITE = ArmorModifier(prefix="Parasite", valueBuff=-8, weightBuff=2, strBuff=4, intBuff=2, inHealthBuff=-3, inActionPointBuff=-3, inHealthRegenBuff=-1, inActionPointRegenBuff=-1, chance=5)

MOD_ARM_SMART = ArmorModifier(prefix="Smart", valueBuff=1, weightBuff=0.3, intBuff=5, inDefenseBuff=1, inActionPointRegenBuff=1, chance=10)
MOD_ARM_SWIFT = ArmorModifier(prefix="Swift", valueBuff=1, weightBuff=-0.4, agiBuff=5, inDefenseBuff=1, inActionPointBuff=1, inActionPointRegenBuff=1, chance=10)
MOD_ARM_STRONG = ArmorModifier(prefix="Strong", valueBuff=1, weightBuff=0.7, strBuff=5, inDefenseBuff=1, inHealthBuff=1, inActionPointBuff=1, inHealthRegenBuff=1, chance=10)

MOD_ARM_DUMB = ArmorModifier(prefix="Dumb", valueBuff=-1, intBuff=-5, inDefenseBuff=-1, chance=14)
MOD_ARM_SLOW = ArmorModifier(prefix="Slow", valueBuff=-1, weightBuff=0.3, agiBuff=-5, inDefenseBuff=-1, inActionPointBuff=-1, chance=14)
MOD_ARM_WEAK = ArmorModifier(prefix="Weak", valueBuff=-1, weightBuff=-0.3, strBuff=-5, inDefenseBuff=-1, inHealthBuff=-1, chance=14)

MOD_ARM_GOLDEN = ArmorModifier(prefix="Golden", valueBuff=10, weightBuff=3, inDefenseBuff=2, chance=6)
MOD_ARM_CARDBOARD = ArmorModifier(prefix="Cardboard", valueBuff=-10, weightBuff=-3, inDefenseBuff=-7, chance=6)

ARMOR_MODIFIERS = [MOD_ARM_RUSTY, MOD_ARM_SHINY,
                   MOD_ARM_OLD, MOD_ARM_NEW,
                   MOD_ARM_LIGHT, MOD_ARM_HEAVY,
                   MOD_ARM_GODLY, MOD_ARM_SHITTY,
                   MOD_ARM_HEALTHY, MOD_ARM_PARASITE,
                   MOD_ARM_SMART, MOD_ARM_SWIFT, MOD_ARM_STRONG,
                   MOD_ARM_DUMB, MOD_ARM_SLOW, MOD_ARM_WEAK,
                   MOD_ARM_GOLDEN, MOD_ARM_CARDBOARD]
