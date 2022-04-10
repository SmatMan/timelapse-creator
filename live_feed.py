import cv2

# this program displays a live feed of the webcam. used for calibrating the camera.

cam = cv2.VideoCapture(0)

# resolution
cam.set(3, 1280)
cam.set(4, 720)

while True:
    result, image = cam.read()
    cv2.putText(image, "OpenCV", (10, 500), cv2.FONT_HERSHEY_SIMPLEX, 4, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.imshow('OpenCV', image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break