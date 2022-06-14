import gamecolors as color

def userChoice(choices):
    validChoices = [] 
    func=False 
    while func == False:
        i=0
        while i < len(choices):
            letter = chr(ord('A')+i)
            print(" ", letter, ": ", choices[i][0], sep="")
            validChoices.append(letter)
            i+=1
        choice=input(">").upper()
        if choice in validChoices:
            func = choices[validChoices.index(choice)][1]
        else:
            color.prRed("Hey, can't you read? Pick a valid choice!")
    func()