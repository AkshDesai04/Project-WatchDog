class Config:

    sleep_interval = 0  # in ms
    path = "D:\\WatchdogTesting\\"
    take_selfie = True  # Yet to work on
    take_screenshot = True
    multi_diaplay = False  # Yet to work on
    face_recognition = False  # Yet to work on
    keylogger = False  # Yet to work on
    process_logger = False  # Yet to work on

    def getConfigData(path):  # Check if self needs to be added here
        for i in range(0, path.length):
            pass  # Add code to read from file here
