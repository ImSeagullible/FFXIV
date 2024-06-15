import script_variables as vars
import time

'''
Screen Resolution expectation: Fullscreen/Windowed Fullscreen, 1440p

Materia Gambling "bot"
To be ran from Central Thanaland with the following in mind:
    Inventory needs to be open
    Have already transmuted at least one Materia group
    If doing 9s, manually get a 10 upgrade first to not trigger cutscene
    Expanded Inventory View (All 4 Boxes at once)
    Inventory at 120% Scale
    Return Inventory to Default Position
    Dialog/Transmute Screen to 100% Scale
    Dialog/Transmute Screen to Default Position
    
====================================================================
This will be using the last 2 rows of the bottom-left inventory bag.
And will be labeled as:
1,2,3,4,5
6,7,8,9,10
====================================================================
'''



# Populate these to match the bottom-left Inventory Materia counts
inventoryMateriaCounts = [
    995,995,995,995,995
]

vars.alert("Script starting, make sure the \"Materia Transmutation\" window is open.")
time.sleep(3)
amountOfMateria = 999
materiaCounter = amountOfMateria



def doShit():
    vars.randomSleep(0, 0)
    vars.rightClick()  # Right Click Materia to bring up Menu
    vars.randomSleep(1, 1)
    vars.leftClick()  # Left Click Materia "Transmute" from Menu
    time.sleep(0.6)
    vars.write1() # Enter 1
    time.sleep(0.3)
    vars.pressEnter() # Leave textbox
    time.sleep(0.3)
    vars.pressG() # Confirm 1
    time.sleep(0.3)
    vars.pressG() # Leave menu
    time.sleep(0.3)


for x in range(amountOfMateria):
    vars.MoveToMateria(1) # Mouseover Materia
    doShit()
    vars.MoveToMateria(2)  # Mouseover Materia
    doShit()
    vars.MoveToMateria(3)  # Mouseover Materia
    doShit()
    vars.MoveToMateria(4)  # Mouseover Materia
    doShit()
    vars.MoveToMateria(5)  # Mouseover Materia
    doShit()

    vars.randomSleep(1,2)
    vars.moveToOkButton() # Move to OK Button
    vars.randomSleep(0,0)
    vars.leftClick() # Left Click OK Button
    vars.randomSleep(1, 2)
    vars.moveToConfirmButton() # Move to Confirm Button
    vars.randomSleep(0,0)
    vars.leftClick() # Left Click OK Button
    vars.randomSleep(1, 2)
    vars.moveToYesButton() # Move to Yes Button
    vars.randomSleep(0,0)
    vars.leftClick() # Left Click Yes Button
    vars.leftClick() # Left Click Yes Button
    amountOfMateria -= 1
    vars.randomSleep(1, 3)
    materiaCounter += 1

vars.alert("Script is complete")
