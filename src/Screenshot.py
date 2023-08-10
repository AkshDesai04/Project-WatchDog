import pyautogui
import cv2
import numpy as np
import time
import database_operations
from datetime import datetime


def start_data_capture(con, interval):
    while True:
        image = screenshot()
        now = datetime.now()

        database_operations.db_insert(con, 'Screenshots', {image, now})

        time.sleep(interval)


def screenshot():
    image = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    print("Screenshot Taken")
    return image