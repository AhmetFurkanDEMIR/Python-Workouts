import cv2
import mediapipe as mp
import subprocess
from Xlib import display, X
from Xlib.ext.xtest import fake_input
import numpy as np

class HandPos():

    def __init__(self):

        output = subprocess.Popen('xrandr | grep "\*" | cut -d" " -f4',shell=True, stdout=subprocess.PIPE).communicate()[0]
        resolution = output.split()[0].split(b'x')
        self.width = int(resolution[0])
        self.height = int(resolution[1])

        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_drawing_styles = mp.solutions.drawing_styles
        self.mp_hands = mp.solutions.hands

        self.hands = self.mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.8)

        self.cap = cv2.VideoCapture(0)

        self.xPrevPress = 0
        self.yPrevPress = 0

        self.xPrevMove = 0
        self.yPrevMove = 0

        self.firstFlag = None


    def capRead(self):
  
        success, image = self.cap.read()

        if not success:

            print("Ignoring empty camera frame.")

            return


        self.frame = np.zeros((0, 0, 3), dtype=np.uint8)

        image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)

        image.flags.writeable = False
        results = self.hands.process(image)

        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        x = 0
        y = 0
    
        if results.multi_hand_landmarks:

            for hand_landmarks in results.multi_hand_landmarks:

                x = hand_landmarks.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_TIP].x * self.width
                y = hand_landmarks.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_TIP].y * self.height

                if self.firstFlag==None:

                    self.firstFlag=True

                    self.xPrevPress = x
                    self.yPrevPress = y

                    break

                d = display.Display()
                s = d.screen()

                if not ((x < self.xPrevPress + 45 and x > self.xPrevPress -45) and (y < self.yPrevPress + 45 and y > self.yPrevPress - 45)):

                    a = self.width/3

                    if x < a:

                        nmb = 100

                    elif x < a+a/2:

                        nmb = 90

                    else:

                        nmb = 30

                        if x > a+a:

                            nmb = 20

                    if hand_landmarks.landmark[self.mp_hands.HandLandmark.THUMB_TIP].x * self.width + nmb > hand_landmarks.landmark[self.mp_hands.HandLandmark.WRIST].x * self.width:

                        fake_input(d, X.ButtonPress, 1)
                        d.sync()
                        fake_input(d, X.ButtonRelease, 1)
                        d.sync()

                        self.xPrevPress = x
                        self.yPrevPress = y


                if not ((x < self.xPrevMove + 5 and x > self.xPrevMove -5) and (y < self.yPrevMove + 5 and y > self.yPrevMove - 5)):

                    root = s.root
                    root.warp_pointer(int(x),int(y))
                    d.sync()

                    self.xPrevMove = x
                    self.yPrevMove = y

                self.frame = np.zeros((600, 600, 3), dtype=np.uint8)

                self.mp_drawing.draw_landmarks(
                  self.frame,
                  hand_landmarks,
                  self.mp_hands.HAND_CONNECTIONS,
                  self.mp_drawing_styles.get_default_hand_landmarks_style(),
                  self.mp_drawing_styles.get_default_hand_connections_style())
                
                medX = 999
                larX = -999

                medY = 999
                larY = -999

                for i in hand_landmarks.landmark:

                    if i.x > larX:

                        larX = i.x

                    if i.x<medX:

                        medX = i.x

                    if i.y > larY:

                        larY = i.y

                    if i.y < medY:

                        medY = i.y

                larX = int(larX*600) + 5
                larY = int(larY*600) + 5
                medX = int(medX*600) - 5
                medY = int(medY*600) - 5

                self.frame = self.frame[medY:medY+(larY-medY),medX:medX+(larX-medX)].copy()

                wi = self.frame.shape[0]
                hi = self.frame.shape[1]

                z = np.zeros((600, 600,4), dtype=np.uint8)

                self.frame = np.dstack((self.frame, np.full((wi,hi),255)))

                trans_mask = self.frame[:,:,2] == 0
                self.frame[trans_mask] = np.zeros(4, dtype=np.uint8)

                z[0:wi,0:hi] = self.frame.copy()

                self.frame=z.copy()

        return self.frame, x,y
            

if __name__ == "__main__":
    a = HandPos()

    while True:

        a.capRead()