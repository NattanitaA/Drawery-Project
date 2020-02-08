from time import sleep
import threading
from Homeposition_2 import HomePosition
CW =1
CCW =0
""" test """
state = "Start"
#box = False
num_box = 0
x = HomePosition('x',19,26,15,CW,.00025) #[dir,step]
y = HomePosition('y',20,21,17,CCW,.00025)
z = HomePosition('z',13,6,18,CCW,.0003)
def prepare_pos():
    global state
    global x,y,z
    motor_threading1 = threading.Thread(target=x.move,args=(1000,CCW,.0003)) #1000
    motor_threading2 = threading.Thread(target=y.move,args=(1600,CW,.0003)) #1675
    motor_threading3 = threading.Thread(target=z.move,args=(150,CW,.0003))
    motor_threading1.start()
    motor_threading2.start()
    motor_threading3.start()
    motor_threading1.join()
    motor_threading2.join()
    motor_threading3.join()
    state = "Prepare_pos"
    return "Prepare positon"
    
def update_inter(condition):
    global x,y,z
    x.interrupt = condition
    y.interrupt = condition
    z.interrupt = condition

def prepare_pos2():
    motor_threading2 = threading.Thread(target=y.move,args=(1600,CW,.0003)) #167
    motor_threading2.start()
    motor_threading2.join()
    return "Prepare positon"    
def out():
    global state
    #state = "move to locker"
    z.move(700,CW,.00035)
    sleep(0.05)
    x.move(3000,CW,.0003)
    sleep(0.05)
    return "OUT"
def lift():
    global state
    state = "lifting"
    x.lift = True
    z.lift = True
    print("lifting")
    x.move(2300,CCW,.0003)
    sleep(0.05)
    z.move(500,CW,.00035)
    sleep(0.05)
    x.move(3000,CW,.0003)

    x.lift = False
    z.lift = False
    state = "locker with box"
    #box = True

    return "LIFT"
def place():
    #state = "place the box"
    x.move(2920,CCW,.0004)
    sleep(0.05)
    z.move(600,CCW,.0006)
    sleep(0.05)
    y.move(300,CW,.0007)
    sleep(0.2)
    y.move(500,CCW,.0007)
    x.move(3000,CW,.0004)
    sleep(0.2)
    return
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
    global state
    global num_box
    num_box = n
    if n == 3 :
        y.move(1500,CW,.0003)
        z.move(30,CCW,.0003)
        state = "locker"
        sleep(1)
        if not x.interrupt and not y.interrupt and not z.interrupt:
            print("lifting the box")
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
        z.move(460,CCW,.0003)
        

    elif n == 4:
        y.move(1350,CCW,.0003)
        state = "locker"
        sleep(1)
        if not x.interrupt and not y.interrupt and not z.interrupt:
            print("lifting the box")
            lift()
        z.move(4400,CW,.0003)
        sleep(0.05)
        x.move(3000,CCW,.0003)
        sleep(0.05)
        z.move(460,CCW,.0003)

    elif n == 2 :
        state = "locker"
        motor_threading1 = threading.Thread(target=y.move,args=(1500,CW,.0003)) #1000
        motor_threading2 = threading.Thread(target=z.move,args=(1980,CW,.0003)) #1675
        motor_threading1.start()
        motor_threading2.start()
        motor_threading1.join()
        motor_threading2.join()
        sleep(1)
        if not x.interrupt and not y.interrupt and not z.interrupt:
            print("lifting the box")
            lift()
        motor_threading1 = threading.Thread(target=y.move,args=(2700,CCW,.0003)) #1000
        motor_threading2 = threading.Thread(target=z.move,args=(2300,CW,.0003)) #1675
        motor_threading1.start()
        motor_threading2.start()
        motor_threading1.join()
        motor_threading2.join()
        x.move(3000,CCW,.0003)
        sleep(0.05)
        z.move(400,CCW,.0003)

    elif n == 1 :
        state = "locker"
        motor_threading1 = threading.Thread(target=y.move,args=(1350,CCW,.0003)) #1000
        motor_threading2 = threading.Thread(target=z.move,args=(2000,CW,.00032)) #1675
        motor_threading1.start()
        motor_threading2.start()
        motor_threading1.join()
        motor_threading2.join()
        print("reach locker top_right")
        sleep(1)
        print(not x.interrupt and not y.interrupt and not z.interrupt)
        if not x.interrupt and not y.interrupt and not z.interrupt:
            print("lifting the box")
            lift()
        z.move(2600,CW,.00032)
        x.move(3000,CCW,.0003)
        z.move(700,CCW,.00032)
    print("1234")
    update_inter(False)
    return

def returnpos_to_locker(n):
    global state
    global num_box
    num_box = n
    state = "return_to_locker"
    if n == 1:
        out()
        z.move(2540,CCW,.0003)
        place()
    elif n == 2:
        out() 
        motor_threading1 = threading.Thread(target=y.move,args=(2700,CW,.0003)) #1000
        motor_threading2 = threading.Thread(target=z.move,args=(2525,CCW,.0003)) #1675
        motor_threading1.start()
        motor_threading2.start()
        motor_threading1.join()
        motor_threading2.join()
        place()
    elif n == 4 :
        out()
        z.move(4600,CCW,.0003)
        place()
    elif n == 3:
        out()
        motor_threading1 = threading.Thread(target=y.move,args=(2610,CW,.0003)) #1000
        motor_threading2 = threading.Thread(target=z.move,args=(4600,CCW,.0003)) #1675
        motor_threading1.start()
        motor_threading2.start()
        motor_threading1.join()
        motor_threading2.join()
        place()
    update_inter(False)
    #box = False
    num_box = 0
    return
def return_home_inter():
    print("Returing Home Mode : interrupt")
    x.return_home()
    t1 = threading.Thread(target=y.return_home,args=())
    t2 = threading.Thread(target=z.return_home,args=())
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    z.return_home()
    
    print("HOME")
    return
def return_home_inter2():
    z.return_home()
    x.return_home()
    y.return_home()
    print("HOME")
    return

def return_box_inter(n):
    if n == 3 :
        motor_threading1 = threading.Thread(target=y.move,args=(1400,CW,.0003))
        motor_threading2 = threading.Thread(target=z.move,args=(700,CW,.0003))
        motor_threading1.start()
        motor_threading2.start()
        motor_threading1.join()
        motor_threading2.join()
        x.move(250,CCW,.0003)
    elif n == 4:
        motor_threading1 = threading.Thread(target=y.move,args=(1400,CCW,.0003))
        motor_threading2 = threading.Thread(target=z.move,args=(1000,CW,.0003))
        motor_threading1.start()
        motor_threading2.start()
        motor_threading1.join()
        motor_threading2.join()
        x.move(300,CCW,.0003)
    elif n == 2 :
        motor_threading1 = threading.Thread(target=y.move,args=(1480,CW,.0003)) #1000
        motor_threading2 = threading.Thread(target=z.move,args=(2680,CW,.0003)) #1675
        motor_threading1.start()
        motor_threading2.start()
        motor_threading1.join()
        motor_threading2.join()
        x.move(200,CCW,.0003)
        
    elif n == 1 :
        motor_threading1 = threading.Thread(target=y.move,args=(1350,CCW,.0003)) #1000
        motor_threading2 = threading.Thread(target=z.move,args=(2700,CW,.0003)) #1675
        motor_threading1.start()
        motor_threading2.start()
        motor_threading1.join()
        motor_threading2.join()
        x.move(300,CCW,.0003)
    place()
    print("finishing return box to locker")

def inter():
    global state
    global num_box
    x.interrupt = True
    y.interrupt = True
    z.interrupt = True
    
    print("state condition : ", state)
    print("wating for all axis stop")
    while  x.interrupt or y.interrupt or z.interrupt:
        sleep(0.1)
    print("handle interrupt")
    print("state123 :" , state)
    if state == "Prepare_pos" or state == "locker" or state == "Start":
        return_home_inter()
        prepare_pos()
        print("state :",state)
        print("HOME1")
        return "HOME1"
    elif state == "locker with box" or state == "lifting":
        print("num box : " , num_box)
        print("state :",state)
        return_home_inter2()
        sleep(0.05)
        prepare_pos2()
        return_box_inter(num_box)
        return_home_inter()
        prepare_pos()
        print("HOME2")
        return "HOME2"
    elif state == "return_to_locker" :
        return_home_inter2()
        print("num box : " , num_box)
        print("state :",state)
        t1 = threading.Thread(target=z.move,args=(5000,CW,.0003)) 
        t2 = threading.Thread(target=y.move,args=(300,CW,.0003))
        t1.start()
        t2.start()
        t1.join()
        t2.join()
        x.move(3200,CCW,.0003)
        z.move(450,CCW,.0003)
        #distance from home to return pos
        print("HOME3")
        return "Return Drawer"
    else :
        print("else : ",state)
        return state
    return 