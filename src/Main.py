import time
import datetime
import os
import threading
import pyautogui
import cv2
import numpy as np

def work():
	i = ""
	while True:
		current_time = datetime.datetime.now()
		i = str(current_time.day) + "d-" + str(current_time.month) + "m-" + str(current_time.year) + "y---" + str(current_time.hour) + "hours" + "-" + str(current_time.minute) + "-" + "mins" + str(current_time.second) + "-" + "secs"
		screenshot(i)
		selfie(i)
		time.sleep(10)

def screenshot(i):
    image = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(image),cv2.COLOR_RGB2BGR)

    cv2.imwrite("D:\\Shots\\Screenshot---" + i + ".png", image)
    
    print("Taking a screenshot")

def selfie(i):
	print("Taking a selfie")

def compress():
	print("Compressing images")

def face_rec():
	print("Running face rec")




def get_text(str):
    f = open("config.config.config", "r")
    for x in f:
        if x.startswith(str):
            return x.split("=")[1].strip()
    return "output"



if __name__ == "__main__": 
	t1 = threading.Thread(target=work)
	t1.start()