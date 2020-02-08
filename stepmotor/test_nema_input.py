from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
CW =1
CCW =0
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

class HomePosition:
    def __init__(self,dir_motor,step_motor,pos_home,CW_CCW,num_sleep):
        self.dir_motor = dir_motor
        self.step_motor = step_motor
        self.pos_home = pos_home
        self.num_sleep = num_sleep
        self.value_switch = GPIO.input(self.pos_home)
        self.CW_CCW = CW_CCW
        GPIO.setup(self.dir_motor, GPIO.OUT)
        GPIO.setup(self.step_motor, GPIO.OUT)
    def limit_switch(self):
        self.value_switch = GPIO.input(self.pos_home)
        return self.value_switch
    def move(self,num):
        i = 0 
        GPIO.output(self.dir_motor,self.CW_CCW)
        while i <= num :
            GPIO.output(self.step_motor,GPIO.HIGH)
            sleep(self.num_sleep)
            GPIO.output(self.step_motor,GPIO.LOW)
            sleep(self.num_sleep)
            i+=1
x = HomePosition(19,26,4,CCW,.001)
y = HomePosition(20,21,17,CW,.001)
z = HomePosition(13,6,18,CW,.0005)
# Main body of code
try:
    while True:
        user_input = input()
        if user_input == 'x':
            num = int(input())
            x.move(num)
        elif user_input == 'y':
            num = int(input())
            y.move(num)
        elif user_input == 'z':
            num = int(input())
            z.move(num)
        else:
            print("axis not found")
            # lift x = 2300 z = 500 x
            # 1 to return y = 2600 z = 4400 thenx = 3000
            # place z = 460
            # 2 to return z = 4400 then x = 3000
            # 3 to return y = 2700 z = 2300then x = 3000 then z = 380
            # 4 to return z = 2600 then x = 3000 then z = 700
            # return to 3
            # return to 2 z = 500
            # return to 1 z = 500
except KeyboardInterrupt: # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup
    print("Cleaning up!")
    gpio.cleanup
