from .Modifiers import FoodModifier

#MOD_FOOD_EXAMPLE = FoodModifier(prefix="Example", valueBuff=x, chance=x, inHealValueBuff=x, inUsesLeftBuff=x, inWeightBuff=x)
MOD_FOOD_GIANT = FoodModifier(prefix="Giant", valueBuff=3, chance=6, inUsesBuff=4, inWeightBuff=1.4)
MOD_FOOD_HUGE = FoodModifier(prefix="Huge", valueBuff=2, chance=8, inUsesBuff=3, inWeightBuff=1)
MOD_FOOD_BIG = FoodModifier(prefix="Big", valueBuff=1, chance=10, inUsesBuff=1, inWeightBuff=0.5)

MOD_FOOD_SMALL = FoodModifier(prefix="Small", valueBuff=-1, chance=10, inUsesBuff=-1, inWeightBuff=-0.5)
MOD_FOOD_TINY = FoodModifier(prefix="Tiny", valueBuff=-2, chance=8, inUsesBuff=-2, inWeightBuff=-1)
MOD_FOOD_MINI = FoodModifier(prefix="Mini", valueBuff=-1, chance=6, inUsesBuff=-3, inWeightBuff=-1.4)

MOD_FOOD_ORGANIC = FoodModifier(prefix="Organic", valueBuff=5, chance=10, inHealValueBuff=3)
MOD_FOOD_GM = FoodModifier(prefix="GM", valueBuff=1, chance=10, inHealValueBuff=-2, inUsesBuff=2, inWeightBuff=1)

MOD_FOOD_RIPE = FoodModifier(prefix="Ripe", valueBuff=2, chance=15, inHealValueBuff=2)
MOD_FOOD_ROTTEN = FoodModifier(prefix="Rotten", valueBuff=-2, chance=15, inHealValueBuff=-2, inUsesBuff=-2, inWeightBuff=-0.2)

FOOD_MODIFIERS = [MOD_FOOD_GIANT, MOD_FOOD_HUGE, MOD_FOOD_BIG,
                  MOD_FOOD_SMALL, MOD_FOOD_TINY, MOD_FOOD_MINI,
                  MOD_FOOD_ORGANIC, MOD_FOOD_GM,
                  MOD_FOOD_RIPE, MOD_FOOD_ROTTEN]
