import cv2


def selfie(i, folder):  # TODO: Remove parameters coz i and folder are already managed by the Main.py file
    cam = cv2.VideoCapture(0)
    result, image = cam.read()
    if result:
        print("Selfie Taken")
        return image
    else:
        print("No image detected. Please! try again")
    print("selfie taken")
