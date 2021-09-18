import cv2
import numpy as np
import time
import HandTracking as ht
import autopy   # Install using "pip install autopy"

pTime = 0
width = 640
height = 480
frameR = 100
smoothening = 8
prev_x, prev_y = 0, 0
curr_x, curr_y = 0, 0

cap = cv2.VideoCapture(0)
cap.set(3, width)
cap.set(4, height)

detector = ht.handDetector(maxHands=1)
screen_width, screen_height = autopy.screen.size()
while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmlist, bbox = detector.findPosition(img)

        if len(lmlist)!=0:
            x1, y1 = lmlist[8][1:]
        x2, y2 = lmlist[12][1:]

        fingers = detector.fingersUp()
        cv2.rectangle(img, (frameR, frameR), (width - frameR, height - frameR), (255, 0, 255), 2)
        if fingers[1] == 1 and fingers[2] == 0: