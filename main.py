#import opencv
import cv2
import time 
import os

files = os.listdir("out/")

print(f"Starting this program will delete all {len(files)} files in the out/ directory. Would you like to continue?")
if input("(y/n): ") == "y":
    for file in files:
        os.remove(f"out/{file}")
    print("All files deleted. Program starting.")




cam = cv2.VideoCapture(0)
cam.set(3, 1280)
cam.set(4, 720)

while True: # callibration
    result, image = cam.read()

    # place text on bottom right and show
    cv2.putText(image, "press y to continue", (10, 500), cv2.FONT_HERSHEY_SIMPLEX, 4, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.imshow('OpenCV', image)

    if cv2.waitKey(1) & 0xFF == ord('y'):
        break

passNum = 0

while True:
    result, image = cam.read()
    # save image
    cv2.imwrite(f'out/image{passNum}.jpg', image)
    print(f"Written image{passNum}.jpg")
    cv2.putText(image, f"{passNum}", (10, 500), cv2.FONT_HERSHEY_SIMPLEX, 4, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.imshow('OpenCV', image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    passNum += 1
    time.sleep(20)