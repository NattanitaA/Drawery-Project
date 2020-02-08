from time import sleep
import threading
from HomePosition import HomePosition

""" test """
state = "Start"
box = False
num_box = 0
x = HomePosition(19,26,4,CW)
y = HomePosition(20,21,17,CCW)
z = HomePosition(13,6,18,CCW)
def prepare_pos():
    motor_threading1 = threading.Thread(target=x.move,args=(1000,CCW,.0005)) #1000
    motor_threading2 = threading.Thread(target=y.move,args=(1600,CW,.0005)) #1675
    motor_threading3 = threading.Thread(target=z.move,args=(100,CW,.0005))
    motor_threading1.start()
    motor_threading2.start()
    motor_threading3.start()
    motor_threading1.join()
    motor_threading2.join()
    motor_threading3.join()
    state = "Prepare_pos"
    return "Prepare positon"
    
def out():
    state = "move to locker"
    z.move(700,CW,.0005)
    sleep(0.05)
    x.move(3000,CW,.0003)
    sleep(0.05)
    return "OUT"
def lift():
    state = "lifting"
    x.lift = True
    z.lift = True
    x.move(2300,CCW,.0007)
    sleep(0.05)
    z.move(500,CW)
    sleep(0.05)
    x.move(3000,CW,.0007)

    x.lift = False
    z.lift = False
    box = True

    return "LIFT"
def place():
    state = "place the box"
    x.move(3000,CCW,.0005)
    sleep(0.05)
    z.move(500,CCW,.0005)
    sleep(0.05)
    x.move(3000,CW,.0005)
def go_home():
    motor_threading1 = threading.Thread(target=x.return_home,args=()) #1000
    motor_threading2 = threading.Thread(target=y.return_home,args=()) #1675
    motor_threading3 = threading.Thread(target=z.return_home,args=())
    motor_threading1.start()
    motor_threading2.start()
    motor_threading3.start()
    motor_threading1.join()
    motor_threading2.join()
    motor_threading3.join()
    state = "Home"
    return "HOME"
#GPIO.cleanup()

def go_to_locker(n):
    num_box = n
    if n == 1 :
        y.move(1450,CW,.0003)
        state = "locker"
        print("reach locker bot_left")
        lift()
        box = True
        state = "locker with box"
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

    elif n == 2:
        y.move(1300,CCW,.0005)
        print("reach locker bot_right")
        box = True
        state = "locker"
        lift()
        state = "locker with box"
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
        state = "locker"
        lift()
        box = True
        state = "locker with box"
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
        state = "locker"
        print("reach locker top_right")
        lift()
        box = True
        state = "locker with box"
        z.move(2600,CW,.0005)
        sleep(0.05)
        x.move(3000,CCW,.0005)
        sleep(0.05)
        z.move(700,CCW,.0005)

    state = "return pos"
    return

def returnpos_to_locker(n):
    num_box = n
    if n == 4:
        out()
        state = "return_to_locker"
        z.move(2600,CCW,.0005)
        sleep(0.05)
        # x.move(3000,CCW,.0005)
        # sleep(0.05)
        # z.move(500,CCW,.0005)
        # sleep(0.05)
        # x.move(3000,CW,.0005)
        place()
    elif n == 3:
        out()
        state = "return_to_locker"
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
    elif n == 2 :
        out()
        state = "return_to_locker"
        z.move(4600,CCW,.0005)
        sleep(0.05)
        x.move(3000,CCW,.0005)
        sleep(0.05)
        z.move(500,CCW,.0005)
        sleep(0.05)
        x.move(3000,CW,.0005)
    elif n == 1:
        out()
        state = "return_to_locker"
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
    box = False
    num_box = 0
    state = "locker"
    return
def return_home_inter():
    if x.return_home() :
        t1 = threading.Thread(target=y.return_home(),args=())
        t2 = threading.Thread(target=z.return_home(),args=())
        t1.start()
        t2.start()
        t1.join()
        t2.join()
    prepare_pos()
def return_box_inter(n):
    if n == 1 :
        y.move(1450,CW,.0003)
    elif n == 2:
        y.move(1300,CCW,.0005)
    elif n == 3 :
        motor_threading1 = threading.Thread(target=y.move,args=(1450,CW,.0005)) #1000
        motor_threading2 = threading.Thread(target=z.move,args=(2000,CW,.0005)) #1675
        motor_threading1.start()
        motor_threading2.start()
        motor_threading1.join()
        motor_threading2.join()
    elif n == 4 :
        motor_threading1 = threading.Thread(target=y.move,args=(1300,CCW,.0005)) #1000
        motor_threading2 = threading.Thread(target=z.move,args=(2000,CW,.0005)) #1675
        motor_threading1.start()
        motor_threading2.start()
        motor_threading1.join()
        motor_threading2.join()
    place()

def inter():
    x.interupt = True
    y.interupt = True
    z.interupt = True
    while  x.status or y.status or z.status:
        sleep(0.005)
    x.interupt = False
    y.interupt = False
    z.interupt = False
    if state == "Prepare_pos":
        return_home_inter()
        return
    elif state == "locker with box":
        return_home_inter()
        return_box_inter(num_box)
        t1 = threading.Thread(target=x.return_home,args=()) 
        t2 = threading.Thread(target=y.return_home,args=()) 
        t3 = threading.Thread(target=z.return_home,args=()) 
        t1.start()
        t2.start()
        t1.join()
        t2.join()
        return
    elif state  == "return_to_locker" :
        return_home_inter()
        #distance from home to return pos
        pass
        return