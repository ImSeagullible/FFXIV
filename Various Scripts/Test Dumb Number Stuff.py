import random
import time

xSecond = 5
xMilliSecond = 3

ySecond = 2
yMillisecond = 7

testNumber = float(str(xSecond) +"."+ str(xMilliSecond)) - 2

second = random.randint(0,1)
milliSecond = random.randint(1,9)
sleepValue = float(str(second) + "." + str(milliSecond))
print(sleepValue)