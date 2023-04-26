import pyautogui as pag
import keyboard

drag_up = False

while True:
    if keyboard.is_pressed('page up'):
        drag_up = True
        pag.mouseDown(button='left')

    # Check if the Esc key is pressed
    elif keyboard.is_pressed('page down'):
        # Stop the loop
        pag.mouseUp(button='left')
        break
    if drag_up == True:
        pag.drag(0, -10, duration=0.1, button='left')