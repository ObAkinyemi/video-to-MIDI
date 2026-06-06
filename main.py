from __future__ import print_function
import cv2 as cv
import argparse

# opening a video in opencv
video = cv.VideoCapture('song2.mp4')

# 2. Safety check: make sure Python actually found and opened the file
if not video.isOpened():
    print(f"could not open video file. check file name!")
    exit(0)


width = int(video.get(cv.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv.CAP_PROP_FRAME_HEIGHT))

# 4. Print the numbers to your terminal so we can prove it works
print("--- Phase 0 Success ---")
print(f"Video successfully loaded!")
print(f"Width: {width} pixels")
print(f"Height: {height} pixels")

scanLineHeight = 0.7*height
whiteKeyWidth = float(width/52)
whiteKeyCheckPoint = float(whiteKeyWidth/2)

keys = []
for key in range(0,51):
    

# 5. Close the video pipeline to clean up your computer's memory
video.release()



# while True:
#     ret, frame = capture.read()
#     if frame is None:
#         break

#     fgMask = backSub.apply(frame)

#     cv.rectangle(frame, (10, 2), (100,20), (255,255,255), -1)
#     cv.putText(frame, str(capture.get(cv.CAP_PROP_POS_FRAMES)), (15, 15),
#                cv.FONT_HERSHEY_SIMPLEX, 0.5 , (0,0,0))

#     cv.imshow('Frame', frame)
#     cv.imshow('FG Mask', fgMask)

#     keyboard = cv.waitKey(30)
#     if keyboard == 'q' or keyboard == 27:
#         break