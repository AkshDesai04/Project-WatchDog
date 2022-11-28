# Project WatchDog  
  
## About the project  
This is a security project meant for checking in on what the device has been used to do.  
It can be used as a parenting tool or even a tool to check what your classmate did with your laptop when he took it for making his "presentation"  
  
### How it works?  
The project works with 2 major inputs.  
1. Screenshots  
2. Webcam  
 - The project takes the above mentioned inputs at a regular interval  
 - It then runs face recognition on the webcam input and locks the device upon detection of an unauthorized face.  
 - Every screenshot and webcam input are saved in a folder on the device.  
 - All of the above mentioned tasks happen on a single thread so as to minimize the impact on the device's performance.  
  
### Dependencies  
The project in it's current state has the following dependencies...  
1. OpenCV  
2. face_recognition  
  
## Getting Started  
### Installation  
#### Windows  
 . Clone the repository onto your device.  
 . Create a file with the extension .vbs and write the following code to it  
 . `CreateObject("Wscript.Shell").Run "<Location of run.bat>",0,True`  
 . Save the above mentioned file to the location `C:\Users\<User Name>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\`  
 . Save the `run.bat` file to preferably a root location (something like `C:\`) since .vbs files cannot have spaces in their paths. (Issues might arise If `run.bat` is saved in a path which contains spaces such as in user names)  
 . Replace the `<Project Location>` in `run.bat` with the location where the project is saved  
 . Set the config.config file to your desired settings (architecture for config.config is not built yet and hence, settings need to be changed manually from the code)  
 . Install the dependencies for the project by running the command `pip install -r requirements.txt`  
 . Project WatchDog will start running after a restart  
  
## Road map  
### Project progress  
- [x] Run the project on startup without any obvious signs of it running  
- [x] Run the project on a single thread so as to reduce performance impact on the system  
- [x] Take screenshots at regular intervals  
    - [ ] Add support for multiple display screenshots  
- [ ] Take webcam images at regular intervals  
- [ ] Key log each key stroke and key combination  
- [ ] Run face recognition on the webcam images  
    - [ ] If new face is detected, save it for admin to later name the face, merge the face or discard the face  
    - [ ] Have a notification saying hi if a known person is detected using the device  
- [ ] Compress existing images on a regular internal to save storage  
- [ ] Lock device if unauthorized face is recognized  
- [ ] Organize the files in a proper folder system  
- [ ] Restrict access to the files from the user to prevent an attacker from deleting and/or altering files  
- [ ] Add config file to allow user to manually set the settings or themselves  
  
### Known Issues  
1. The project can only auto-run on startup for windows.  
2. The project files are not protected by any protection layer (Due to this, anyone can just delete or alter the data)  
  
## Contribution rules  
To contribute to the project, please fork the project and submit any contributions through Pull Requests.  
Thanks for the contributions :)  
  
## Acknowledgment  
### Contributors and Special thanks  
<a href="https://github.com/AkshDesai04/Project-WatchDog/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=AkshDesai04/Project-WatchDog" />
</a>  
  
## License  
The project is protected under the [GNU General Public License v3.0](./LICENSE.md)  
  
## Contact  
To notify regarding non-fatal issues, please use the Issues section of the repository.  
For fatal and/or security related issues, please contact me through email at dev.akshdesai@gmail.com  