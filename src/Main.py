import time
import datetime
import os
import threading
import pyautogui
import cv2
import numpy as np
import pylab

path = "D:\\WatchdogTesting\\"
folder = ""

def work():
	i = ""
	while True:
		current_time = datetime.datetime.now()
		i = str(current_time.hour) + "hours" + "-" + str(current_time.minute) + "-" + "mins" + str(current_time.second) + "-" + "secs"
		folder = str(current_time.day) + "d-" + str(current_time.month) + "m-" + str(current_time.year) + "y\\"
		if not os.path.exists(path + folder):
			os.makedirs(path + folder)
			print("making folder")
		screenshot(i, folder)
		# selfie(i, folder)
		time.sleep(1)

def screenshot(i, folder):
    image = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(image),cv2.COLOR_RGB2BGR)
    cv2.imwrite(path + folder + "\\Screenshot---" + i + ".png", image)
    print("SS Taken")

def selfie(i, folder):
	cam_port = 0
	cam = cv2.VideoCapture(1,cv2.CAP_DSHOW)
	# cam = cv2.VideoCapture(0)

	result, image = cam.read()

	if result:
		cv2.imwrite(path + folder + "\\WebCam---" + i + ".png", image)
	else:
		print("No image detected. Please! try again")

	print("selfie taken")

def compress():
	pass

def face_rec():
	pass

def get_text(str):
    f = open("config.config.config", "r")
    for x in f:
        if x.startswith(str):
            return x.split("=")[1].strip()
    return "output"



if __name__ == "__main__": 
	t1 = threading.Thread(target=work)
	t1.start()