# export wallpaper_engine=$wallpaper_engine:/home/...
# python3 frame.py --wallpaper_engine $wallpaper_engine

import cv2 
import os
import argparse

ap = argparse.ArgumentParser()

ap.add_argument("-s", "--wallpaper_engine", required=True,help="Wallpaper Engine directory")

args = vars(ap.parse_args())

wallpaper_engine = args["wallpaper_engine"]
wallpaper_engine = wallpaper_engine[1:]

cam=cv2.VideoCapture(wallpaper_engine+"video/video.mp4")

i = 0

while True:
    _,frame=cam.read()
    a = wallpaper_engine+"frame/frame{}.jpg".format(i)
    cv2.imwrite(a,frame)
    i+=1


cam.release()
cv2.destroyAllWindows()
