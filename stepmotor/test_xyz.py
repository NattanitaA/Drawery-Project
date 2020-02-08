import RPi.GPIO as gpio
from time import sleep
motor_setup = {'X': [20,21],'Y':[19,26],'Z':[5,6]}
CW = 1
CCW = 0

gpio.setmode(gpio.BCM)
def sleepMicro(sec):
    time.sleep(sec/100000)
for i in motor_setup:
    gpio.setup(motor_setup[i][0], gpio.OUT)
    gpio.setup(motor_setup[i][1], gpio.OUT)
    gpio.output(motor_setup[i][0],CW)
    
def move(motor_axis,duration):
    gpio.output(motor_setup[motor_axis][0],CW)
    for x in range(duration):
        gpio.output(motor_setup[motor_axis][1],gpio.HIGH)
        sleep(.0010)
        gpio.output(motor_setup[motor_axis][1],gpio.LOW)
        sleep(.0010)
    gpio.output(motor_setup[motor_axis][0],CCW)
    for x in range(duration):
        gpio.output(motor_setup[motor_axis][1],gpio.HIGH)
        sleep(.0010)
        gpio.output(motor_setup[motor_axis][1],gpio.LOW)
        sleep(.0010)
    print("DONE")
while True:
    try:
        user_input = input()
        move(user_input,3000)
    except KeyboardInterrupt:
        print("clear")
        gpio.cleanup()

