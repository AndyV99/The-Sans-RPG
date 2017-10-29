from tkinter import *
from tkinter import font
from ...Items import Items, Inventory, Tiers
from ... import ArtHandler
from ..GUIIndexes import *

class StoreScreen(Tk):
    def __init__(self, game):
        Tk.__init__(self)
        self.game = game
        self.shop = self.game.getCurrentTown().shops[game.getCurrentTown().index]
        self.wm_title(self.shop.shopName)
        self.geometry('%dx%d+%d+%d' % self.game.guiHandler.windowInfo)
        self.minsize(1000, 600)
        self.titleFont = font.Font(family="Comic Sans MS", size=35, weight=font.BOLD)
        self.generalFont = font.Font(family="Comic Sans MS", size=20)
        self.smallerFont = font.Font(family="Comic Sans MS", size=14)
        self.inventoryFont = font.Font(family="Comic Sans MS", size=11)

        self.bind("<Key>", self.game.save)

        self.coinImage = PhotoImage(file=ArtHandler.Coin).subsample(5, 5)

        self.buttonSize = 80

        self.currentIndex = IntVar()
        self.currentItem = Inventory.Empty

        self.createAllContent()

        self.addPlayerInventory()
        self.addShopInventory()

        self.addBackButton()

        self.organizeGrid()


    def addBackButton(self):
        self.backButton = Button(text="Back to Town", font=self.generalFont, command=self.back)


    def back(self):
        self.game.guiHandler.back()


    def addPlayerInventory(self):
        images = []
        self.playerLabel = Label(text="{}\'s Inventory".format(self.game.player.name), font=self.generalFont)
        self.playerLabel.grid(row=0, columnspan=3, sticky=NW)

        self.playerMoney.set(self.game.player.money)
        self.moneyLabel = Label(image=self.coinImage, compound=RIGHT, textvariable=self.playerMoney, font=self.generalFont, anchor=E)
        self.moneyLabel.grid(row=0, column=3, sticky=NE)
        self.playerInventoryButtons = []

        for slot in self.game.player.inventory.slots:
            images.append(PhotoImage(file=slot.item.image).subsample(2, 2))

        for i in range(len(images)):
            slot = self.game.player.inventory.slots[i]
            item = slot.item
            if("Empty" in item.name):
                self.playerInventoryButtons.append(Radiobutton(text="x{}".format(slot.quantity), image=images[i], compound=LEFT, font=self.inventoryFont, indicatoron=0, relief=GROOVE, height=self.buttonSize, width=self.buttonSize+5, state=DISABLED))
            else:
                self.playerInventoryButtons.append(Radiobutton(text="x{}".format(slot.quantity), image=images[i], compound=LEFT, font=self.inventoryFont, indicatoron=0, relief=GROOVE, variable=self.currentIndex, value=i, height=self.buttonSize, width=self.buttonSize+5, command=self.updateItem))

            self.playerInventoryButtons[i].image = images[i]

        for i in range(len(self.playerInventoryButtons)):
            self.playerInventoryButtons[i].grid(row=1+(i//4), column=0+(i%4), sticky=NSEW)


    def addShopInventory(self):
        images = []
        self.shopLabel = Label(text="{}\'s Inventory".format(self.shop.vendorName), font=self.generalFont)
        self.shopLabel.grid(row=0, column=7, columnspan=3, sticky=NE)

        self.shopMoneyLabel = Label(image=self.coinImage, compound=RIGHT, text="{} ".format(self.shop.money), font=self.generalFont)
        self.shopMoneyLabel.grid(row=0, column=6, sticky=NW)
        self.shopInventoryButtons = []

        for slot in self.shop.inventory.slots:
            images.append(PhotoImage(file=slot.item.image).subsample(2, 2))

        for i in range(len(images)):
            slot = self.shop.inventory.slots[i]
            item = slot.item
            if("Empty" in item.name):
                self.shopInventoryButtons.append(Radiobutton(text="x{}".format(slot.quantity), image=images[i], indicatoron=0, relief=GROOVE, font=self.inventoryFont, compound=LEFT, height=self.buttonSize, width=self.buttonSize+5, state=DISABLED))
            else:
                self.shopInventoryButtons.append(Radiobutton(text="x{}".format(slot.quantity), image=images[i], indicatoron=0, relief=GROOVE, font=self.inventoryFont, compound=LEFT, variable=self.currentIndex, value=i+20, height=self.buttonSize, width=self.buttonSize+5, command=self.updateItem))

            self.shopInventoryButtons[i].image = images[i]

        for i in range(len(self.shopInventoryButtons)):
            self.shopInventoryButtons[i].grid(row=1+(i//4), column=6+(i%4), sticky="NSEW")


    def createAllContent(self):
        self.playerMoney = IntVar()
        self.playerMoney.set(self.game.player.money)

        self.buyText = StringVar()
        self.buyText.set("Buy x{} for {}")

        self.sellText = StringVar()
        self.sellText.set("Sell x{} for {}")


        self.infoFrame = Frame()

        self.cIName = StringVar()
        self.itemLabel = Label(self.infoFrame, textvariable=self.cIName, font=self.generalFont, width=15, wraplength=200, justify=CENTER)
        self.itemLabel.grid(row=0, column=0, columnspan=2, rowspan=1, sticky="NSEW")

        self.statLabelVar = StringVar()
        self.statLabels = Label(self.infoFrame, textvariable=self.statLabelVar, font=self.smallerFont, anchor=NW, justify=LEFT)
        self.statLabels.grid(row=1, column=0, rowspan=1, sticky=NSEW)

        self.statAmountVar = StringVar()
        self.statAmounts = Label(self.infoFrame, textvariable=self.statAmountVar, font=self.smallerFont, anchor=NW, justify=LEFT)
        self.statAmounts.grid(row=1, column=1, rowspan=1, sticky=NSEW)


        self.exchangeFrame = Frame()

        #self.exchangeFrame.grid(row=5, column=4, columnspan=2, sticky="NSEW")

        for i in range(2):
            self.exchangeFrame.grid_columnconfigure(i, weight=1)

        self.exchangeFrame.grid_rowconfigure(0, weight=1)
        self.exchangeFrame.grid_rowconfigure(1, weight=2)


        self.sellButton = Button(self.exchangeFrame, image=self.coinImage, compound=RIGHT, textvariable=self.sellText, font=self.smallerFont, command=self.sell)
        self.buyButton = Button(self.exchangeFrame, image=self.coinImage, compound=RIGHT, textvariable=self.buyText, font=self.smallerFont, command=self.buy)


        self.plusSellButton = Button(self.exchangeFrame, text="+", font=self.smallerFont, command=lambda : self.changeSellAmount(1))
        self.minusSellButton = Button(self.exchangeFrame, text="-", font=self.smallerFont, command=lambda : self.changeSellAmount(-1))


        self.plusBuyButton = Button(self.exchangeFrame, text="+", font=self.smallerFont, command=lambda : self.changeBuyAmount(1))
        self.minusBuyButton = Button(self.exchangeFrame, text="-", font=self.smallerFont, command=lambda : self.changeBuyAmount(-1))


    def updateItem(self):
        self.sellAmount = 1
        self.buyAmount = 1


        if(self.currentIndex.get() < 20 and self.currentIndex.get() >= 0):
            self.buyButton.grid_forget()
            self.plusBuyButton.grid_forget()
            self.minusBuyButton.grid_forget()

            self.currentItem = self.game.player.inventory.slots[self.currentIndex.get()].item
            self.sellButton.grid(row=1, column=0, columnspan=2, rowspan=2, sticky="NSEW")

            if(self.currentItem.stackable):
                self.plusSellButton.grid(row=0, column=1, sticky="NSEW")
                self.minusSellButton.grid(row=0, column=0, sticky="NSEW")
                self.sellButton.grid(rowspan=1)

            self.updateSellButtons()

        elif(self.currentIndex.get() >= 20):
            self.sellButton.grid_forget()
            self.plusSellButton.grid_forget()
            self.minusSellButton.grid_forget()

            self.currentItem = self.shop.inventory.slots[self.currentIndex.get()-20].item
            self.buyButton.grid(row=1, column=0, columnspan=2, rowspan=2, sticky="SNEW")

            if(self.currentItem.stackable):
                self.plusBuyButton.grid(row=0, column=1, sticky="NSEW")
                self.minusBuyButton.grid(row=0, column=0, sticky="NSEW")
                self.buyButton.grid(rowspan=1)

            self.updateBuyButtons()

        if(issubclass(self.currentItem.__class__, Items.Weapon)):
            self.showWeaponInfo()
        elif(issubclass(self.currentItem.__class__, Items.Armor)):
            self.showArmorInfo()
        elif(issubclass(self.currentItem.__class__, Items.Food)):
            self.showFoodInfo()

        if(self.currentItem.name != "Empty"):
            self.cIName.set(self.currentItem.name)
            self.infoFrame.grid(row=1, column=4, columnspan=2, rowspan=5, sticky="NSEW")
            self.exchangeFrame.grid(row=5, column=4, columnspan=2, sticky="NSEW")


    def updateBuyButtons(self):
        currentItemValue = self.currentItem.value
        if(self.buyAmount == 1 and self.currentItem.stackable):
            self.minusBuyButton.config(state=DISABLED)
        elif(self.buyAmount != 1 and self.currentItem.stackable):
            self.minusBuyButton.config(state=NORMAL)
        if(self.currentItem.stackable and (self.buyAmount+1)*self.currentItem.value > self.game.player.money or self.buyAmount == self.shop.inventory.slots[self.shop.inventory.indexOf(self.currentItem)].quantity):
            self.plusBuyButton.config(state=DISABLED)
        elif(self.currentItem.stackable):
            self.plusBuyButton.config(state=NORMAL)
        if(self.buyAmount*self.currentItem.value > self.game.player.money):
            self.buyButton.config(state=DISABLED)
        else:
            self.buyButton.config(state=NORMAL)
        if(self.currentItem.stackable):
            self.buyText.set("Buy x{} for {}".format(self.buyAmount, self.buyAmount*self.currentItem.value))
        else:
            self.plusBuyButton.grid_forget()
            self.minusBuyButton.grid_forget()
            self.buyText.set("Buy for {}".format(self.currentItem.value))


    def updateSellButtons(self):
        if(self.sellAmount == 1 and self.currentItem.stackable):
            self.minusSellButton.config(state=DISABLED)
        elif(self.sellAmount != 1 and self.currentItem.stackable):
            self.minusSellButton.config(state=NORMAL)

        if(self.currentItem.stackable and (self.sellAmount+1)*self.currentItem.value > self.shop.money or self.sellAmount == self.game.player.inventory.slots[self.game.player.inventory.indexOf(self.currentItem)].quantity):
            self.plusSellButton.config(state=DISABLED)
        else:
            self.plusSellButton.config(state=NORMAL)

        if(self.sellAmount*self.currentItem.value//2 > self.shop.money):
            self.sellButton.config(state=DISABLED)
        else:
            self.sellButton.config(state=NORMAL)

        if(self.currentItem.stackable):
            self.sellText.set("Sell x{} for {}".format(self.sellAmount, self.sellAmount*self.currentItem.value//2))
        else:
            self.sellText.set("Sell for {}".format(self.currentItem.value//2))


    def changeBuyAmount(self, amount):
        self.buyAmount += amount
        self.updateBuyButtons()

    def changeSellAmount(self, amount):
        self.sellAmount += amount
        self.updateSellButtons()


    def showWeaponInfo(self):
        weapon = self.currentItem
        self.buyText.set("Buy for {}".format(weapon.value))
        self.sellText.set("Sell for {}".format(weapon.value//2))
        self.statLabelVar.set("Damage:\nAP Cost: \nSTR Buff: \nAGI Buff: \nINT Buff: \nWeight: \nValue: ")
        self.statAmountVar.set(("{}\n"*7).format(weapon.getDamageForLabel(self.game.player), weapon.actionPointCost, weapon.strBuff, weapon.agiBuff, weapon.intBuff, round(weapon.weight, 1), weapon.value))


    def showArmorInfo(self):
        a = self.currentItem
        self.buyText.set("Buy for {}".format(a.value))
        self.sellText.set("Sell for {}".format(a.value//2))
        self.statLabelVar.set("Defense:\nHP:\nAP:\nHP Regen:\nAP Regen:\nSTR Buff:\nAGI Buff:\nINT Buff:\nWeight:\nValue:")
        self.statAmountVar.set(("{}\n"*10).format(a.defense, a.healthBuff, a.actionPointBuff, a.healthRegenBuff, a.actionPointRegenBuff, a.strBuff, a.agiBuff, a.intBuff, round(a.weight, 1), a.value))


    def showFoodInfo(self):
        f = self.currentItem
        self.buyText.set("Buy x{} for {}".format(self.buyAmount, f.value))
        self.sellText.set("Sell x{} for {}".format(self.sellAmount, f.value//2))
        self.statLabelVar.set("Heal:\nUses:\nWeight:\nValue:")
        self.statAmountVar.set(("{}\n"*4).format(f.healValue, f.usesLeft, round(f.weight, 1), f.value))


    def buy(self):
        self.shop.sellToPlayer(self.currentItem, self.buyAmount)
        self.addPlayerInventory()
        self.addShopInventory()

        if((self.currentItem in self.shop.inventory.getItems())):
            self.currentIndex.set(self.shop.inventory.indexOf(self.currentItem)+20)
            self.updateBuyButtons()
        else:
            self.currentItem = Inventory.Empty
            self.currentIndex.set(-1)
            self.infoFrame.grid_forget()
            self.exchangeFrame.grid_forget()
        self.updateItem()

    def sell(self):
        self.shop.buyFromPlayer(self.currentItem, self.sellAmount)
        self.addPlayerInventory()
        self.addShopInventory()
        if(self.currentItem in self.game.player.inventory.getItems()):
            self.currentIndex.set(self.game.player.inventory.indexOf(self.currentItem))
            self.updateSellButtons()
        else:
            self.currentItem = Inventory.Empty
            self.currentIndex.set(-1)
            self.infoFrame.grid_forget()
            self.exchangeFrame.grid_forget()
        self.updateItem()

    def organizeGrid(self):
        self.backButton.grid(row=0, column=4, columnspan=2, sticky=NSEW)

        for i in range(10):
            self.grid_columnconfigure(i, weight=1)

        for j in range(6):
            self.grid_rowconfigure(j, weight=1)

        self.grid_columnconfigure(4, minsize=200)
