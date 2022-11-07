import threading
import time
import datetime

import numpy as np
import cv2
import pyautogui

def work():
	i = ""
	while True:
		current_time = datetime.datetime.now()
		i = str(current_time.day) + "d-" + str(current_time.month) + "m-" + str(current_time.year) + "y---" + str(current_time.hour) + "hours" + "-" + str(current_time.minute) + "-" + "mins" + str(current_time.second) + "-" + "secs"
		screenshot(i)
		# selfie(i)
		time.sleep(10)

def screenshot(i):
	image = pyautogui.screenshot()
	image = cv2.cvtColor(np.array(image),cv2.COLOR_RGB2BGR)
	cv2.imwrite("D:\\Shots\\Screenshot-" + i + ".png", image)

def selfie(i):
	# TODO: Work on this
	print("selfie")

if __name__ == "__main__":
	t1 = threading.Thread(target=work, args=())
	t1.start()