from ..Beings import Enemy
from random import *

class Rat(Enemy):
    def __init__(self, name="Rat", level=1):
        super().__init__(name, level, 0)
        self.totalHealth = randint(int(self.level*4), int(self.level*5))
        self.currentHealth = self.totalHealth
        self.damage = randint(int(level*2), max((int(level*2)+1, int(3*(level-1)))))
        self.defense = level
        self.evasiveness = round(level+1, 1)
        self.speed = round(3*level, 1)
        self.lootChance = level//2
        self.xp = randint(int(level*3), int(level*5))


class Bat(Enemy):
    def __init__(self, name="Bat", level=1):
        super().__init__(name, level, 0)
        self.totalHealth = randint(int(self.level*3), int(self.level*5))
        self.currentHealth = self.totalHealth
        self.damage = randint(int(level), max((int(level*2)+1, int(3*(level-1)))))
        self.defense = level
        self.evasiveness = round(2*level+1, 1)
        self.speed = round(4*level, 1)
        self.lootChance = level//2
        self.xp = randint(int(level*4), int(level*6))


class Spider(Enemy):
    def __init__(self, name="Spider", level=1):
        super().__init__(name, level, 0)
        self.totalHealth = randint(int(self.level*3), int(self.level*5))
        self.currentHealth = self.totalHealth
        self.damage = randint(int(level*2), int(level*3))
        self.defense = level
        self.evasiveness = round(3*level+1, 1)
        self.speed = round(4*level, 1)
        self.lootChance = level//2
        self.xp = randint(int(level*4), int(level*6))


class Goblin(Enemy):
    def __init__(self, name="Spider", level=1):
        super().__init__(name, level, 0)
        self.totalHealth = randint(int(self.level*5), int(self.level*8))
        self.currentHealth = self.totalHealth
        self.damage = randint(int(2*level), int(3*level))
        self.defense = level
        self.evasiveness = 0 + level
        self.speed = round(2*level, 1)
        self.lootChance = (level+1)//2
        self.xp = randint(int(level*6), int(level*8))


class Wolf(Enemy):
    def __init__(self, name="Wolf", level=1):
        super().__init__(name, level, 0)
        self.totalHealth = randint(int(self.level*6), int(self.level*9))
        self.currentHealth = self.totalHealth
        self.damage = randint(int(self.level*3), int(self.level*4))+1
        self.defense = level
        self.evasiveness = 2 + level
        self.speed = round(4*level, 1)
        self.xp = randint(int(level*7), int(level*10))


class Skeleton(Enemy):
    def __init__(self, name="Skeleton", level=1):
        super().__init__(name, level, 0)
        self.totalHealth = randint(int(self.level*4), int(self.level*8))
        self.currentHealth = self.totalHealth
        self.damage = randint(int(self.level*4), int(self.level*5))
        self.defense = level
        self.evasiveness = 0 + level
        self.speed = round(2*level, 1)
        self.lootChance = (level+3)//2
        self.xp = randint(int(level*8), int(level*11))


class Orc(Enemy):
    def __init__(self, name="Orc", level=1):
        super().__init__(name, level, 0)
        self.totalHealth = randint(int(self.level*8), int(self.level*13))
        self.currentHealth = self.totalHealth
        self.damage = randint(int(self.level*6), int(self.level*9))
        self.defense = 2 + level
        self.evasiveness = 1 + level
        self.speed = round(1*level, 1)
        self.lootChance = (level+6)//2
        self.xp = randint(int(level*9), int(level*15))


class Giant(Enemy):
    def __init__(self, name="Giant", level=1):
        super().__init__(name, level, 0)
        self.totalHealth = randint(int(self.level*15), int(self.level*25))
        self.currentHealth = self.totalHealth
        self.damage = randint(int(self.level*7), int(self.level*5))
        self.defense = 3 + level
        self.evasiveness = level
        self.speed = round(1*level, 1)
        self.lootChance = (level+3)//2
        self.xp = randint(int(level*15), int(level*20))


class Demon(Enemy):
    def __init__(self, name="Demon", level=1):
        super().__init__(name, level, 0)
        self.totalHealth = randint(int(self.level*15), int(self.level*25))
        self.currentHealth = self.totalHealth
        self.damage = randint(int(self.level*7), int(self.level*5))
        self.defense = 4 + level
        self.evasiveness = level
        self.speed = round(1*level, 1)
        self.lootChance = (level+3)//2
        self.xp = randint(int(level*15), int(level*20))
