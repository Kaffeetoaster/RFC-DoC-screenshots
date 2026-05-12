import os
import time

import mss
import mss.tools
import pyautogui

from measure_duration import *
from config.config import DELAY_BETWEEN_SCREENSHOTS
from config.config import NUM_SCREENSHOTS

def take_screenshot(filename, region=None):
    with mss.MSS() as sct:
        mouse_x, mouse_y = pyautogui.position()
        active_monitor = sct.monitors[1]

        for monitor in sct.monitors[1:]:
            left = monitor["left"]
            top = monitor["top"]
            right = left + monitor["width"]
            bottom = top + monitor["height"]
            if left <= mouse_x < right and top <= mouse_y < bottom:
                active_monitor = monitor
                break

        capture_area = dict(active_monitor)
        if region is not None:
            region_left, region_top, region_width, region_height = region
            capture_area["left"] = active_monitor["left"] + region_left
            capture_area["top"] = active_monitor["top"] + region_top
            capture_area["width"] = region_width
            capture_area["height"] = region_height

        screenshot = sct.grab(capture_area)
        directory = os.path.dirname(filename)
        if directory:
            os.makedirs(directory, exist_ok=True)
        mss.tools.to_png(screenshot.rgb, screenshot.size, output=filename)
        return filename

def zoom_out(seconds):
    pyautogui.keyDown('pageup')
    time.sleep(seconds) # Hold the 'pageup' key 
    pyautogui.keyUp('pageup')

def zoom_in(seconds):
    pyautogui.keyDown('pagedown')
    time.sleep(seconds) # Hold the 'pagedown' key
    pyautogui.keyUp('pagedown')

def move_right(seconds):
    pyautogui.keyDown('right')
    time.sleep(seconds) # Hold the 'right' key
    pyautogui.keyUp('right')

def move_left(seconds):
    pyautogui.keyDown('left')
    time.sleep(seconds) # Hold the 'left' key
    pyautogui.keyUp('left')

def move_down(seconds):
    pyautogui.keyDown('down')
    time.sleep(seconds) # Hold the 'down' key
    pyautogui.keyUp('down')

def move_up(seconds):
    pyautogui.keyDown('up')
    time.sleep(seconds) # Hold the 'up' key
    pyautogui.keyUp('up')


def move_to_next_column(Number_x, Number_y, delay_x, delay_y):
    for i in range(Number_y - 1): # move back down to the bottom
        move_down(delay_y)
                 
    time.sleep(1.0)
    #take_screenshot(f'screenshots/screenshot_{x}_{0}_control.png')
    move_right(delay_x)
    time.sleep(1.0)

def move_to_next_column_unit(Number_x, Number_y, delay_x, delay_y):
    pyautogui.press('Enter')
    time.sleep(5.0)

def take_screenshots(Number_x, Number_y, delay_x, delay_y):
    for x in range(Number_x):
        for y in range(Number_y):
            print(f"taking screenshot at column {x} and row {y}...")
            take_screenshot(f'screenshots/screenshot_{x}_{y}.png')
            if y != Number_y - 1: # don't move up after the last screenshot in the column
                move_up(delay_y)
                time.sleep(2.0)
        # move to next row
        if x != Number_x - 1: # don't move right after the last column
             move_to_next_column(Number_x, Number_y, delay_x, delay_y)




start_new_log()
pyautogui.FAILSAFE = True
time.sleep(15) # Wait a few seconds before starting to take screenshots

print("Starting to scroll and press down keys...")
time.sleep(1)
measure(take_screenshots, NUM_SCREENSHOTS[0], NUM_SCREENSHOTS[1], DELAY_BETWEEN_SCREENSHOTS[0], DELAY_BETWEEN_SCREENSHOTS[1])






