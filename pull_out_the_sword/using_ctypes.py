import pyautogui as pag
import keyboard
import time
import ctypes

def main():
    pag.mouseDown()
    while True:
        if keyboard.is_pressed('esc'):
            pag.mouseUp()
            break
        else:
            ctypes.windll.user32.mouse_event(0x0003, 0, -2000, 0, 0)
            time.sleep(0.03)

while True:          
    if keyboard.is_pressed('page up'):
        main()
        break