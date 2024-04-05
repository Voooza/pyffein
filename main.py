import pyautogui as pag
import random as r

NAP_LENGTH = 10  # How long should I sleep between ticks?

pos = pag.position()  # Capture current cursor position


while True:  # Cycle forever
    pag.sleep(NAP_LENGTH)  # Take a nap
    if pos == pag.position():  # Check if we should move the cursor. Have we moved since last tick?
        # print(f'last position   : {pos}')  # Debug print statements
        # print(f'current position: {pag.position()}')   # Debug print statements
        pag.moveRel(r.randint(-10, 10), r.randint(-10, 10))  # Move the cursor by a random number of pixels
        pos = pag.position()  # Capture the new position for the comparison in the next tick
    else:
        # print("Nothing to do")  # Debug print statements
        pos = pag.position()  # Capture the new position for the comparison in the next tick
