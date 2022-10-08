import threading

import numpy as np
import cv2
import pyautogui

def screenshot():
	i = 0
	while True:
		print("SS Taken")
		image = pyautogui.screenshot()
		image = cv2.cvtColor(np.array(image),cv2.COLOR_RGB2BGR)
		cv2.imwrite("image" + str(i) + ".png", image)
		i += 1

if __name__ == "__main__":
	thread = threading.Thread(target=screenshot)
	thread.start()