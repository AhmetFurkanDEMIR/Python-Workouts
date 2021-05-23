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

