import time
import random
import inventory as inv
import gamecolors as color
import userchoice as choice
import gamerandnum as randnum
import reStart
import part1

def fate2():
    color.prLightPurple("What Will You Do?")
    startFate2 = [["Shoot at him with your gun", fate2enda],
                    ["Run towards the soldier and attack",fate2endb]]
    choice.userChoice(startFate2)

def fate2enda():
    if not inv.hasGun():
        print()
        color.prRed("You dont have a gun")
        print()
        time.sleep(3)
        color.prCyan("While trying to pull out your non existant gun.")
        time.sleep(3)
        color.prCyan("The soldier shoots you!")
        print()
        time.sleep(3)
        color.prRed("You Died!")
        time.sleep(2)
        reStart.restartGame()

def gunuserYesNo():
        color.prLightPurple("Do You Want To Pick Up His Gun?")
        x=input(">").upper()
        if x in ["Y", "YES"]:
            inv.takeGun()
        elif x in ["N", "NO"]:
            inv.notGun()

def fate2endb():
    print()
    color.prCyan("You have started running towards the soldier.")
    time.sleep(3)
    color.prCyan("While running you are trying your best to deflect the bullets.")
    time.sleep(4)
    color.prCyan("You finally make it next to the soldier.")
    time.sleep(3)
    color.prCyan("You start attacking him.")
    time.sleep(3)
    color.prCyan("You are losing the fight.")
    time.sleep(3)
    color.prCyan("You finally get one good hit and you knock him out.")
    time.sleep(4)
    print()
    gunuserYesNo()
    if inv.hasDebre() == True:
        time.sleep(3)
        print()
        color.prCyan("You start walking to Quin's HQ.")
        time.sleep(3)
        color.prCyan("You spot Quin.")
        time.sleep(3)
        if inv.hasGun() == False:
            print()
            color.prCyan("Quin spots you!")
            time.sleep(3)
            color.prCyan("Since you dont have a gun.")
            time.sleep(3)
            color.prCyan("Quin shoots you!")
            print()
            time.sleep(3)
            color.prRed("You Died!")
            time.sleep(2)
            reStart.restartGame()
        if inv.hasGun() == True:
            print()
            color.prCyan("Before you or Quin can blink you shoot him dead in the head")
            youWin()
    else:
        time.sleep(3)
        print()
        color.prCyan("Since you did not destroy the two ships.")
        time.sleep(3)
        color.prCyan("The enemies on those ships snuck onto Quin's ship.")
        time.sleep(3)
        color.prCyan("They spot you and shoot you on the spot!")
        print()
        time.sleep(3)
        color.prRed("You Died!")
        time.sleep(2)
        reStart.restartGame()

def youWin():
    print()
    time.sleep(2)
    color.prGreen("CONGRATULATIONS! YOU WIN!")
    print()
    time.sleep(2)
    color.prGreen("Game Over!")
