import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
while True:
    x_axis = GPIO.input(4)
    y_axis = GPIO.input(24)
    z_axis = GPIO.input(18)
    
    print([x_axis,y_axis,z_axis])
    if x_axis == True and y_axis == True and z_axis == True:
        print("HOME POSITION")