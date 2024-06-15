import random
import pyautogui
import time

'''
===========================================================
=============       Position Arrays      ==================
===========================================================
Position arrays should be filled as XMin, XMax, YMin, YMax
'''
# Inventory
materiaOne = [1922,1962,922,960]
materiaTwo = [1978,2017,922,960]
materiaThree = [2033,2071,923,959]
materiaFour = [2087,2128,923,959]
materiaFive = [2142,2182,923,960]
materiaSix = [1922,1961,977,1013]
materiaSeven = [1978,2015,977,1013]
materiaEight = [2034,2070,976,1015]
materiaNine = [2090,2126,977,1013]
materiaTen = [2144,2182,979,1012]
# Dialog
#confirmButton = [1213,1348,784,798] # This version allowed for overlap of No after clicking Confirm
confirmButton = [1228,1265,784,795]
okButton = [1184,1268,796,809]
yesButton = [1182,1265,783,794]

def findAndMove(x, region1,region2,region3,region4):
    found = False

    try:
        start = pyautogui.locateOnScreen(x, region=(region1,region2,region3,region4))#If the file is not a png file it will not work
        pyautogui.moveTo(start)#Moves the mouse to the coordinates of the image
        found = True
    except Exception as e:
        print("Image not found - " + x)

    return found

def findAndNoMove(x, region1,region2,region3,region4):
    found = False

    try:
        pyautogui.locateOnScreen(x, region=(region1,region2,region3,region4))#If the file is not a png file it will not work
        found = True
    except Exception as e:
        print("Image not found - " + x)

    return found

def randCoord(x):
    randomX = random.randint(x[0],x[1])
    randomY = random.randint(x[2],x[3])
    return randomX,randomY
def randomSleep(x,y):
    second = random.randint(x,y)
    milliSecond = random.randint(1,9)
    sleepValue = float(str(second) + "." + str(milliSecond))
    if sleepValue < 0.5:
        sleepValue = 0.5
    time.sleep(sleepValue)
def alert(x):
    pyautogui.alert(x)
def leftClick():
    randomNumber = random.randint(1,6)
    pyautogui.mouseDown(button='left')
    pyautogui.mouseUp(button='left')
    '''
    sleepTimer = 0
    if randomNumber < 4:
        sleepTimer = 0.1
    else:
        sleepTimer = 0.1

    if randomNumber == 3:
        pyautogui.mouseDown(button='left')
        time.sleep(sleepTimer)
        pyautogui.mouseUp(button='left')

        pyautogui.mouseDown(button='left')
        time.sleep(sleepTimer)
        pyautogui.mouseUp(button='left')
    else:
        pyautogui.mouseDown(button='left')
        time.sleep(sleepTimer)
        pyautogui.mouseUp(button='left')
        '''
def rightClick():
    pyautogui.click(clicks=1, button='right')
def MoveToMateria(x):
    if x == 1:
        moveToMateriaOne()
    elif x == 2:
        moveToMateriaTwo()
    elif x == 3:
        moveToMateriaThree()
    elif x == 4:
        moveToMateriaFour()
    elif x == 5:
        moveToMateriaFive()
    elif x == 6:
        moveToMateriaSix()
    elif x == 7:
        moveToMateriaSeven()
    elif x == 8:
        moveToMateriaEight()
    elif x == 9:
        moveToMateriaNine()
    elif x == 10:
        moveToMateriaTen()
def moveToMateriaOne():
    pyautogui.moveTo(random.randint(materiaOne[0],materiaOne[1]), random.randint(materiaOne[2],materiaOne[3]))
def moveToMateriaTwo():
    pyautogui.moveTo(random.randint(materiaTwo[0],materiaTwo[1]), random.randint(materiaTwo[2],materiaTwo[3]))
def moveToMateriaThree():
    pyautogui.moveTo(random.randint(materiaThree[0],materiaThree[1]), random.randint(materiaThree[2],materiaThree[3]))
def moveToMateriaFour():
    pyautogui.moveTo(random.randint(materiaFour[0],materiaFour[1]), random.randint(materiaFour[2],materiaFour[3]))
def moveToMateriaFive():
    pyautogui.moveTo(random.randint(materiaFive[0],materiaFive[1]), random.randint(materiaFive[2],materiaFive[3]))
def moveToMateriaSix():
    pyautogui.moveTo(random.randint(materiaSix[0],materiaSix[1]), random.randint(materiaSix[2],materiaSix[3]))
def moveToMateriaSeven():
    pyautogui.moveTo(random.randint(materiaSeven[0],materiaSeven[1]), random.randint(materiaSeven[2],materiaSeven[3]))
def moveToMateriaEight():
    pyautogui.moveTo(random.randint(materiaEight[0],materiaEight[1]), random.randint(materiaEight[2],materiaEight[3]))
def moveToMateriaNine():
    pyautogui.moveTo(random.randint(materiaNine[0],materiaNine[1]), random.randint(materiaNine[2],materiaNine[3]))
def moveToMateriaTen():
    pyautogui.moveTo(random.randint(materiaTen[0],materiaTen[1]), random.randint(materiaTen[2],materiaTen[3]))
def moveToConfirmButton():
    pyautogui.moveTo(random.randint(confirmButton[0],confirmButton[1]), random.randint(confirmButton[2],confirmButton[3]))
def moveToOkButton():
    pyautogui.moveTo(random.randint(okButton[0],okButton[1]), random.randint(okButton[2],okButton[3]))
def moveToYesButton():
    pyautogui.moveTo(random.randint(yesButton[0],yesButton[1]), random.randint(yesButton[2],yesButton[3]))
def pressEnter():
    pyautogui.press('enter')
def pressG():
    pyautogui.press('g')
def write1():
    pyautogui.write('1')

def enterOneMateria():
    rightClick()
    found = False
    while not found:
        found = findAndNoMove('transmute.png',1850,850,400,400)
        if not found:
            found = findAndNoMove('highlighted mute.png',1850,850,400,400)
    time.sleep(0.1)
    leftClick()
    found = False
    while not found:
        found = findAndNoMove('quantity.png',1000,600,600,600)
    write1()
    time.sleep(0.1)
    pressEnter()
    pressG()
    pressG()
    found = False
    while not found:
        found = findAndNoMove('greyed_confirm.png',1000,600,600,600)

def enterLastMateriaAndComplete():
    rightClick()
    found = False
    while not found:
        found = findAndNoMove('transmute.png',1850,850,500,500)
        if not found:
            found = findAndNoMove('highlighted mute.png', 1850, 850, 500, 500)
    leftClick()
    found = False
    while not found:
        found = findAndMove('filled_confirm.png',1000,600,400,400)
        if not found:
            found = findAndMove('filled_confirm2.png', 1000, 600, 400, 400)
        if not found:
            found = findAndMove('filled_confirm3.png', 1000, 600, 400, 400)
    leftClick()
    found = False
    while not found:
        found = findAndMove('yesbutton.png',1000,600,400,400)
        if not found:
            leftClick()
    leftClick()
    leftClick()
    found = False
    while not found:
        found = findAndMove('greyed_confirm.png',1000,600,400,400)
        if not found:
            leftClick()
            leftClick()