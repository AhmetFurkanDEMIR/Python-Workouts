from flask import Flask,render_template,flash,redirect,url_for,request, Response
import cv2
import time
import os
import torch
import math
import threading

app = Flask(__name__)
app.secret_key= "demirai"

global cap
global model
global frameMain

Video_path = "http://konya.sehirkameralari.com/live/52f8ad56da5f9/playlist.m3u8?token="
cap = cv2.VideoCapture(Video_path)

model = torch.hub.load('ultralytics/yolov5', 'yolov5x', pretrained=True)

def ThreadFrame():

    while True:

        ret, img = cap.read()

        if ret == True:
            frame = cv2.resize(img, (0,0), fx=0.5, fy=0.5) 

            results = model(frame)

            hummanXY = []

            for i in results.xyxy[0]:

                if i[5]==0:

                    x = int(i[0]+((i[2]-i[0])/2))
                    y = int(i[1]+((i[3]-i[1])/2))

                    hummanXY.append([x,y])
                    cv2.circle(frame,(x,y), 5, (0,204,0), -1)

            count = 0

            for i in range(0, len(hummanXY)):

                for j in range(i+1, len(hummanXY)):

                    hummanM = hummanXY[i]
                    hummanT = hummanXY[j]

                    if math.sqrt((hummanM[0]-hummanT[0])**2+(hummanM[1]-hummanT[1])**2)<30:

                        cv2.line(frame,(hummanM[0],hummanM[1]),(hummanT[0],hummanT[1]),(0,0,255),3)
                        cv2.circle(frame,(hummanM[0],hummanM[1]), 5, (0,0,255), -1)
                        cv2.circle(frame,(hummanT[0],hummanT[1]), 5, (0,0,255), -1)

                        count+=1

                    else:

                        cv2.line(frame,(hummanM[0],hummanM[1]),(hummanT[0],hummanT[1]),(96,96,96),1)

            if count!=0:

              cv2.putText(frame, "Social Distancing X : {}".format(count), (frame.shape[0]-30,45), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255),1)
            
            else:

              cv2.putText(frame, "Social Distancing", (frame.shape[0]+65,45), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,204,0),1)

            frame = cv2.imencode('.jpg', frame)[1].tobytes()

            global frameMain
            frameMain = frame

t1 = threading.Thread(target=ThreadFrame, args = ())
t1.start()

def gen():

    while True:
        
        yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frameMain + b'\r\n')



@app.route("/video_feed/<string:idd>")
def video_feed(idd):

    return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route("/",methods =["GET","POST"])
def login():

    return render_template("capture.html", count=1)



if __name__ == "__main__":

    app.run(host="0.0.0.0", port=80)


