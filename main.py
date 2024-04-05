import pyautogui as pag
import random as r
import sys

pag.FAILSAFE = False
NAP_LENGTH = 5  # How long should I sleep between ticks?

pos = pag.position()  # Capture current cursor position


def wiggle(pos):
    if pos == pag.position():  # Check if we should move the cursor. Have we moved since last tick?
        print(f'last position   : {pos}')  # Debug print statements
        print(f'current position: {pag.position()}')   # Debug print statements
        pag.moveRel(r.randint(-200, 200), r.randint(-200, 200), 2, pag.easeOutElastic)  # Move the cursor by a random number of pixels
        return pag.position()  # Capture the new position for the comparison in the next tick
    else:
        print("Nothing to do")  # Debug print statements
        return pag.position()  # Capture the new position for the comparison in the next tick


if __name__ == "__main__":
    print('Press Ctrl-C to quit.')
    try:
        while True:
            pag.sleep(NAP_LENGTH)  # Take a nap
            pos = wiggle(pos)
            sys.stdout.flush()
    except KeyboardInterrupt:
        print("\n")
