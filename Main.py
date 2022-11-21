import threading
import time
import datetime
import numpy as np
import cv2
import pyautogui
import os
# import face_recognition

# import Config.py

def work():
	i = ""
	while True:
		current_time = datetime.datetime.now()
		i = str(current_time.day) + "d-" + str(current_time.month) + "m-" + str(current_time.year) + "y---" + str(current_time.hour) + "hours" + "-" + str(current_time.minute) + "-" + "mins" + str(current_time.second) + "-" + "secs"
		# screenshot(i) # temp
		# selfie(i)
		# time.sleep(int(get_text("time")))
		print(get_text("time"))

def screenshot(i):
	image = pyautogui.screenshot()
	image = cv2.cvtColor(np.array(image),cv2.COLOR_RGB2BGR)
	
	cv2.imwrite("D:\\Shots\\Screenshot---" + i + ".png", image)

# def selfie(i):
# 	# TODO: Work on this
# 	print("selfie")

# def compress():
# 	path = "D:\\Shots"
# 	dir_list = os.listdir(path)
# 	for i in range(len(dir_list)):
# 		if dir_list[i].index('---red') == -1:
# 			print("Doing " + dir_list[i])
# 	print("Done")

# def face_rec():
# 	path = "C:\\Users\\Aksh Desai\\Videos\\Test\\Test Data"
# 	dir_list = os.listdir(path)
# 	for i in range(len(dir_list)):
# 		known_image = face_recognition.load_image_file("C:\\Users\\Aksh Desai\\Videos\\Test\\Known People\\Rachel.jpg")
# 		unknown_image = face_recognition.load_image_file("C:\\Users\\Aksh Desai\\Videos\\Test\\Test Data\\" + dir_list[i])

# 		biden_encoding = face_recognition.face_encodings(known_image)[0]
# 		unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

# 		results = face_recognition.compare_faces([biden_encoding], unknown_encoding)

# 		print(results)




def get_text(str):
    f = open("config.config.config", "r")
    for x in f:
        if x.startswith(str):
            return x.split("=")[1].strip()
    return "output"



if __name__ == "__main__":
	t1 = threading.Thread(target=work)
	t1.start()
	# # t2 = threading.Thread(target=compress)
	# # t2.start()
	# t3 = threading.Thread(target=face_rec)
	# t3.start()