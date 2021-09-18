# Virtual Mouse Using OpenCV
In this project we will be using the live feed coming from the webcam to create a virtual mouse.

## Project Description:
In this project, I am using my hand as a virtual mouse than can do everything that a mouse does without even touching your system. I am using the webcam of my system to detect my hands. It will then create a bounding box around my hand and focus on two fingers: The fore finger and the middle finger. The fore finger will act as a cursor and moving it around, we will be moving the cursor around. Now, inorder to successfully click using hand tracking, it is detecting the distance between the fore finger and the middle finger. If they are joined together, then it will perform a click. 

Furthermore, a smoothness factor was added as the movement was really shaky.

## Requirements:
Following modules need to be installed for it to work properly:
- OpenCV
- Mediapipe
- Autopy

### OpenCV:
OpenCV is a huge open-source library for computer vision, machine learning, and image processing. OpenCV supports a wide variety of programming languages like Python, C++, Java, etc. It can process images and videos to identify objects, faces, or even the handwriting of a human.

It can be installed using "pip install opencv-python"


### Mediapipe:
MediaPipe is a framework for building multimodal (eg. video, audio, any time series data), cross platform (i.e Android, iOS, web, edge devices) applied ML pipelines.

It can be installed using "pip install mediapipe"

### Autopy:
AutoPy is a simple, cross-platform GUI automation library for Python. It includes functions for controlling the keyboard and mouse, finding colors and bitmaps on-screen, and displaying alerts.

It can be installed using "pip install autopy"

## Important Note:
I faced alot of dependency issues throughout this project. Some of the issues and their solutions are as follows:
- autopy not installing: This is because autopy currently doesn't support Python versions above 3.8
- webcam not opening: It was a bug in mediapipe and was fixed in latest python versions

Hence, inorder for the project to run smoothly, you need to 