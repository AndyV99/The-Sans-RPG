from tkinter import *
from tkinter import font
from random import *
import time
from ..GUIIndexes import *

class RoomScreen(Tk):
    def __init__(self, game):
        Tk.__init__(self)
        self.game = game
        self.dungeon = self.game.getCurrentTown().dungeon
        self.room = self.dungeon.getCurrentRoom()

        print("Create Room Screen")

        self.titleFont = font.Font(family="Comic Sans MS", size=24)
        self.buttonFont = font.Font(family="Comic Sans MS", size=18)
        self.generalFont = font.Font(family="Comic Sans MS", size=18)
        self.smallerFont = font.Font(family="Comic Sans MS", size=14)
        self.nameFont = font.Font(family="Comic Sans MS", size=20, weight=font.BOLD)

        self.geometry('%dx%d+%d+%d' % self.game.guiHandler.windowInfo)
        self.minsize(1000, 600)
        self.wm_title("Room #{}".format(self.dungeon.currentRoom+1))

        self.log = StringVar()

        self.addPlayerInfo()
        self.addEnemyInfo()
        self.configureGrid()
        self.addLogAndButtons()


    def addPlayerInfo(self):
        self.game.guiHandler.addPlayerInfo(self)
        self.playerInfo.grid(row=0, column=0, sticky="NWS")


    def addEnemyInfo(self):
        BAR_HEIGHT = 20
        BAR_WIDTH = 150

        self.enemyInfo = Frame()
        self.enemyInfo.grid(row=0, column=2, sticky="NWES")

        enemy = self.room.enemies[self.room.currentEnemy]

        self.enemyName = Label(self.enemyInfo, text="{} lvl {}".format(enemy.name, enemy.level), font=self.nameFont, anchor=SW)
        self.enemyName.grid(row=0, column=0, columnspan=2, sticky="NW")

        self.enemyhpFrame = Frame(self.enemyInfo)

        self.enemyhealthBar = Canvas(self.enemyhpFrame, height=BAR_HEIGHT, width=BAR_WIDTH, bd=5, relief=RAISED)
        self.enemyhealthBar.create_rectangle(5, 5, ((enemy.currentHealth/enemy.totalHealth)*BAR_WIDTH)+7, BAR_HEIGHT+10, fill="green")
        self.enemyhealthLabel = Label(self.enemyhpFrame, text="HP : {}/{}".format(enemy.currentHealth, enemy.totalHealth), font=self.generalFont)

        self.enemyhpSymbol = Label(self.enemyhpFrame, image=self.hp)

        self.enemyhealthBar.grid(row=0, column=2, sticky="E")
        self.enemyhealthLabel.grid(row=0, column=0, sticky="NWS")
        self.enemyhpSymbol.grid(row=0, column=1, sticky="NWS")

        self.enemyhpFrame.grid(row=1, column=0, columnspan=2, sticky="NEWS")

        self.enemyDamageLabel = Label(self.enemyInfo, text="Damage", font=self.generalFont, anchor=SE)
        self.enemyDamageNumber = Label(self.enemyInfo, text="{}".format(enemy.damage), font=self.generalFont, anchor=SW)
        self.enemyDamageLabel.grid(row=2, column=0, sticky="NW")
        self.enemyDamageNumber.grid(row=2, column=1, sticky="NES")


        self.enemyDefenseLabel = Label(self.enemyInfo, text="Defense", font=self.generalFont, anchor=SE)
        self.enemyDefenseNumber = Label(self.enemyInfo, text="{}".format(enemy.defense), font=self.generalFont, anchor=SW)
        self.enemyDefenseLabel.grid(row=3, column=0, sticky="NW")
        self.enemyDefenseNumber.grid(row=3, column=1, sticky="NES")


        self.enemyEvasivenessLabel = Label(self.enemyInfo, text="Evasiveness", font=self.generalFont, anchor=SE)
        self.enemyEvasivenessNumber = Label(self.enemyInfo, text="{}".format(enemy.evasiveness), font=self.generalFont, anchor=SW)
        self.enemyEvasivenessLabel.grid(row=4, column=0, sticky="NW")
        self.enemyEvasivenessNumber.grid(row=4, column=1, sticky="NES")

        self.enemySpeedLabel = Label(self.enemyInfo, text="Speed", font=self.generalFont, anchor=SE)
        self.enemySpeedNumber = Label(self.enemyInfo, text="{}".format(enemy.speed), font=self.generalFont, anchor=SW)
        self.enemySpeedLabel.grid(row=5, column=0, sticky="NW")
        self.enemySpeedNumber.grid(row=5, column=1, sticky="NES")

        for i in range(13):
            self.enemyInfo.grid_rowconfigure(i, weight=1, minsize=15)
        self.enemyInfo.grid_columnconfigure(0, weight=1)
        self.enemyInfo.grid_columnconfigure(1, weight=1)


    def addLogAndButtons(self, newLog=""):
        self.addPlayerInfo()
        self.addEnemyInfo()
        player = self.game.player
        enemy = self.room.enemies[self.room.currentEnemy]
        weapon = self.game.player.equipment.slots[0].item
        restRegen = (player.agility*2) + (player.intelligence*3) + (player.level*2)

        log = "\n".join(newLog)

        self.log.set(log)

        self.logAndButtonsFrame = Frame()

        self.logLabel = Label(self.logAndButtonsFrame, textvariable=self.log, font=self.smallerFont, wraplength=400, anchor=W, justify=LEFT)
        self.logLabel.grid(row=0, column=0, sticky="NEWS")

        self.attackButton = Button(self.logAndButtonsFrame, image=self.ap, compound=RIGHT, text="Attack -{}".format(weapon.actionPointCost), font=self.generalFont, command=self.attack)
        self.attackButton.grid(row=1, column=0, sticky="NEWS")

        if(player.currentActionPoints < weapon.actionPointCost):
            self.attackButton.config(state=DISABLED)
        else:
            self.attackButton.config(state=NORMAL)

        self.restButton = Button(self.logAndButtonsFrame, image=self.ap, compound=RIGHT, text="Rest +{}".format(restRegen), font=self.generalFont, command=self.rest)
        self.restButton.grid(row=2, column=0, sticky="NEWS")

        self.runButton = Button(self.logAndButtonsFrame, text="Attempt Run (50%)", font=self.generalFont, command=self.run)
        self.runButton.grid(row=3, column=0, sticky="NEWS")

        self.logAndButtonsFrame.grid_columnconfigure(0, weight=1)

        self.logAndButtonsFrame.grid_rowconfigure(0, weight=1, minsize=400)
        self.logAndButtonsFrame.grid_rowconfigure(1, weight=1)
        self.logAndButtonsFrame.grid_rowconfigure(2, weight=1)
        self.logAndButtonsFrame.grid_rowconfigure(3, weight=1)

        self.logAndButtonsFrame.grid(row=0, column=1, sticky="NEWS")


    def attack(self):
        player = self.game.player
        enemy = self.room.enemies[self.room.currentEnemy]

        returnStrings = []

        if(player.speed > enemy.speed):
            plrDmg = player.equipment.slots[0].item.getDamage(player)
            returnStrings.append("{} did {} damage.".format(player.name, plrDmg))
            eneBlock = enemy.getBlock()
            returnStrings.append("{} blocked {} damage.".format(enemy.name, eneBlock))
            plrDmg = min(enemy.totalHealth, max(plrDmg-eneBlock, 0))
            returnStrings.append("{} lost {} health.".format(enemy.name, plrDmg))
            enemy.currentHealth -= plrDmg
            player.currentActionPoints -= player.equipment.slots[0].item.actionPointCost

            dead, string = self.checkDead()
            returnStrings.append(string)

            if(not dead):
                eneDmg = enemy.getDamage()
                returnStrings.append("{} did {} damage.".format(enemy.name, eneDmg))
                plrBlock = player.getBlock()
                returnStrings.append("{} blocked {} damage.".format(player.name, plrBlock))
                eneDmg = min(player.totalHealth, max(eneDmg-player.getBlock(), 0))
                returnStrings.append("{} lost {} health.".format(player.name, eneDmg))
                player.currentHealth -= eneDmg

                self.checkDead()
                self.addLogAndButtons()

            hpGain, apGain = player.passiveEffects()
            if(hpGain > 0):
                returnStrings.append("{} regenerated {} health from passive effects!".format(player.name, hpGain))
            if(apGain > 0):
                returnStrings.append("{} regenerated {} action points from passive effects!".format(player.name, apGain))

        else:
            eneDmg = enemy.getDamage()
            returnStrings.append("{} did {} damage.".format(enemy.name, eneDmg))
            plrBlock = player.getBlock()
            returnStrings.append("{} blocked {} damage.".format(player.name, plrBlock))
            eneDmg = min(player.totalHealth, max(eneDmg-player.getBlock(), 0))
            returnStrings.append("{} lost {} health.".format(player.name, eneDmg))
            player.currentHealth -= eneDmg

            self.checkDead()

            plrDmg = player.equipment.slots[0].item.getDamage(player)
            returnStrings.append("{} did {} damage.".format(player.name, plrDmg))
            eneBlock = enemy.getBlock()
            returnStrings.append("{} blocked {} damage.".format(enemy.name, eneBlock))
            plrDmg = min(enemy.totalHealth, max(plrDmg-eneBlock, 0))
            returnStrings.append("{} lost {} health.".format(enemy.name, plrDmg))
            enemy.currentHealth -= plrDmg
            player.currentActionPoints -= player.equipment.slots[0].item.actionPointCost


            dead, string = self.checkDead()
            returnStrings.append(string)

            hpGain, apGain = player.passiveEffects()
            if(hpGain > 0):
                returnStrings.append("{} regenerated {} health from passive effects!".format(player.name, hpGain))
            if(apGain > 0):
                returnStrings.append("{} regenerated {} action points from passive effects!".format(player.name, apGain))

        self.addLogAndButtons(returnStrings)

    def rest(self):
        player = self.game.player
        enemy = self.room.enemies[self.room.currentEnemy]

        returnStrings = []

        restRegen = (player.agility*2) + (player.intelligence*3) + (player.level*2)
        returnStrings.append("{} rested for {} action ponts.".format(player.name, restRegen))
        player.currentActionPoints = min(player.totalActionPoints, player.currentActionPoints+restRegen)

        hpGain, apGain = player.passiveEffects()
        if(hpGain > 0):
            returnStrings.append("{} regenerated {} health from passive effects!".format(player.name, hpGain))
        if(apGain > 0):
            returnStrings.append("{} regenerated {} action points from passive effects!".format(player.name, apGain))

        eneDmg = enemy.getDamage()
        returnStrings.append("{} did {} damage.".format(enemy.name, eneDmg))
        plrBlock = player.getBlock()
        returnStrings.append("{} blocked {} damage.".format(player.name, plrBlock))
        eneDmg = min(player.totalHealth, max(eneDmg-player.getBlock(), 0))
        returnStrings.append("{} lost {} health.".format(player.name, eneDmg))
        player.currentHealth -= eneDmg

        self.checkDead()

        self.addLogAndButtons(returnStrings)

    def run(self):
        player = self.game.player
        enemy = self.room.enemies[self.room.currentEnemy]
        returnStrings = []
        r = randint(0, 100)
        if(r > 50):
            self.addLogAndButtons(["You Got Away"])
            time.sleep(1)
            self.game.guiHandler.swapGUI(DUNGEON_SCREEN)
        else:
            self.addLogAndButtons(["You couldn't get away!"])
            eneDmg = enemy.getDamage()
            returnStrings.append("{} did {} damage.".format(enemy.name, eneDmg))
            plrBlock = player.getBlock()
            returnStrings.append("{} blocked {} damage.".format(player.name, plrBlock))
            eneDmg = min(player.totalHealth, max(eneDmg-player.getBlock(), 0))
            returnStrings.append("{} lost {} health.".format(player.name, eneDmg))
            player.currentHealth -= eneDmg

            checkDead()

            self.addLogAndButtons(returnStrings)


    def checkDead(self):
        player = self.game.player
        enemy = self.room.enemies[self.room.currentEnemy]
        if(player.currentHealth <= 0):
            self.game.guiHandler.swapGUI(GAME_OVER)
        if(enemy.currentHealth <= 0):
            self.nextEnemy()
            self.game.addXPToPlayer(enemy.xp)
            gold = randint(int(self.room.level*2), int(self.room.level*6))
            player.money += gold
            return True, "{} died.\n{} gained {}xp and {} gold.\nNext Enemy.".format(enemy.name, player.name, enemy.xp, gold)
        else:
            return False, ""


    def nextEnemy(self):
        if(self.room.currentEnemy+1 == len(self.room.enemies)):
            self.dungeon.nextRoom()
            self.game.guiHandler.swapGUI(DUNGEON_SCREEN)
        else:
            self.room.currentEnemy += 1

    def configureGrid(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1, minsize=400)
        self.grid_columnconfigure(2, weight=1)

        self.grid_rowconfigure(0, weight=1)
