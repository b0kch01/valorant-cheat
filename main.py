# Valorant (any game really) trigger bot
# Made with ♥ by b0kch01

import os, ctypes
if os.name != "nt":
    input("Windows support only. Press [Enter] to close")
    exit(0)

import win32api
import win32gui
import keyboard
import time
import d3dshot
import numpy as np
from pynput import mouse
from pynput.mouse import Controller, Button
from pyfiglet import Figlet
from termcolor import cprint, colored
import colorama


# Fix legacy console color
colorama.init()

# CONSTANTS
KEYBIND = "alt" # Default keybind
BOX_LENGTH = 4 # Screen capture size
SCREEN_X = win32api.GetSystemMetrics(0) # Auto-fetched (doesn't always work)
SCREEN_Y = win32api.GetSystemMetrics(1)

# Calculating box coorinates
X1 = int(SCREEN_X/2 - BOX_LENGTH/2)
Y1 = int(SCREEN_Y/2 - BOX_LENGTH/2)
X2 = int(X1 + BOX_LENGTH)
Y2 = int(Y1 + BOX_LENGTH)

REGION = (X1, Y1, X2, Y2)

cprint("Setting up...")
cprint(" - [¤] Windows", "green")
cprint(f" - [¤] {SCREEN_X}x{SCREEN_Y}", "green")

if ctypes.windll.shell32.IsUserAnAdmin() == 0:
    cprint(" - [x] Please run as administrator", "red")
    exit(0)

cprint(f" - [¤] {SCREEN_X}x{SCREEN_Y}", "green")

time.sleep(0.5)

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
f = Figlet(font="ogre")

CACHED_TITLESCREEN = f"""
{ f.renderText("Valorant Cheat")[:-3] }
{ colored(" Created with ♥ by b0kch01! ", "grey", "on_white") }
{ colored(" USE AT YOUR OWN RISK       ", "grey", "on_yellow") }

Enjoy! :)
"""

def clear():
    os.system("cls")

def titlescreen():
    clear()
    print(CACHED_TITLESCREEN)


# MAIN SCRIPT


try:
    titlescreen()
    if input("Set custom keybind? (yes/no): ")[:1] in "yY":
        titlescreen()
        print(f"Current keybind: [{colored(KEYBIND, 'green')}]")
        print("\nPress [ESC] to continue")
        
        new_key = KEYBIND

        while True:
            new_key = keyboard.read_key()

            if new_key == "esc":
                break
            elif new_key != KEYBIND:
                KEYBIND = new_key
                titlescreen()
                print(f"Current keybind: [{colored(KEYBIND, 'green')}]")
                print("\nPress [ESC] to continue")

    titlescreen()
    print(f"Current keybind: [{colored(KEYBIND, 'green')}]")
    cprint("\nReady to frag.", "green")

    current_pixel = rgb_pixel()

    while True:
        if keyboard.is_pressed(KEYBIND):
            timeS = time.time()
            new_pixel = rgb_pixel()

            if abs(current_pixel - new_pixel) > 5:
                mouse.click(Button.left)
                print("[¤] Clicked within " + time_elapsed(timeS))

            current_pixel = new_pixel
        else:
            current_pixel = rgb_pixel()
            time.sleep(0.05)

except KeyboardInterrupt:
    pass

cprint("\n~ Program exited ;-;", "grey", "on_red")
time.sleep(1)