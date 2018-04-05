from flask import Flask
#, render_template, url_for, request, session, redirect, send_from_directory
#from Files.FaceID import FaceDetection as fdr
from Files.SpeechRecognition import speechDandR as sdr
import serial
import json
#import pytransmit
import os
import subprocess
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
app = Flask(__name__)

@app.route('/')
def index():
    return 'Avon Index'

@app.route('/query/<text>')
def query(text):

    i,r = sdr.speechPrediction(text=text)
    print(i,r)

    send_inst = True

    on = 'smarthome.lights.switch.on'
    off = 'smarthome.lights.switch.off'

    gar = 'garage'
    bed = 'bedroom'
    kit = 'kitchen'
    bath = 'bathroom'

    if i == on:
        if r == gar:
            #ard.digitalWrite(2,'HIGH')
            print(r)
            ser.write(b'1')
        elif r == bed:
            #ard.digitalWrite(3,'HIGH')
            print(r)
            ser.write(b'2')
        elif r == kit:
            #ard.digitalWrite(4, 'HIGH')
            print(r)
            ser.write("3".encode())
            print(ser.write("3".encode()))
        elif r == bath:
            #ard.digitalWrite(5,'HIGH')
            print(r)
            ser.write(b'4')
        else:
            print("Unknown Room")
    else:
        print('On Unkown Intent')

    if i == off:
        if r == gar:
            #ard.digitalWrite(2,'HIGH')
            print(r)
            ser.write("5".encode())
        elif r == bed:
            #ard.digitalWrite(3,'HIGH')
            print(r)
            ser.write("6".encode())
        elif r == kit:
            #ard.digitalWrite(4, 'HIGH')
            print(r)
            ser.write("7".encode())
        elif r == bath:
            #ard.digitalWrite(5,'HIGH')
            print(r)
            ser.write("8".encode())
        else:
            print("Unknown Room")
    else:
        print("Off Unknown Intent")

    #sdr.JSONresponse(response=response)
    #ir.getState(intent= intent, room = room)
    # here you'll be running dialogflow api
    # to get intents
    # create new classes for each intent.
    # Class Actions , light
    # Light on'- method(which light)

    return json.dumps({'room':r, 'intent':i})
'''
@app.route('/trainingvideo/<name>')
def trainingVideo(name):
    ftp = pytransmit.FTPClient()
    directory = '/home/yash/Documents/Avon/Video'
    if not os.path.exists(directory):
        os.mkdir(directory)
    ftp.change_directory(directory)
    ftp_HOST = '0.0.0.0'
    ftp_PORT = '5000'

    ftp.connect(ftp_HOST,ftp_PORT)
    ftp.download_file('%s.mp4'%name)
    path = "%s/%s"%(directory,name)
    fdr.ImgforMobilenet(path=path,name=name)

    subprocess.call(["python3 /Training/image_retraining/retrain.py",
                     "--image dir /Training/image_retraining/data/",
                     "--learning_rate = 0.0001",'--testing_percentage =10',
                     '--validation_percentage =10',
                     '--train_batch_size = 30',
                     '--validation_batch_size = -30',
                     '--flip_left_right True',
                     '--random_scale = 10',
                     '--random_brightness = 10',
                     '--eval_step_interval = 10',
                     '--how_many_training_steps = 10',
                     '--architecture mobilenet_1.0_224'],
                    shell=False)


    return json.dumps({'Added User':name})
'''

if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run(host='0.0.0.0', port=8000, debug=True)
