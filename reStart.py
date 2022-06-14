import time
import random
import inventory as inv
import gamecolors as color
import userchoice as choice
import gamerandnum as randnum
import part1
import part2

def restartGame():
        print()
        time.sleep(1)
        color.prLightPurple("Bringing You Back To The Menu")
        time.sleep(1)
        print("3")
        time.sleep(.8)
        print("2")
        time.sleep(.8)
        print("1")
        time.sleep(.8)
        startGame()

def startGame():
    time.sleep(2)
    color.prLightPurple("     Loading...")
    print()
    time.sleep(.5)
    print("       10%..")
    time.sleep(.5)
    print("Preparing The StoryLine")
    print("       20%..")
    time.sleep(2)
    print("       40%..")
    time.sleep(.5)
    print("  Giving Coins")
    print("       60%..")
    time.sleep(2)
    print("       80%..")
    time.sleep(.25)
    print("       100%")
    part1.part1()