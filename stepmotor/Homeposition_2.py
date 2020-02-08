import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
CW =1
CCW =0

GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

class HomePosition():
    def __init__(self,name,dir_motor,step_motor,pos_home,CW_CCW,num_sleep=.0003):
        self.name = name
        self.dir_motor = dir_motor
        self.step_motor = step_motor
        self.pos_home = pos_home
        self.value_switch = GPIO.input(self.pos_home)
        self.CW_CCW = CW_CCW
        self.num_sleep = num_sleep
        GPIO.setup(self.dir_motor, GPIO.OUT)
        GPIO.setup(self.step_motor, GPIO.OUT)
        self.interrupt = False
        self.lift = False
        self.status = False
    def limit_switch(self):
        self.value_switch = GPIO.input(self.pos_home)
        return self.value_switch
    def return_home(self):
        GPIO.output(self.dir_motor,self.CW_CCW)
        try:
            self.interrupt = True
            while True:
                GPIO.output(self.step_motor,GPIO.HIGH)
                sleep(self.num_sleep)
                GPIO.output(self.step_motor,GPIO.LOW)
                sleep(self.num_sleep)
                if self.limit_switch():
                    sleep(0.005)
                    if self.limit_switch():
                        break
            return True
        except:
            print(self.limit_switch())
            sleep(0.005)
            if self.limit_switch():
                self.return_home()
        finally:
            self.interrupt = False
    def move(self,duration,direction,num2=0.003):
        GPIO.output(self.dir_motor,direction)
        if self.status:
            print("BUSY")
        self.status = True
        print(self.name,"move_function")
        for _ in range(duration):
            if self.interrupt and not self.lift :
                self.status = False
                print("Interrupted")
                return "Interrupt"
            GPIO.output(self.step_motor,GPIO.HIGH)
            sleep(num2)
            GPIO.output(self.step_motor,GPIO.LOW)
            sleep(num2)
        self.status = False
        return "DONE"
