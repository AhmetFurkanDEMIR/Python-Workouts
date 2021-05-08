import pyautogui
import cv2
import mss
import numpy as np
import threading
import time

monitor = {'top': 0, 'left': 0, 'width': 1366, 'height': 768}
sct = mss.mss()

color_space_up = np.array([90, 90, 90], np.uint8)
color_space_dow = np.array([70, 70, 70], np.uint8)

color_black = np.array([0, 0, 0], np.uint8)
color_white = np.array([255, 255, 255], np.uint8)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 80, (1366,768))


def thre_space():

	pyautogui.keyDown('space')
	time.sleep(0.3)
	pyautogui.keyUp('space')


while True:

	img = np.array(sct.grab(monitor))
	frame = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

	cv2.rectangle(frame, pt1=(480,190), pt2=(560,240), color=(0,0,255), thickness=3)
	squ0 = frame[190:240, 480:560, :]

	cv2.rectangle(frame, pt1=(110,214), pt2=(176,338), color=(0,0,255), thickness=3)
	squ1 = frame[214:338, 110:176, :]


	mask = cv2.inRange(squ0, color_space_dow, color_space_up)
	kernal = np.ones((5, 5), "uint8")
	black_mask0 = cv2.dilate(mask, kernal)
	res_red = cv2.bitwise_and(squ0, squ0, mask = black_mask0)
	contours, hierarchy = cv2.findContours(black_mask0, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


	for pic, contour in enumerate(contours):
		area = cv2.contourArea(contour)
		if(area > 300):
			a = threading.Thread(target=thre_space)
			a.start()

	mask = cv2.inRange(squ1, color_black, color_black)
	kernal = np.ones((5, 5), "uint8")
	black_mask0 = cv2.dilate(mask, kernal)
	res_red = cv2.bitwise_and(squ1, squ1, mask = black_mask0)
	contours, hierarchy = cv2.findContours(black_mask0, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


	for pic, contour in enumerate(contours):
		area = cv2.contourArea(contour)
		if(area > 300):	
			color_space = np.array([172, 172, 172], np.uint8)

			color_space_up = np.array([185, 185, 185], np.uint8)
			color_space_dow = np.array([165, 165, 165], np.uint8)


	mask = cv2.inRange(squ1, color_white, color_white)
	kernal = np.ones((5, 5), "uint8")
	black_mask0 = cv2.dilate(mask, kernal)
	res_red = cv2.bitwise_and(squ1, squ1, mask = black_mask0)
	contours, hierarchy = cv2.findContours(black_mask0, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


	for pic, contour in enumerate(contours):
		area = cv2.contourArea(contour)
		if(area > 300):	
			color_space_up = np.array([90, 90, 90], np.uint8)
			color_space_dow = np.array([70, 70, 70], np.uint8)



	frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
	out.write(frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

out.release()