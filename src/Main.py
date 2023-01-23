import datetime
import os
import cv2
import time

import Screenshot
import Selfie
import Config

print("hi, init taking place.\nJust a moment...")
path = Config.Config.path  # Path is the folder where all data will be stored
folder = ""  # path to the folder where today's files will be stored. It is within path's folder
i = ""  # date, time and other into
config_file = "D:\\WatchdogTesting\\Config.config"

while True:
    print("loop")
    current_time = datetime.datetime.now()
    i = str(current_time.hour) + "hours" + "-" + str(current_time.minute) + "-" + "mins" + str(
        current_time.second) + "-" + "secs"
    folder = str(current_time.day) + "d-" + str(current_time.month) + "m-" + str(
        current_time.year) + "y\\"  # Later change to Config.Config.folder
    if not os.path.exists(path + folder):
        os.makedirs(path + folder)
        print("making folder")
    if Config.Config.take_screenshot:
        ssfn = path + folder + "Screenshot---" + i + ".png"  # screenshot file name
        cv2.imwrite(ssfn, Screenshot.screenshot())
    if Config.Config.take_selfie:
        sffn = path + folder + "\\Selfie---" + i + ".png"  # selfie file name
        cv2.imwrite(sffn, Selfie.selfie())
    time.sleep(Config.Config.sleep_interval)
