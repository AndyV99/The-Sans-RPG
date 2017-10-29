from tkinter import *
from tkinter import font
from ..Items import Inventory, Items
from ..Items.Armor import Armor


class PlayerInventory(Tk):
    def __init__(self, game):
        Tk.__init__(self)
        self.game = game

        self.wm_title("{}\n's Inventory".format(game.player.name))
        self.geometry('%dx%d+%d+%d' % self.game.guiHandler.windowInfo)
        self.minsize(1000, 600)

        self.bind("<Key>", self.game.save)

        self.nameFont = font.Font(family="Comic Sans MS", size = 28, weight=font.BOLD)
        self.generalFont = font.Font(family="Comic Sans MS", size=18)
        self.smallerFont = font.Font(family="Comic Sans MS", size=16)
        self.inventoryFont = font.Font(family="Comic Sans MS", size=11)
        self.buttonSize = 80

        self.createAllContent()

        self.updateInfo()
        self.updateInventory()
        self.updateEquipment()

        self.playerInventory.grid(row=0, column=1, sticky="NSEW")
        self.playerInfo.grid(row=0, column=0, rowspan=2, sticky="NSEW")
        self.playerEquipment.grid(row=2, column=1, sticky="NEWS")

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1, minsize=80)
        self.grid_rowconfigure(3, weight=1)
        self.grid_columnconfigure(0, weight=1, minsize=300)
        self.grid_columnconfigure(1, weight=1, minsize=300)
        self.grid_columnconfigure(2, weight=1, minsize=200)


    def createAllContent(self):
        self.currentItem = Inventory.Empty
        self.currentIndex = IntVar()
        self.currentIndex.set(-1)

        self.playerInventory = Frame()
        self.playerEquipment = Frame()

        self.itemInfoFrame = Frame()
        self.itemName = Label(self.itemInfoFrame, text="", font=self.generalFont, wraplength=200, width=12)
        self.itemName.grid(row=0, column=0, columnspan=2, sticky="NE")

        self.statLabelVar = StringVar()
        self.statLabels = Label(self.itemInfoFrame, textvariable=self.statLabelVar, font=self.smallerFont, anchor=NW, justify=LEFT)
        self.statLabels.grid(row=1, column=0, sticky="NW")

        self.statAmountVar = StringVar()
        self.statAmounts = Label(self.itemInfoFrame, textvariable=self.statAmountVar, font=self.smallerFont, anchor=NW, justify=LEFT)
        self.statAmounts.grid(row=1, column=1, sticky="NE")

        self.useText = StringVar()
        self.useButton = Button(self.itemInfoFrame, textvariable=self.useText, font=self.generalFont)
        self.useButton.grid(row=2, columnspan=2, sticky="EW")

        self.backButton = Button(text="Back", font=self.generalFont, command=self.back)
        self.backButton.grid(row=2, column=0, sticky="NEWS")


    def updateInventory(self):
        images = []
        self.playerInventoryButtons = []

        for slot in self.game.player.inventory.slots:
            images.append(PhotoImage(file=slot.item.image).subsample(2, 2))

        for i in range(len(images)):
            slot = self.game.player.inventory.slots[i]
            item = slot.item
            if("Empty" in item.name):
                self.playerInventoryButtons.append(Radiobutton(self.playerInventory, text="x{}".format(slot.quantity), image=images[i], compound=LEFT, font=self.inventoryFont, indicatoron=0, relief=GROOVE, height=self.buttonSize, width=self.buttonSize+5, state=DISABLED))
                self.playerInventoryButtons[i].config(state=DISABLED)
            else:
                self.playerInventoryButtons.append(Radiobutton(self.playerInventory, text="x{}".format(slot.quantity), image=images[i], compound=LEFT, font=self.inventoryFont, indicatoron=0, relief=GROOVE, variable=self.currentIndex, value=i, height=self.buttonSize, width=self.buttonSize+5, command=self.updateItem))

            self.playerInventoryButtons[i].image = images[i]

        for i in range(len(self.playerInventoryButtons)):
            self.playerInventoryButtons[i].grid(row=0+(i//4), column=0+(i%4), sticky="")

        for j in range(4):
            self.playerInventory.grid_rowconfigure(j, weight=1, minsize=80)

        for k in range(3):
            self.playerInventory.grid_columnconfigure(k, weight=1, minsize=80)


    def updateEquipment(self):
        images = []
        self.playerEquipmentButtons = []

        for slot in self.game.player.equipment.slots:
            images.append(PhotoImage(file=slot.item.image).subsample(2, 2))

        for i in range(len(images)):
            slot = self.game.player.equipment.slots[i]
            item = slot.item
            if("Empty" in item.name or item.name == "Fist"):
                self.playerEquipmentButtons.append(Radiobutton(self.playerEquipment,  image=images[i], font=self.inventoryFont, indicatoron=0, relief=FLAT, height=self.buttonSize, width=self.buttonSize, state=DISABLED))
            else:
                self.playerEquipmentButtons.append(Radiobutton(self.playerEquipment, image=images[i], font=self.inventoryFont, indicatoron=0, relief=FLAT, variable=self.currentIndex, value=i+20, height=self.buttonSize, width=self.buttonSize, command=self.updateItem))

            self.playerEquipmentButtons[i].image = images[i]

            for i in range(len(self.playerEquipmentButtons)):
                self.playerEquipmentButtons[i].grid(row=0, column=(i%4), sticky="")

            for j in range(1):
                self.playerEquipment.grid_rowconfigure(j, weight=1)

            for k in range(3):
                self.playerEquipment.grid_columnconfigure(k, weight=1, minsize=85)


    def updateItem(self):
        direction = 0
        if(self.currentIndex.get() < 20 and self.currentIndex.get() >= 0):
            direction = 1
            self.currentItem = self.game.player.inventory.slots[self.currentIndex.get()].item
        elif(self.currentIndex.get() >= 20):
            direction = -1
            self.currentItem = self.game.player.equipment.slots[self.currentIndex.get()-20].item

        self.itemInfoFrame.grid(row=0, column=2, columnspan=1, rowspan=3, sticky="NEWS")
        self.itemName.config(text=self.currentItem.name)
        item = self.currentItem
        itemClass = item.__class__

        if("Empty" in item.name):
            self.itemInfoFrame.grid_forget()
        else:
            if(issubclass(itemClass, Items.Weapon)):
                if(direction==1):
                    self.useText.set("Equip")
                    if(not "Fist" in self.game.player.equipment.slots[0].item.name):
                        self.useButton.config(state=DISABLED)
                    else:
                        self.useButton.config(state=NORMAL)
                else:
                    self.useButton.config(state=NORMAL)
                    self.useText.set("Unequip")

                self.useButton.config(command=lambda : self.equip(direction))
                self.statLabelVar.set("Damage:\nAP Cost: \nSTR Buff: \nAGI Buff: \nINT Buff: \nWeight: \nValue: ")
                self.statAmountVar.set(("{}\n"*7).format(item.getDamageForLabel(self.game.player), item.actionPointCost, item.strBuff, item.agiBuff, item.intBuff, round(item.weight, 1), item.value))
            elif(issubclass(itemClass, Items.Armor)):
                if(direction==1):
                    self.useText.set("Equip")
                    if(issubclass(itemClass, Armor.HeadArmor) and not "Empty" in self.game.player.equipment.slots[1].item.name):
                        self.useButton.config(state=DISABLED)
                    elif(issubclass(itemClass, Armor.TorsoArmor) and not "Empty" in self.game.player.equipment.slots[2].item.name):
                        self.useButton.config(state=DISABLED)
                    elif(issubclass(itemClass, Armor.LegArmor) and not "Empty" in self.game.player.equipment.slots[3].item.name):
                        self.useButton.config(state=DISABLED)
                    else:
                        self.useButton.config(state=NORMAL)
                else:
                    self.useButton.config(state=NORMAL)
                    self.useText.set("Unequip")

                self.useButton.config(command=lambda : self.equip(direction))
                self.statLabelVar.set("Defense:\nHP:\nAP:\nHP Regen:\nAP Regen:\nSTR Buff:\nAGI Buff:\nINT Buff:\nWeight:\nValue:")
                self.statAmountVar.set(("{}\n"*10).format(item.defense, item.healthBuff, item.actionPointBuff, item.healthRegenBuff, item.actionPointRegenBuff, item.strBuff, item.agiBuff, item.intBuff, round(item.weight, 1), item.value))
            elif(issubclass(self.currentItem.__class__, Items.Food)):
                self.useText.set("Eat")
                self.useButton.config(command=self.eat)
                self.statLabelVar.set("Heal:\nUses:\nWeight:\nValue:")
                self.statAmountVar.set(("{}\n"*4).format(item.healValue, item.usesLeft, round(item.weight, 1), item.value))


    def updateInfo(self):
        self.game.guiHandler.addPlayerInfo(self)
        self.playerInfo.grid(row=0, column=0, rowspan=2, sticky="NSEW")
        self.backButton.grid(row=2, column=0, sticky="NEWS")


    def equip(self, direction):
        if(direction == 1):
            self.game.player.equipItem(self.currentItem)
            self.updateInventory()
            self.updateEquipment()
            self.updateItem()
            self.updateInfo()
        elif(direction == -1):
            self.game.player.unequipItem(self.currentItem)
            self.updateInventory()
            self.updateEquipment()
            self.updateItem()
            self.updateInfo()


    def eat(self):
        self.game.player.eat(self.currentItem)
        self.updateInventory()
        self.updateItem()
        self.updateInfo()


    def back(self):
        self.game.guiHandler.back()
