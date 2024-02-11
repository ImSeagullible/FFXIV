import pyautogui
import time

counter = 0
xValues = []
yValues = []

while True:
    if counter == 0:
        print("Starting, move to top-left")
    elif counter < 5:
        print(pyautogui.position())
        x,y = pyautogui.position()
        xValues.append(x)
        yValues.append(y)
        if counter == 4:
            minX = min(xValues)
            maxX = max(xValues)
            minY = min(yValues)
            maxY = max(yValues)
            print("Materia Array: " + str(minX) + "," + str(maxX) + "," + str(minY) + "," + str(maxY))
    else:
        counter = 0
        xValues = []
        yValues = []
    time.sleep(3)
    counter += 1