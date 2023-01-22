import datetime
import os
import cv2
import time

import Screenshot
import Selfie
from congif import config

print("hi, init taking place.\nJust a moment...")
path = config.path #Path is the folder where all data will be stored
folder = "" #Folder is the path to the folder where todays files will be stored. It is within path's folder
i = "" #i stores the date, time and other into
config_file = "D:\\WatchdogTesting\\config.config"

while True:
    print("loop")
    current_time = datetime.datetime.now()
    i = str(current_time.hour) + "hours" + "-" + str(current_time.minute) + "-" + "mins" + str(current_time.second) + "-" + "secs"
    folder = str(current_time.day) + "d-" + str(current_time.month) + "m-" + str(current_time.year) + "y\\" # Later change to config.folder
    if not os.path.exists(path + folder):
        os.makedirs(path + folder)
        print("making folder")
    if config.take_screenshot:
        ssfn = path + folder + "Screenshot---" + i + ".png"     #screenshot file name
        cv2.imwrite(ssfn, Screenshot.screenshot(i, folder))
    if config.take_selfie:
        sffn = path + folder + "\\Selfie---" + i + ".png"       #selfie file name
        cv2.imwrite(sffn, Selfie.selfie(i, folder))
    print(ssfn)
    time.sleep(config.sleep_interval)