# Project WatchDog  
This is a security project meant for checking in on what the device has been used to do.  
It can be used as a parenting tool or even a tool to check what your classmate did with your laptop when he took it for making his "presentation"  

## Installation 🚀  
Clone the repository onto your device.    
Create a file with the extention .vbs and write the following code to it 
> CreateObject("Wscript.Shell").Run "<Location of run.bat>",0,True  
    
## Save Readme ✨  
Once you're done, click on the save button to directly save your Readme to your
project's root directory!

- [ ] Aksh
- [x] Desai


# Project WatchDog  

## About the project  
This is a security project meant for checking in on what the device has been used to do.  
It can be used as a parenting tool or even a tool to check what your classmate did with your laptop when he took it for making his "presentation"  

### Need for the project  
  
### How it works?  
The project works with 2 major inputs.  
1. Screenshots  
2. Webcam  
The project takes the above mentioned inputs at a regular interval  
It then runs face recognition on the webcam input and locks the device upon detection of an unauthorized face.  
Every screenshot and webcam input are saved in a folder on the device.  
All of the above mentioned tasks happen on a single thread so as to minimize the impact on the device's performance.  

### Dependencies  
The project in it's current state has the following dependencies...
1. OpenCV
2. face_recognition
  
## Getting Started  
### Installation  
Clone the repository onto your device.    
Create a file with the extension .vbs and write the following code to it 
> CreateObject("Wscript.Shell").Run "<Location of run.bat>",0,True  
  
## Road map  
### Project progress  
### Known Issues  
1. The project can only auto-run on startup for windows.
2. The project files are not protected by any protection layer (Due to this, anyone can just delete or alter the data)
  
## Contribution rules  
## Acknowledgment  
### Contributors and Special thanks  
  
## License  
  
## Contact  