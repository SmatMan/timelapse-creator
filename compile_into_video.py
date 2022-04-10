import cv2
import os

img_folder = "out/" # folder with frames
output_name = "output.mp4" # video output name
fps = 30 # frames per second

# grab all frames from img_folder and grab the metadata from the first frame
images = [img for img in os.listdir(img_folder) if img.endswith(".jpg")]
frame = cv2.imread(os.path.join(img_folder, images[0]))
height, width, layers = frame.shape

# initialize the video writer and combine the frames
video = cv2.VideoWriter(output_name, 0, fps, (width,height))
for image in images:
    video.write(cv2.imread(os.path.join(img_folder, image)))

cv2.destroyAllWindows()
video.release()