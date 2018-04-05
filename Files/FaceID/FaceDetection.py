import cv2
import dlib
import time
import os


def ImgforMobilenet(path,name):
        cap = cv2.VideoCapture(path)
        total = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        fps = int(cap.get(cv2.CAP_PROP_FPS))
        duration = int(total/fps)

        start_time = time.time()
        count = 0
        success, image = cap.read()
        while success:
            if (start_time - time.time)%2 == 0:
                count += 1
                success,image = cap.read()
                faceDetect(image)

def faceDetect(img,name):

        facedetector = dlib.get_frontal_face_detector()
        detect = facedetector.run(img,1)
        imageNo = 0
        directory = "Training/image_retraining/data/%s" %(name)
        if not os.path.exists(directory):
            os.mkdir(directory)

        for i,d in enumerate(detect):
            y = d.top()
            x = d.left()
            w = d.right() - x
            h = d.bottom() - y
            cropImg = img[y:(y + h), x:(x + w)]
            cv2.imshow(cropImg)
            imageNo += 1
            path = "%s/%d.png" % (directory, imageNo)
            cv2.imwrite(path,cropImg)



