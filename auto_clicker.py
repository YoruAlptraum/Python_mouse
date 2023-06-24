import pyautogui
import time
import keyboard

def autoclicker(interval):
    print("Press 'pause' to start and stop the autoclicker.")
    running = False
    last_stop_time = 0

    while True:
        if keyboard.is_pressed('pause'):
            current_time = time.time()
            if running:
                print("Autoclicker stopped!")
                running = False
                last_stop_time = current_time
            else:
                if current_time - last_stop_time >= 1:
                    print("Autoclicker started!")
                    running = True
        if keyboard.is_pressed('end'):
            print("Program finished")
            break
        if running:
            pyautogui.click()
            time.sleep(interval)

# Usage example
autoclicker(0.1)
