# Wallpaper Engine

**Animated video wallpaper.**

By recording your videos frame by frame, we quickly convert these frames to wallpaper, so you can see the video of the length you want on your desktop in motion. Our process will consist of two stages, Let's see how it works then :). These code fragments were written and run in Linux (Pardus).

Before proceeding with the steps, run the command below to install the necessary python packages.
```linux
pip3 install -r requirements.txt
```


### Frame (first stage)

First and foremost, we need to put an environment variable (wallpaper_engine) into our current directory where its code is located. Sample syntax :
```linux
export wallpaper_engine=$wallpaper_engine:/home/...
```

According to my own index, the example syntax is :
```linux
export wallpaper_engine=$wallpaper_engine:/home/demir/Desktop/asd/
```

Let's see the codes now. frame.py codes available in my code repository : 

```python
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

```

With this code snippet, we save all the frames in our videos to the folder named frame. The syntax required to run this code is (It takes "wallpaper_engine" as argument.)(Depending on the length and quality of the video, the waiting process may take longer.)(Unless you change your video, it is sufficient to run this code once.):
```linux
python3 frame.py --wallpaper_engine $wallpaper_engine
```

![Screenshot_2020-10-23_18-54-10](https://user-images.githubusercontent.com/54184905/97026313-e56bf280-1561-11eb-9a67-174de89e388e.png)

In our current example, 1384 frames came out. And we have completed our first step :).


### Run (second stage)

At this stage, we will quickly make the recorded frames as desktop wallpaper, and if the sound of the video is available in the mp3 directory, this sound will be played back.

Let's see the codes now. run.py codes available in my code repository : 
```python
# export wallpaper_engine=$wallpaper_engine:/home/...
# python3 run.py --wallpaper_engine $wallpaper_engine

import os
import time
import threading
import argparse

ap = argparse.ArgumentParser()

ap.add_argument("-s", "--wallpaper_engine", required=True,help="Wallpaper Engine directory")

args = vars(ap.parse_args())

wallpaper_engine = args["wallpaper_engine"]
wallpaper_engine = wallpaper_engine[1:]

def proca():

	a = wallpaper_engine + "mp3/mp3.mp3"

	kn = None

	if not os.path.isfile(os.path.join(a)):

		kn = True

	if kn==None:

		while True:

			os.system("mpg321 {}".format(a))

aa = threading.Thread(target=proca)

z = len(os.listdir("../asd/frame/"))

aa.start()

while True:

	for i in range(0,z):

		a = wallpaper_engine + "frame/frame{}.jpg".format(i)

		os.system("xfconf-query -c xfce4-desktop -p /backdrop/screen0/monitor0/workspace0/last-image -s \"{}\"".format(a))
		time.sleep(0.01)

```

With this code, we will quickly make all frames as desktop wallpaper so the video we want will play on our desktop. The syntax required to run this code is this (takes the parameter "wallpaper_engine" as an argument) :
```linux
python3 run.py --wallpaper_engine $wallpaper_engine
```

**And the result**

![ezgif com-video-to-gif(1)](https://user-images.githubusercontent.com/54184905/97030836-0c2d2780-1568-11eb-9ef1-0ecf80064dfb.gif)

**Video result**

https://www.linkedin.com/posts/1dfurkan_linux-pardus-unix-activity-6725455211856449536-kpEw


### Things to pay attention

* The video to be played must be in the "video" directory with the name video.mp4.

* If the sound of the video will be played, it must be in the "mp3" directory with the name mp3.mp3.

* In the directory where the script will be run, there should be folders named frame, mp3 and video, and also script scripts named frame.py and run.py should be located in the same directory.

