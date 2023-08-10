import datetime
import cv2
import database_operations
import time


def start_data_capture(con, interval):
    while True:
        image = selfie()
        now = datetime.now()

        database_operations.db_insert(con, 'Selfies', {image, now})

        time.sleep(interval)


def selfie():
    cam = cv2.VideoCapture(0)
    result, image = cam.read()
    if result:
        print("Selfie Taken")
        return image
    else:
        print("No image detected. Please! try again")
    print("selfie taken")