from . import Shops
from ..Dungeons.Dungeons import Dungeon
import random

TOWN_BEGINNINGS = ["Pitts", "Charles", "Neble", "James", "Browns", "Incenis", "Hostis", "Necrol", "Ritos", "West", "East", "Northern", "Nuxil", "Xynopl", "Anders", "Tikus", "Danos",
                                         "Hani", "Varis", "Banti", "Genis", "Opitus", "Racto", "Enus", "Eroti", "Andri", "Bisus", "Ionius", "Quiotl", "Kindol", "Cinus", "Coplis", "Danus", "Doinus", "Daxul", "Faxor",
                                         "Finos", "Faro", "Ganto", "Garis", "Jank", "Jixno", "Jerius", "Gallus", "Ginni"]
TOWN_ENDS = ["burg", "opolis", "boro", "ville", "town", "ton"]


class Town(object):
    def __init__(self, name="Genisburg", index=0, shops=[], game=0, level=1):
        self.name = random.choice(TOWN_BEGINNINGS) + random.choice(TOWN_ENDS)
        self.index = index
        self.shops = []
        self.game = game
        self.level = level
        self.generateShops()
        self.hasBeenSet = False
        self.isDungeonDone = False


    def generateShops(self):
        SHOPS = [shop for sub in Shops.Shop.__subclasses__() for shop in sub.__subclasses__()]*2
        shops = random.randint(3, 7)
        self.shops.append(Shops.GeneralStore(game=self.game, level=self.level))
        shops -= 1
        self.shops.append(Shops.Inn(game=self.game, level=self.level))
        shops -= 1
        if(len(Shops.SHOP_KEEPER_NAMES) < shops):
            Shops.resetKeeperNames()
        for i in range(shops):
            newShop = random.choice(SHOPS)
            self.shops.append(newShop(game=self.game))
            SHOPS.remove(newShop)


    def setTownRectangles(self, height, width):
        self.hasBeenSet = True
        possibleX = list(range(width))
        possibleX = possibleX[10:width-50]
        possibleY = list(range(height))
        possibleY = possibleY[10:height-50]
        for shop in self.shops:
            x1 = random.choice(possibleX)
            y1 = random.choice(possibleY)
            localWidth = random.randint(25, 45)
            localHeight = random.randint(25, 45)
            shop.setRectangle(rect=[x1, y1, localWidth, localHeight])
            for boxX in range(x1-46, x1+localWidth):
                if(boxX in possibleX):
                    possibleX.remove(boxX)
            for boxY in range(y1-46, y1+localHeight):
                if(boxY in possibleY):
                    possibleY.remove(boxY)


    def newDungeon(self):
        self.isDungeonDone = False
        self.dungeon = Dungeon(self.game, self.level)
