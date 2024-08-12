# use pyautogui to take a screenshot to a path

import pyautogui
import time

latest_file_path = ""
file_path = "./dump-imgs/"


def take_screenshot(path):
    # take screenshot
    myScreenshot = pyautogui.screenshot()
    # save screenshot
    myScreenshot.save(path)
    print("Screenshot saved to: " + path)


def take_screenshot_with_delay(path, delay):
    # take screenshot
    time.sleep(delay)
    myScreenshot = pyautogui.screenshot()
    # save screenshot
    myScreenshot.save(path)
    # print("Screenshot saved to: " + path)


def get_file_path():
    global latest_file_path

    # file name is file_path + current time + date + png
    # file_name = file_path + time.strftime("%H-%M-%S") + "-" + time.strftime("%d-%m-%Y") + ".png"
    file_name = file_path + time.strftime("%H-%M-%S") + ".png"

    latest_file_path = file_name

    return latest_file_path


# take_screenshot_with_delay(file_name, 15)
# take_screenshot(file_name)
