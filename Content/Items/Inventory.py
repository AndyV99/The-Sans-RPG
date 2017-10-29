from . import Items
from .Armor import HeadArmor, LegArmor, TorsoArmor

Empty = Items.Item(inName="Empty", inWeight=0, inValue=0)

class InventorySlot(object):
    def __init__(self, item=Empty, quantity=0):
        self.item = item
        self.quantity = quantity


class Inventory(object):
    def __init__(self, size=20):
        self.slots = [InventorySlot() for i in range(size)]
        self.weight = 0


    def indexOf(self, item):
        for i in range(len(self.slots)):
            if(self.slots[i].item==item):
                return i
            else:
                pass

    def getItems(self):
        items = []
        for slot in self.slots:
            items.append(slot.item)
        return items


    def addItem(self, item, quantity=1):
        #i to keep track of iteration/slot numbers
        i = 0

        #loop condition
        done = False

        while(not done):
            #if the index is bigger than the inventory, theres no room for the item
            if(i > len(self.slots)-1):
                return "No Room!"

            #if this item is in the inventory and stackable, add the quantity to the stack and its done
            if(self.slots[i].item.name == item.name and item.stackable):
                self.slots[i].quantity += quantity
                done = True

            #if this item isn't in the inventory, try to find an empty slot
            elif("Empty" in self.slots[i].item.name and item.stackable):
                    self.slots[i] = InventorySlot(item, quantity)
                    done = True

            #make sure unstackable items don't stack, but also be sure to add support for adding multiple unstackable items
            elif("Empty" in self.slots[i].item.name and not item.stackable):
                self.slots[i] = InventorySlot(item, 1)
                if(quantity == 1):
                    done = True
                else:
                    quantity -= 1
            i += 1
            self.updateWeight()

    def updateWeight(self):
        self.weight = sum(slot.item.weight for slot in self.slots)

    def removeItem(self, item, quantity=1):
        done = False
        while(not done):
            slotIndex = self.getItems().index(item)

            if(False):
                done = True
            elif(quantity == 0):
                done = True
            elif(item.stackable and quantity < self.slots[slotIndex].quantity):
                self.slots[slotIndex].quantity -= quantity
                done = True
            elif(self.slots[slotIndex].quantity == quantity):
                self.slots[slotIndex] = InventorySlot()
                done = True
            else:
                self.slots[slotIndex].quantity -= quantity
                done = True
            self.updateWeight()


    def getItems(self):
        outItems = []
        for slot in self.slots:
            outItems.append(slot.item)
        return outItems

    def getWeight(self):
        for slot in self.slots:
            self.weight += slot.item.weight

    #DEBUG ONLY REMOVE LATER
    def printInventory(self):
        for slot in self.slots:
            print("{} x{}".format(slot.item.name, slot.quantity))

EmptyHead = HeadArmor.HeadArmor()
EmptyHead.weight = 0
EmptyLeg = LegArmor.LegArmor()
EmptyLeg.weight = 0
EmptyTorso = TorsoArmor.TorsoArmor()
EmptyTorso.weight = 0
EmptyWeapon = Items.Weapon(name="Fist", inDamage=2, inActionCost=5)

class EquipmentInventory(object):
    def __init__(self):
        self.slots = [InventorySlot() for i in range(4)]
        self.slots[0].item = EmptyWeapon
        self.slots[1].item = EmptyHead
        self.slots[2].item = EmptyTorso
        self.slots[3].item = EmptyLeg
        self.weight = 0
        self.damage = 0
        self.defense = 0
        self.healthBuff = 0
        self.healthRegenBuff = 0
        self.actionPointBuff = 0
        self.actionPointRegenBuff = 0


    def getSlotIndex(self, item):
        sloti = 0
        for slot in self.slots:
            if(slot.item == item):
                sloti = self.slots.index(slot)
        return sloti

    def equip(self, item):
        if(issubclass(item.__class__, Items.Weapon)):
            if("Fist" in self.slots[0].item.name):
                self.slots[0].item = item
                self.weight += item.weight
                self.damage = item.damage
                return "You weilded the {}".format(item.name)
            else:
                return "You already have a weapon equipt"

        elif(issubclass(item.__class__, HeadArmor.HeadArmor)):
            if("Empty" in self.slots[1].item.name):
                self.slots[1].item = item
                self.weight += item.weight
                self.addArmorStuff(item)
                return "You weilded the {}".format(item.name)
            else:
                return "You already have a helmet equipt"

        elif(issubclass(item.__class__, TorsoArmor.TorsoArmor)):
            if("Empty" in self.slots[2].item.name):
                self.slots[2].item = item
                self.weight += item.weight
                self.addArmorStuff(item)
                return "You weilded the {}".format(item.name)
            else:
                return "You already have a torso equipt"

        elif(issubclass(item.__class__, LegArmor.LegArmor)):
            if("Empty" in self.slots[3].item.name):
                self.slots[3].item = item
                self.weight += item.weight
                self.addArmorStuff(item)
                return "You weilded the {}".format(item.name)
            else:
                return "You already have pants equipt"


    def unequip(self, item):

        slot = self.getSlotIndex(item)
        if(slot==0):
            self.damage = 0
            self.weight -= item.weight
            self.slots[0].item = EmptyWeapon

        elif(slot==1):
            self.subArmorStuff(item)
            self.weight -= item.weight
            self.slots[1].item = EmptyHead

        elif(slot==2):
            self.subArmorStuff(item)
            self.weight -= item.weight
            self.slots[2].item = EmptyTorso

        elif(slot==3):
            self.subArmorStuff(item)
            self.weight -= item.weight
            self.slots[3].item = EmptyLeg

        return "You unequipt the {}".format(item.name)

    def addArmorStuff(self, item):
        self.defense += item.defense
        self.healthBuff += item.healthBuff
        self.healthRegenBuff += item.healthRegenBuff
        self.actionPointBuff += item.actionPointBuff
        self.actionPointRegenBuff += item.actionPointRegenBuff

    def subArmorStuff(self, item):
        self.defense -= item.defense
        self.healthBuff -= item.healthBuff
        self.healthRegenBuff -= item.healthRegenBuff
        self.actionPointBuff -= item.actionPointBuff
        self.actionPointRegenBuff -= item.actionPointRegenBuff


    def printInventory(self):
        for slot in self.slots:
            print("{} x{}".format(slot.item.name, slot.quantity))
