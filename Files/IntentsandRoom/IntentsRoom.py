import serial

def getState(i, r):

    ser = serial.Serial('COM3', 9600, timeout=1)
    send_inst = True

    on = 'smarthome.lights.switch.on'
    off = 'smarthome.lights.switch.off'

    gar = 'garage'
    bed = 'bedroom'
    kit = 'kitchen'
    bath = 'bathroom'

    print(i == on,i == off)

    if i == on:
        if r == gar:
            #ard.digitalWrite(2,'HIGH')
            print(r)
            ser.write("1".encode())
            print(ser.write("1".encode()))
        elif r == bed:
            #ard.digitalWrite(3,'HIGH')
            print(r)
            ser.write("2".encode())
            print(ser.write("2".encode()))
        elif r == kit:
            #ard.digitalWrite(4, 'HIGH')
            print(r)
            ser.write("3".encode())
            print(ser.write("3".encode()))
        elif r == bath:
            #ard.digitalWrite(5,'HIGH')
            print(r)
            ser.write("4".encode())
            print(ser.write("4".encode()))
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

'''
python retrain.py --image_dir data --learning_rate 0.001 --testing_percentage 10 --validation_percentage 10 --train_batch_size 32 --validation_batch_size -1 --flip_left_right True --random_scale 10 --random_brightness 10 --eval_step_interval 5 --how_many_training_steps 20 --architecture mobilenet_1.0_128
'''
