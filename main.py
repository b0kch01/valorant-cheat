# Valorant (any game really) trigger bot
# Made with ♥ by b0kch01

import os
import win32api
import win32gui
import keyboard
import time
import d3dshot
import numpy as np
from pynput import mouse
from pynput.mouse import Controller, Button
from pyfiglet import Figlet
from termcolor import cprint
import colorama

# Fix legacy console color
colorama.init()


# CONSTANTS
BOX_LENGTH = 4 # Screen capture size
SCREEN_X = win32api.GetSystemMetrics(0) # Auto-fetched (doesn't always work)
SCREEN_Y = win32api.GetSystemMetrics(1)

print(SCREEN_X, SCREEN_Y)

# Calculating box coorinates
X1 = int(SCREEN_X/2 - BOX_LENGTH/2)
Y1 = int(SCREEN_Y/2 - BOX_LENGTH/2)
X2 = int(X1 + BOX_LENGTH)
Y2 = int(Y1 + BOX_LENGTH)

REGION = (X1, Y1, X2, Y2)

# Disable click delay (100ms)
win32gui.GetDoubleClickTime = lambda: 0;

# Instantiate mouse controller
mouse = Controller()

# Instantiate screen capture (numpy is the fastest)
d = d3dshot.create(capture_output="numpy")

# Grabs center screen as an average pixel value
def rgb_pixel():
	return np.average(d.screenshot(region=REGION))

# Given start time, returns time elapsed in ms
def time_elapsed(start_time):
    return str(int((time.time() - start_time)*1000)) + "ms"


# User Interface
def titlescreen():
    # os.system("cls")
    f = Figlet(font="ogre")
    print(f.renderText("Valorant Cheat")[:-3])
    cprint(" Created with ♥ by b0kch01! ", "grey", "on_white")
    cprint(" USE AT YOUR OWN RISK       ", "grey", "on_yellow")

    print("\nRemember, hold [esc] to exit the program")
    print("Enjoy! :)\n")

    cprint("Current keybind: [ALT]\n", "green")


# MAIN SCRIPT
titlescreen()
current_pixel = rgb_pixel()

try:
    while True:
        timeS = time.time()
        new_pixel = rgb_pixel()

        if keyboard.is_pressed("alt"):
            if abs(current_pixel - new_pixel) > 5:
                mouse.click(Button.left)
                print("[¤] Clicked within " + time_elapsed(timeS))

        current_pixel = new_pixel

        # Stopping program
        if keyboard.is_pressed("esc"): break
except KeyboardInterrupt:
    pass

print("Program exited.")