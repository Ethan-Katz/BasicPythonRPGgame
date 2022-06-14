import gamecolors as color

inv = {
    "coins": 50,
    "gun": False,
    "laser":False
}

def takeGun():
    global inv
    inv["gun"] = True
    print("")
    color.prGreen("You Collected The Gun!")

def hasGun():
    return inv["gun"]

def notGun():
    global inv
    inv["gun"] = False
    print("")
    color.prRed("You Did Not Collect The Gun!")

def notGun1():
    global inv
    inv["gun"] = False
    print("")
    color.prRed("He Took Your Gun!")

def takeLaser():
    global inv
    inv["laser"] = True
    print("")
    color.prGreen("You Collected The laser!")

def hasLaser():
    return inv["laser"]

def dropLaser():
    global inv
    inv["laser"] = False
    print("")
    color.prRed("Laser Removed From Ship!")

def takeCoins(c):
    global inv
    inv["coins"] += c

def dropCoins(c):
    global inv
    inv["coins"] -= c

def numCoins():
    return inv["coins"]

def takeDebre():
    global inv
    inv["debre"] = True

def hasDebre():
    return inv["debre"]

def dropDebre():
    global inv
    inv["debre"] = False