import pyautogui
import keyboard
import time
time.sleep(5)
x = 1
while x == 1:
    pyautogui.tripleClick()
    if keyboard.is_pressed('x'):
        x = 0  

