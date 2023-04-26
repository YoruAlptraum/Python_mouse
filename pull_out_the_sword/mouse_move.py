import pyautogui as pag
import keyboard

move_up = False

while True:
    if keyboard.is_pressed('page up'):
        move_up = True
        pag.mouseDown(button='left')

    # Check if the Esc key is pressed
    elif keyboard.is_pressed('page down'):
        # Stop the loop
        pag.mouseUp(button='left')
        break
    if move_up == True:
        pag.move(0, -10, duration=0.1)