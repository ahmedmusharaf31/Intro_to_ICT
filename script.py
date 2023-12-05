import pyautogui as pg
import time
import os
import winsound
delay = 0.001 
def writespec(i):
    s='~!@#$%^&*()_+{}:"|<>?'
    t="`1234567890-=[];'\\,./"
    with pg.hold('shift'):
        pg.press(t[s.index(i)])


def write(s):
    for i in s:
        if i in '~!@#$%^&*()_+{}:"|<>?':
            writespec(i)
            continue
        if i.isupper():
            with pg.hold('shift'):
                pg.press(i.lower())
        else:
            pg.typewrite(i)
        time.sleep(delay)
print("Enter the name of the txt file to read from:",end=' ')
n=input()
time.sleep(10) # How much time to sleep before start writing
with open(n,"r") as f:
    write(f.read())
    pass
winsound.Beep(1500, 1000) # 1000 = 1s (beeps for 1s at frequency 1500Hz)
time.sleep(5)
