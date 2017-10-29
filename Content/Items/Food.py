from .Items import Food

"""
class FoodItem(Food):
    def __init__(self, name, value, weight, healValue, uses):
        super().__init__(name, value, weight, healValue, uses)
"""

class Apple(Food):
    def __init__(self, name="Apple", value=1, weight=0.3, healValue=2, uses=1):
        super().__init__(name, value, weight, healValue, uses)


class Potato(Food):
    def __init__(self, name="Potato", value=2, weight=0.4, healValue=2, uses=2):
        super().__init__(name, value, weight, healValue, uses)


class Berries(Food):
    def __init__(self, name="Berries", value=2, weight=0.5, healValue=1, uses=5):
        super().__init__(name, value, weight, healValue, uses)


class LoafOfBread(Food):
    def __init__(self, name="Loaf of Bread", value=15, weight=0.4, healValue=5, uses=6):
        super().__init__(name, value, weight, healValue, uses)


class FrogLeg(Food):
    def __init__(self, name="Frog Leg", value=8, weight=0.2, healValue=2, uses=1):
        super().__init__(name, value, weight, healValue, uses)


class Pheasant(Food):
    def __init__(self, name="Pheasant", value=10, weight=1, healValue=6, uses=2):
        super().__init__(name, value, weight, healValue, uses)


class Rabbit(Food):
    def __init__(self, name="Rabbit", value=10, weight=1.2, healValue=6, uses=2):
        super().__init__(name, value, weight, healValue, uses)


class JarOfWater(Food):
    def __init__(self, name="Jar of Water", value=15, weight=4, healValue=5, uses=6):
        super().__init__(name, value, weight, healValue, uses)


class JarOfJam(Food):
    def __init__(self, name="Jar of Jam", value=10, weight=4, healValue=7, uses=4):
        super().__init__(name, value, weight, healValue, uses)


class SweetRoll(Food):
    def __init__(self, name="Sweet Roll", value=20, weight=3, healValue=15, uses=1):
        super().__init__(name, value, weight, healValue, uses)


class HealthPotion(Food):
    def __init__(self, name="Health Potion", value=15, weight=1, healValue=20, uses=1):
        super().__init__(name, value, weight, healValue, uses)
