from tkinter import *
from tkinter import font
from ..Towns import Towns, Shops
from .GUIIndexes import *

class TownScreen(Tk):
    def __init__(self, game):
        Tk.__init__(self)
        self.game = game
        self.town = game.getCurrentTown()
        self.geometry('%dx%d+%d+%d' % self.game.guiHandler.windowInfo)
        self.minsize(1000, 600)
        self.wm_title("{}".format(self.town.name))
        self.titleFont = font.Font(family="Comic Sans MS", size=35, weight=font.BOLD)
        self.nameFont = font.Font(family="Comic Sans MS", size = 24, weight=font.BOLD)
        self.generalFont = font.Font(family="Comic Sans MS", size=18)

        self.bind("<Key>", self.game.save)

        self.addPlayerInformationPanel()
        self.shopLabel()
        self.addTitleBar()

        self.addCanvas()

        #DEBUG ONLY REMOVE LATER
        #self.bind("<Key>", self.newTown)

        self.addButtons()

        self.configureGrid()
        self.drawShops()


    def addTitleBar(self):
        self.titleBar = Frame()

        self.titleLabel = Label(self.titleBar, text=self.town.name, font=self.titleFont, anchor=W)
        self.titleLabel.grid(row=0, column=0, sticky="NWS")

        self.nextTownButton = Button(self.titleBar, text="Next Town", font=self.generalFont, command=self.nextTown)
        self.previousTownButton = Button(self.titleBar, text="Prev. Town", font=self.generalFont, command=self.prevTown)
        if(self.town.isDungeonDone):
            self.enterDungonenButton = Button(self.titleBar, text="New Dungeon", font=self.generalFont, command=self.generateDungeon)
            self.nextTownButton.config(state=NORMAL)
            self.previousTownButton.config(state=NORMAL)
        else:
            self.enterDungonenButton = Button(self.titleBar, text="Enter Dungeonn", font=self.generalFont, command=self.openDungeon)
            self.nextTownButton.config(state=DISABLED)
            self.previousTownButton.config(state=DISABLED)


        if(self.game.currentTown == 0):
            self.enterDungonenButton.grid(row=0, column=1, sticky="NEWS")
            self.nextTownButton.grid(row=0, column=2, sticky="NEWS")
            self.titleBar.grid_columnconfigure(0, weight=1, minsize=450)
            self.titleBar.grid_columnconfigure(1, weight=1)
            self.titleBar.grid_columnconfigure(2, weight=1)
        else:
            self.previousTownButton.grid(row=0, column=1, sticky="NEWS")
            self.enterDungonenButton.grid(row=0, column=2, sticky="NEWS")
            self.nextTownButton.grid(row=0, column=3, sticky="NEWS")
            self.titleBar.grid_columnconfigure(0, weight=3, minsize=500)
            self.titleBar.grid_columnconfigure(1, weight=1)
            self.titleBar.grid_columnconfigure(2, weight=1)
            self.titleBar.grid_columnconfigure(3, weight=1)

        self.titleBar.grid(row=0, column=0, columnspan=3, sticky="NWES")

    def prevTown(self):
        self.game.prevTown()
        self.town = self.game.getCurrentTown()
        self.wm_title("{}".format(self.town.name))
        self.addPlayerInformationPanel()
        self.shopLabel()
        self.addTitleBar()
        self.addCanvas()
        self.addButtons()
        self.drawShops()

    def nextTown(self):
        self.game.nextTown()
        self.town = self.game.getCurrentTown()
        self.wm_title("{}".format(self.town.name))
        self.addPlayerInformationPanel()
        self.shopLabel()
        self.addTitleBar()
        self.addCanvas()
        self.addButtons()
        self.drawShops()

    def generateDungeon(self):
        self.town.newDungeon()
        self.addTitleBar()

    def openDungeon(self):
        self.game.guiHandler.swapGUI(DUNGEON_SCREEN)


    def addButtons(self):
        self.inventoryButton = Button(text="Inventory", font=self.generalFont, command=self.openInventory)
        self.inventoryButton.grid(row=2, column=0, sticky="NEWS")


    def openInventory(self):
        self.game.guiHandler.swapGUI(PLAYER_INVENTORY)


    def addPlayerInformationPanel(self):
        self.game.guiHandler.addPlayerInfo(self)
        self.playerInfo.grid(row=1, column=0, rowspan=1, columnspan=1, sticky="NEW")


    def shopOptions(self, event):
        hitShop = False
        for shop in self.town.shops:
            if(event.x in range(shop.x1, shop.x2) and event.y in range(shop.y1, shop.y2)):
                self.currentShopName.set(shop.shopName)
                self.town.index = self.town.shops.index(shop)
                self.currentShop = shop
                self.showShop()
                hitShop = True
        if(hitShop == False):
            self.hideShop()


    def showShop(self):
        shopCls = self.currentShop.__class__
        if(issubclass(shopCls, Shops.Store)):
            self.currentShopUse.set("Enter")
            self.doesPlayerHaveMoney(-1)
        elif(issubclass(shopCls, Shops.Inn)):
            self.currentShopUse.set("Sleep for {}".format(self.currentShop.cost))
            self.doesPlayerHaveMoney(self.currentShop.cost, True)
            if(self.game.player.currentHealth == self.game.player.totalHealth and self.game.player.currentActionPoints == self.game.player.totalActionPoints):
                self.enterButton.config(state=DISABLED)
        elif(issubclass(shopCls, Shops.Healer)):
            self.currentShop.updateValues()
            self.currentShopUse.set("Heal {}hp for {}".format(self.currentShop.pointsToHeal, self.currentShop.totalCost))
            self.doesPlayerHaveMoney(self.currentShop.totalCost, True)
        elif(issubclass(shopCls, Shops.Blacksmith)):
            self.currentShopUse.set("Enter")
            self.doesPlayerHaveMoney(-1)
        elif(issubclass(shopCls, Shops.Challenge)):
            self.currentShopUse.set("Enter")
            self.doesPlayerHaveMoney(-1)

        self.shopName.grid(row=2, column=1, rowspan=1, sticky="NSEW")
        self.enterButton.grid(row=2, column=2, rowspan=1, sticky="NWSE")


    def useShop(self):
        shopCls = self.currentShop.__class__
        if(issubclass(shopCls, Shops.Store)):
            self.game.guiHandler.swapGUI(STORE_SCREEN)
        elif(issubclass(shopCls, Shops.Inn) or issubclass(shopCls, Shops.Healer)):
            self.currentShop.serve()
            self.showShop()
            self.addPlayerInformationPanel()
        elif(issubclass(shopCls, Shops.Blacksmith)):
            self.game.guiHandler.swapGUI(BLACKSMITH_SCREEN)
        elif(issubclass(shopCls, Shops.Challenge)):
            self.game.guiHandler.swapGUI(CHALLENGE_SCREEN)


    def doesPlayerHaveMoney(self, cost, gold=False):
        if(self.game.player.money < cost):
            self.enterButton.config(state=DISABLED)
        elif(cost == 0):
            self.enterButton.config(state=DISABLED)
        else:
            self.enterButton.config(state=NORMAL)

        if(gold):
            self.enterButton.config(image=self.coin, compound=RIGHT)
        else:
            self.enterButton.config(image="", compound=NONE)


    def hideShop(self):
        self.shopName.grid_forget()
        for i in range(2):
            self.enterButton.grid_forget()


    def shopLabel(self):
        self.currentShopName = StringVar()
        self.currentShopUse = StringVar()
        self.shopName = Label(textvariable=self.currentShopName, font=self.generalFont)
        self.enterButton = Button(textvariable=self.currentShopUse, relief=GROOVE, font=self.generalFont, width=10, command=self.useShop)


    def addCanvas(self):
        self.townMap = Canvas(width=500, height=500, relief=RAISED, bd=4, bg="white")
        self.townMap.bind("<Button-1>", self.shopOptions)
        self.townMap.grid(row=1, column=1, rowspan=1, columnspan=2, sticky="NEW")


    def drawShops(self):
        self.update()
        self.townMap.delete("all")
        if(not self.town.hasBeenSet):
            try:
                self.town.setTownRectangles(self.townMap.winfo_height(), self.townMap.winfo_width())
            except IndexError:
                print("SHOP PLACING ERROR")
                self.town.hasBeenSet = False
                self.drawShops()
        for shop in self.town.shops:
            self.townMap.create_rectangle(shop.x1, shop.y1, shop.x2, shop.y2)


    def configureGrid(self):
        for i in range(3):
            self.grid_columnconfigure(i, weight=1)

        self.grid_columnconfigure(1, minsize=300)
        self.grid_columnconfigure(2, minsize=300)

        for j in range(3):
            self.grid_rowconfigure(j, weight=1)

        self.grid_rowconfigure(0, minsize=70)
        self.grid_rowconfigure(2, minsize=50)
