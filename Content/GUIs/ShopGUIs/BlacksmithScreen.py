from tkinter import *
from tkinter import font
from ...Items import Inventory, Items
from ... import ArtHandler

class BlacksmithScreen(Tk):
    def __init__(self, game):
        Tk.__init__(self)
        self.game = game
        self.shop = game.getCurrentTown().shops[game.getCurrentTown().index]

        self.geometry('%dx%d+%d+%d' % self.game.guiHandler.windowInfo)
        self.minsize(1000, 600)
        self.wm_title("{}".format(self.shop.shopName))

        self.bind("<Key>", self.game.save)

        self.generalFont = font.Font(family="Comic Sans MS", size=20)
        self.smallerFont = font.Font(family="Comic Sans MS", size=14)
        self.inventoryFont = font.Font(family="Comic Sans MS", size=11)

        self.coinImage = PhotoImage(file=ArtHandler.Coin).subsample(5, 5)

        self.buttonSize = 80
        self.playerMoney = IntVar()

        self.currentItem = Inventory.Empty
        self.currentIndex = IntVar()
        self.currentIndex.set(-1)

        self.playerInventoryFrame = Frame()

        self.addItemInfo()

        self.modifierAmount = IntVar()
        self.modifierAmount.set(1)

        self.updatePlayerInventory()
        self.updateBlacksmith()
        self.updateItem()

        self.addBackButton()

        self.configureGrid()


    def addItemInfo(self):
        self.itemInfoFrame = Frame()
        self.itemName = Label(self.itemInfoFrame, text="", font=self.generalFont, wraplength=200, width=12)
        self.itemName.grid(row=0, column=0, columnspan=2, sticky="NEWS")

        self.statLabelVar = StringVar()
        self.statLabels = Label(self.itemInfoFrame, textvariable=self.statLabelVar, font=self.smallerFont, anchor=NW, justify=LEFT)
        self.statLabels.grid(row=1, column=0, sticky="NEWS")

        self.statAmountVar = StringVar()
        self.statAmounts = Label(self.itemInfoFrame, textvariable=self.statAmountVar, font=self.smallerFont, anchor=NW, justify=LEFT)
        self.statAmounts.grid(row=1, column=1, sticky="NEWS")

        self.giveButton = Button(self.itemInfoFrame, text="Give", font=self.generalFont, command=self.give)
        self.giveButton.grid(row=2, column=0, columnspan=2, sticky="NEWS")

        self.takeButton = Button(self.itemInfoFrame, text="Take", font=self.generalFont, command=self.take)
        self.takeButton.grid(row=2, column=0, columnspan=2, sticky="NEWS")

        self.itemInfoFrame.grid(row=0, column=1, sticky="NEWS")


    def take(self):
        self.game.player.inventory.addItem(self.currentItem)
        self.shop.slot.removeItem(self.currentItem)
        self.currentIndex.set(-1)
        self.updatePlayerInventory()
        self.updateBlacksmith()
        self.updateItem()

    def give(self):
        self.game.player.inventory.removeItem(self.currentItem)
        self.shop.slot.addItem(self.currentItem)
        self.currentIndex.set(-1)
        self.updatePlayerInventory()
        self.updateBlacksmith()
        self.updateItem()


    def updateItem(self):
        if(self.currentIndex.get() < 20 and self.currentIndex.get() >= 0):
            self.takeButton.grid_forget()
            self.giveButton.grid(row=2, column=0, columnspan=2, sticky="NEWS")
            self.currentItem = self.game.player.inventory.slots[self.currentIndex.get()].item
        elif(self.currentIndex.get() == 20):
            self.giveButton.grid_forget()
            self.takeButton.grid(row=2, column=0, columnspan=2, sticky="NEWS")
            self.currentItem = self.shop.slot.slots[0].item


        self.itemInfoFrame.grid(row=0, column=1, sticky="NEWS")
        self.itemName.config(text=self.currentItem.name)
        item = self.currentItem

        if("Empty" in item.name or self.currentIndex.get() == -1):
            self.itemInfoFrame.grid_forget()
        else:
            if(issubclass(self.currentItem.__class__, Items.Weapon)):
                self.statLabelVar.set("Damage:\nAP Cost: \nSTR Buff: \nAGI Buff: \nINT Buff: \nWeight: \nValue: ")
                self.statAmountVar.set(("{}\n"*7).format(item.getDamageForLabel(self.game.player), item.actionPointCost, item.strBuff, item.agiBuff, item.intBuff, round(item.weight, 1), item.value))
                self.giveButton.grid(row=2, column=0, columnspan=2, sticky="NEWS")
            elif(issubclass(self.currentItem.__class__, Items.Armor)):
                self.statLabelVar.set("Defense:\nHP:\nAP:\nHP Regen:\nAP Regen:\nSTR Buff:\nAGI Buff:\nINT Buff:\nWeight:\nValue:")
                self.statAmountVar.set(("{}\n"*10).format(item.defense, item.healthBuff, item.actionPointBuff, item.healthRegenBuff, item.actionPointRegenBuff, item.strBuff, item.agiBuff, item.intBuff, round(item.weight, 1), item.value))
                self.giveButton.grid(row=2, column=0, columnspan=2, sticky="NEWS")


    def updatePlayerInventory(self):
        self.playerLabel = Label(self.playerInventoryFrame, text="{}\'s Inventory".format(self.game.player.name), font=self.generalFont)
        self.playerLabel.grid(row=0, columnspan=3, sticky=NW)

        self.playerMoney.set(self.game.player.money)
        self.moneyLabel = Label(self.playerInventoryFrame, image=self.coinImage, compound=RIGHT, textvariable=self.playerMoney, font=self.generalFont, anchor=E)
        self.moneyLabel.grid(row=0, column=3, sticky=NE)
        images = []
        self.playerInventoryButtons = []

        for slot in self.game.player.inventory.slots:
            images.append(PhotoImage(file=slot.item.image).subsample(2, 2))

        for i in range(len(images)):
            slot = self.game.player.inventory.slots[i]
            item = slot.item
            if("Empty" in item.name or issubclass(item.__class__, Items.Food)):
                self.playerInventoryButtons.append(Radiobutton(self.playerInventoryFrame, text="x{}".format(slot.quantity), image=images[i], compound=LEFT, font=self.inventoryFont, indicatoron=0, relief=GROOVE, height=self.buttonSize, width=self.buttonSize+5, state=DISABLED))
            else:
                self.playerInventoryButtons.append(Radiobutton(self.playerInventoryFrame, text="x{}".format(slot.quantity), image=images[i], compound=LEFT, font=self.inventoryFont, indicatoron=0, relief=GROOVE, variable=self.currentIndex, value=i, height=self.buttonSize, width=self.buttonSize+5, command=self.updateItem))

            self.playerInventoryButtons[i].image = images[i]

        for i in range(len(self.playerInventoryButtons)):
            self.playerInventoryButtons[i].grid(row=1+(i//4), column=0+(i%4), sticky="")

        for j in range(4):
            self.playerInventoryFrame.grid_rowconfigure(j, weight=1, minsize=80)

        for k in range(3):
            self.playerInventoryFrame.grid_columnconfigure(k, weight=1, minsize=80)

        self.addBackButton()
        self.playerInventoryFrame.grid(row=0, column=0, sticky="NEWS")


    def updateBlacksmith(self):
        self.blacksmithFrame = Frame()
        slot = self.shop.slot.slots[0]
        item = slot.item
        image = PhotoImage(file=item.image).subsample(2, 2)
        if("Empty" in item.name):
            self.blacksmithSlot = Radiobutton(self.blacksmithFrame, image=image, compound=NONE, indicatoron=0, relief=GROOVE, height=self.buttonSize, width=self.buttonSize+5, state=DISABLED)
        else:
            self.blacksmithSlot = Radiobutton(self.blacksmithFrame, image=image, compound=NONE, indicatoron=0, relief=GROOVE, variable=self.currentIndex, value=20, height=self.buttonSize, width=self.buttonSize, command=self.updateItem)

        self.blacksmithSlot.image = image
        self.blacksmithSlot.grid(row=0, columnspan=3, sticky="")

        self.modifyButton = Button(self.blacksmithFrame, text="Modify", font=self.generalFont, command=self.modify, relief=GROOVE)
        self.modifyButton.grid(row=2, column=1, sticky="NS")

        self.minusModifierButton = Button(self.blacksmithFrame, text="-", font=self.generalFont, command=lambda : self.changeModifier(-1), relief=GROOVE)
        self.addModifierButton = Button(self.blacksmithFrame, text="+", font=self.generalFont, command=lambda : self.changeModifier(1), relief=GROOVE)
        self.modifierAmountLabel = Label(self.blacksmithFrame, textvariable=self.modifierAmount, font=self.generalFont)

        self.explanationLabel = Label(self.blacksmithFrame, image=self.coinImage, text="After pressing the button, the Blacksmith will attempt to modify your weapon {} times and it will cost you {} ".format(self.modifierAmount.get(), self.modifierAmount.get()*self.shop.cost), compound=RIGHT, wraplength=200, font=self.smallerFont)
        self.explanationLabel.grid(row=3, column=0, columnspan=3, sticky="NEWS")

        self.minusModifierButton.grid(row=1, column=0, sticky="NS")
        self.addModifierButton.grid(row=1, column=2, sticky="NS")
        self.modifierAmountLabel.grid(row=1, column=1, sticky="NEWS")

        self.blacksmithFrame.grid_columnconfigure(0, weight=1)
        self.blacksmithFrame.grid_columnconfigure(1, weight=1)
        self.blacksmithFrame.grid_columnconfigure(2, weight=1)

        self.blacksmithFrame.grid_rowconfigure(0, weight=1)
        self.blacksmithFrame.grid_rowconfigure(1, weight=1)
        self.blacksmithFrame.grid_rowconfigure(2, weight=1)
        self.blacksmithFrame.grid_rowconfigure(3, weight=1)

        self.blacksmithFrame.grid(row=0, column=2, sticky="NEWS")

        self.updateButtons()


    def modify(self):
        self.shop.chances = self.modifierAmount.get()
        self.shop.serve()
        self.updatePlayerInventory()
        self.updateBlacksmith()
        self.updateButtons()
        self.updateItem()


    def changeModifier(self, amount):
        self.modifierAmount.set(self.modifierAmount.get()+amount)
        self.updateButtons()


    def updateButtons(self):
        self.explanationLabel.config(text="After pressing the button, the Blacksmith will attempt to modify your weapon {} times and it will cost you {} ".format(self.modifierAmount.get(), self.modifierAmount.get()*self.shop.cost))
        if(self.modifierAmount.get()*self.shop.cost > self.game.player.money):
            self.modifyButton.config(state=DISABLED)
            self.addModifierButton.config(state=DISABLED)
        else:
            self.modifyButton.config(state=NORMAL)
            self.addModifierButton.config(state=NORMAL)
            self.modifierAmountLabel.config(state=NORMAL)
        if(self.modifierAmount.get() == 1):
            self.minusModifierButton.config(state=DISABLED)
        else:
            self.minusModifierButton.config(state=NORMAL)
        if((self.modifierAmount.get()+1)*self.shop.cost > self.game.player.money):
            self.addModifierButton.config(state=DISABLED)


    def configureGrid(self):
        for i in range(2):
            self.grid_columnconfigure(i, weight=1)

        self.grid_columnconfigure(1, minsize=200)
        self.grid_columnconfigure(2, minsize=400)

        for j in range(1):
            self.grid_rowconfigure(j, weight=1)


    def addBackButton(self):
        self.backButton = Button(self.playerInventoryFrame, text="Back", font=self.generalFont, command=self.back, width=5)
        self.backButton.grid(row=5, column=0, columnspan=4, sticky="NEWS")


    def back(self):
        self.game.guiHandler.back()
