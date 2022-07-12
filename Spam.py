import pyautogui 
import time

time.sleep(5)
f = open('text1.txt', 'r')
while True:
    for word in f:
        time.sleep(0.3)
        pyautogui.typewrite(word)
        pyautogui.press("enter") 