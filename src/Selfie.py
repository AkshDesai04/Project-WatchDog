import cv2


def selfie():
    cam = cv2.VideoCapture(0)
    result, image = cam.read()
    if result:
        print("Selfie Taken")
        return image
    else:
        print("No image detected. Please! try again")
    print("selfie taken")