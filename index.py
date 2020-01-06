import time
import pyautogui, sys
import math



def getRandom(min, max):
    def getCurrentMilliSec():
        return int(int(round(time.time() * 1000)))

    try:
        while True:
            x, y = pyautogui.position()
            r = getCurrentMilliSec()
            try :
                randomNumber = ( int(x) / int(y) ) % r
                randfrom0to1 =  math.atan(randomNumber)/(math.pi/2)
                ans = math.floor(randfrom0to1 * (max - min + 1) + min)
                print(ans)
            except ZeroDivisionError:
                print(max)
    except KeyboardInterrupt:
        print('\n')

        
        
print(getRandom(233,100000))







