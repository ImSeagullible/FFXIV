import pyautogui
import script_variables as vars
import time

pyautogui.alert("Script starting, make sure the \"Materia Transmutation\" window is open.")
time.sleep(3)

inventoryMateriaCount = 115
topRow = True

counter = inventoryMateriaCount

if topRow:
    for x in range(inventoryMateriaCount):
        vars.MoveToMateria(1)
        vars.enterOneMateria()
        vars.MoveToMateria(2)
        vars.enterOneMateria()
        vars.MoveToMateria(3)
        vars.enterOneMateria()
        vars.MoveToMateria(4)
        vars.enterOneMateria()
        vars.MoveToMateria(5)
        vars.enterLastMateriaAndComplete()
        counter = counter-1
        print(counter)
else:
    for x in range(inventoryMateriaCount):
        vars.MoveToMateria(6)
        vars.enterOneMateria()
        vars.MoveToMateria(7)
        vars.enterOneMateria()
        vars.MoveToMateria(8)
        vars.enterOneMateria()
        vars.MoveToMateria(9)
        vars.enterOneMateria()
        vars.MoveToMateria(10)
        vars.enterLastMateriaAndComplete()
        counter = counter - 1
        print(counter)
vars.alert("Script is complete")