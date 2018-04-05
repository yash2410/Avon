import threading
import os
import cv2
import dlib
from time import time
from Files import IntentsandRoom as ir
from Files.SpeechRecognition import speechDandR as sdr

def Speech():

            while True:
                text = sdr.speechRecognition()
                response  = sdr.speechPrediction(text)
                intent , room = sdr.JSONresponse(response)
                ir.getState(intent,room)

def videoCapture():
        startTime = time()
        print("starting")
        cap = cv2.VideoCapture(0)
        faceDetector = dlib.get_frontal_face_detector()
        predictor = dlib.shape_predictor()
        count = 0
        while True:
            count += 1
            success, img = cap.read()
            img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
            detect = faceDetector(img,1)
            print(".....")
            for i, d in enumerate(detect):
                print(d.left(), d.top(), d.right(), d.bottom())
                y = d.top()
                x  = d.left()
                w = d.right() - x
                h = d.bottom() - y
                RectImg = cv2.rectangle(img,(d.left(), d.top()), (d.right(), d.bottom()), (255, 0, 255), 2)
                cropImg = img[y:(y+h),x:(x+w)]
                cv2.imshow("rectCrop", RectImg)
                if not os.path.exists("data"):
                    os.mkdir("data")
                cv2.imwrite("data/detected_face.jpg", cropImg)
                cv2.waitKey(5)


v_thread = threading.Thread(videoCapture())
s_thread = threading.Thread(Speech())

