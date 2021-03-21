# Valorant (any game really) trigger bot
# Made with ♥ by b0kch01

import ctypes
from elevate import elevate
import win32api
import win32gui
import keyboard
import time
import d3dshot
import numpy as np
from pynput import mouse
from pynput.mouse import Controller, Button

# Getting admin so that the program can click on Valorant
if ctypes.windll.shell32.IsUserAnAdmin() != 0:
    elevate(show_console=False)

# CONSTANTS
BOX_LENGTH = 4 # Screen capture size
SCREEN_X = win32api.GetSystemMetrics(0) # Auto-fetched (doesn't always work)
SCREEN_Y = win32api.GetSystemMetrics(1)

# Calculating box coorinates
X1 = int((SCREEN_X - BOX_LENGTH)/2)
Y1 = int((SCREEN_Y - BOX_LENGTH)/2)
X2 = int(SCREEN_X + BOX_LENGTH)
Y2 = int(SCREEN_Y + BOX_LENGTH)

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


if __name__ == "main":
    current_pixel = rgb_pixel()

    while True:
        timeS = time.time()
        new_pixel = rgb_pixel()

        if keyboard.is_pressed("alt") and abs(current_pixel - new_pixel) > 5:
            mouse.click(Button.left)
            print("clicked with " + time_elapsed(timeS))

        current_pixel = new_pixel

        # Stopping program
        if keyboard.is_pressed("esc"): break

print("Program exited.")