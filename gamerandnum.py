import gamecolors as color
import random
import time

def num():
    print("")
    color.prYellow("To Repair Your Ship You Must Guess The Number! (1-10)")
    z = 0
    done=False
    y = (random.randint(1,10))
    while not done:
        z = z+1
        x = int(input(">"))
        if x == y:
            print("")
            color.prGreen("You Got It!")
            time.sleep(2)
            print("")
            done=True
        elif x<y:
            print("")
            color.prRed("Too Low, Try Again!")
        elif x>y:
            print("")
            color.prRed("Too High, Try Again!")