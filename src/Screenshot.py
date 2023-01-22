import pyautogui
import cv2
import numpy as np


def screenshot(i, folder):  # TODO: Remove parameters coz i and folder are already managed by the Main.py file

    image = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    print("Screenshot Taken")
    return image
