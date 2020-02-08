import RPi.GPIO as GPIO
from time import sleep
import threading
GPIO.setmode(GPIO.BCM)
CW =1
CCW =0

""" test """


GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

class HomePosition(threading.Thread):
    def __init__(self,dir_motor,step_motor,pos_home,CW_CCW,num_sleep=.001):
        threading.Thread.__init__(self)
        self.dir_motor = dir_motor
        self.step_motor = step_motor
        self.pos_home = pos_home
        self.value_switch = GPIO.input(self.pos_home)
        self.CW_CCW = CW_CCW
        self.num_sleep = num_sleep
        GPIO.setup(self.dir_motor, GPIO.OUT)
        GPIO.setup(self.step_motor, GPIO.OUT)
    def limit_switch(self):
        self.value_switch = GPIO.input(self.pos_home)
        return self.value_switch
    def run(self): 
        try:
            GPIO.output(self.dir_motor,self.CW_CCW)
            while True:
                GPIO.output(self.step_motor,GPIO.HIGH)
                sleep(self.num_sleep)
                GPIO.output(self.step_motor,GPIO.LOW)
                sleep(self.num_sleep)
                if self.limit_switch():
                    sleep(0.01)
                    if self.limit_switch():
                        break
            return True
        except:
            print(self.limit_switch())
    def move(self,duration,direction,num2=0.001):
        GPIO.output(self.dir_motor,direction)
        global stop_running
        for _ in range(duration):
            GPIO.output(self.step_motor,GPIO.HIGH)
            sleep(num2)
            GPIO.output(self.step_motor,GPIO.LOW)
            sleep(num2)
        return "DONE"
def prepare_pos():
    x = HomePosition(19,26,4,CW)
    y = HomePosition(20,21,17,CCW)
    z = HomePosition(13,6,18,CCW)
    motor_threading1 = threading.Thread(target=x.move,args=(1000,CCW,.0005)) #1000
    motor_threading2 = threading.Thread(target=y.move,args=(1600,CW,.0005)) #1675
    motor_threading3 = threading.Thread(target=z.move,args=(100,CW,.0005))
    motor_threading1.start()
    motor_threading2.start()
    motor_threading3.start()
    motor_threading1.join()
    motor_threading2.join()
    motor_threading3.join()
    return "Prepare positon"
    
def out():
    x = HomePosition(19,26,4,CW,.001)
    y = HomePosition(20,21,17,CCW,.001)
    z = HomePosition(13,6,18,CCW,.001)
    z.move(700,CW,.0005)
    sleep(0.05)
    x.move(3000,CW,.0003)
    sleep(0.05)
    return "OUT"
def lift():
    x = HomePosition(19,26,4,CW,.0007)
    y = HomePosition(20,21,17,CCW,.0005)
    z = HomePosition(13,6,18,CCW,.0007)
    x.move(2300,CCW,.0007)
    sleep(0.05)
    z.move(500,CW)
    sleep(0.05)
    x.move(3000,CW,.0007)
    return "LIFT"
def go_home():
    x = HomePosition(19,26,4,CW,.0005)
    y = HomePosition(20,21,17,CCW,.0005)
    z = HomePosition(13,6,18,CCW,.0005)
    x.start()
    y.start()
    z.start()
    x.join()
    y.join()
    z.join()
    return "HOME"
#GPIO.cleanup()

def go_to_locker(n):
    x = HomePosition(19,26,4,CW,.0005)
    y = HomePosition(20,21,17,CCW,.0005)
    z = HomePosition(13,6,18,CCW,.0005)
    if n == 1 :
        y.move(1450,CW,.0003)
        print("reach locker bot_left")
        lift()
        motor_threading1 = threading.Thread(target=y.move,args=(2600,CCW,.0003)) #1000
        motor_threading2 = threading.Thread(target=z.move,args=(4400,CW,.0003)) #1675
        motor_threading1.start()
        motor_threading2.start()
        motor_threading1.join()
        motor_threading2.join()
        sleep(0.05)
        x.move(3000,CCW,.0003)
        sleep(0.05)
        z.move(460,CCW,.0005)
        return 'hello im done'
    elif n == 2:
        y.move(1300,CCW,.0005)
        print("reach locker bot_right")
        lift()
        z.move(4400,CW,.0005)
        sleep(0.05)
        x.move(3000,CCW,.0005)
        sleep(0.05)
        z.move(460,CCW,.0005)
    elif n == 3 :
        motor_threading1 = threading.Thread(target=y.move,args=(1450,CW,.0005)) #1000
        motor_threading2 = threading.Thread(target=z.move,args=(2000,CW,.0005)) #1675
        motor_threading1.start()
        motor_threading2.start()
        motor_threading1.join()
        motor_threading2.join()
        print("reach locker top_left")
        lift()
        motor_threading1 = threading.Thread(target=y.move,args=(2700,CCW,.0007)) #1000
        motor_threading2 = threading.Thread(target=z.move,args=(2300,CW,.0007)) #1675
        motor_threading1.start()
        motor_threading2.start()
        motor_threading1.join()
        motor_threading2.join()
        x.move(3000,CCW,.0003)
        sleep(0.05)
        z.move(400,CCW,.0005)
        
    elif n == 4 :
        motor_threading1 = threading.Thread(target=y.move,args=(1300,CCW,.0005)) #1000
        motor_threading2 = threading.Thread(target=z.move,args=(2000,CW,.0005)) #1675
        motor_threading1.start()
        motor_threading2.start()
        motor_threading1.join()
        motor_threading2.join()
        print("reach locker top_right")
        lift()
        z.move(2600,CW,.0005)
        sleep(0.05)
        x.move(3000,CCW,.0005)
        sleep(0.05)
        z.move(700,CCW,.0005)
def returnpos_to_locker(n):
    x = HomePosition(19,26,4,CW,.001)
    y = HomePosition(20,21,17,CCW,.001)
    z = HomePosition(13,6,18,CCW,.001)
    if n == 4:
        out()
        z.move(2600,CCW,.0005)
        sleep(0.05)
        x.move(3000,CCW,.0005)
        sleep(0.05)
        z.move(500,CCW,.0005)
        sleep(0.05)
        x.move(3000,CW,.0005)
        sleep(1)
        return "DONE"
    elif n == 3:
        out()
        sleep(0.05)
        motor_threading1 = threading.Thread(target=y.move,args=(2700,CW,.0005)) #1000
        motor_threading2 = threading.Thread(target=z.move,args=(2700,CCW,.0005)) #1675
        motor_threading1.start()
        motor_threading2.start()
        motor_threading1.join()
        motor_threading2.join()
        sleep(0.05)
        x.move(3000,CCW,.0005)
        sleep(0.05)
        z.move(350,CCW)
        sleep(0.05)
        x.move(3000,CW,.0005)
        return "DONE"
    elif n == 2 :
        out()
        z.move(4600,CCW,.0005)
        sleep(0.05)
        x.move(3000,CCW,.0005)
        sleep(0.05)
        z.move(500,CCW,.0005)
        sleep(0.05)
        x.move(3000,CW,.0005)
        return "DONE"
    elif n == 1:
        out()
        sleep(0.05)
        motor_threading1 = threading.Thread(target=y.move,args=(2600,CW,.0005)) #1000
        motor_threading2 = threading.Thread(target=z.move,args=(4600,CCW,.0005)) #1675
        motor_threading1.start()
        motor_threading2.start()
        motor_threading1.join()
        motor_threading2.join()
        sleep(0.05)
        x.move(3000,CCW,.0005)
        sleep(0.05)
        z.move(500,CCW,.0005)
        sleep(0.05)
        x.move(3000,CW,.0005)
        return "DONE"
def inter1():
    pass