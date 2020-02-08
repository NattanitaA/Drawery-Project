#Copyright https://github.com/tatobari (Some parts)

#! /usr/bin/python2

import time
import sys
interrupt = 1
EMULATE_HX711=False

# referenceUnit = 1
if not EMULATE_HX711:
    import RPi.GPIO as GPIO
    from hx711 import HX711
else:
    from emulated_hx711 import HX711

def cleanAndExit():
    print("Cleaning...")

    if not EMULATE_HX711:
        GPIO.cleanup()
        
    print("Bye!")
    sys.exit()

hx = HX711(9, 11)

# The first parameter is the order in which the bytes are used to build the "long" value.
# The second paramter is the order of the bits inside each byte.
hx.set_reading_format("MSB", "MSB")


hx.set_reference_unit(60)
#hx.set_reference_unit(referenceUnit)

hx.reset()

hx.tare()


#Nattanita's Code
# *********************************************************

def checkWeight():
    global interrupt
    
    while True:

        try:

            print(interrupt)
            while interrupt:
                
                weight = []
                count = 0
                    
                for _ in range(15):
                    val = max(0, int(hx.get_weight(9)))
                    # if interrupt == 0:
                    #     cleanAndExit()
                    weight.append(val)
                    print(weight)
                    print(interrupt)
#                    time.sleep(1)
                #print(weight)
                check = weight[0]
                for i in weight:
                    # if interrupt == 0:
                        # cleanAndExit()
                    if i > check + 10 or i < check-10: break
                    count += 1
                    #time.sleep(0.5)
                if count == 15:
                    return True
            cleanAndExit()
            hx.power_down()
            hx.power_up()
            time.sleep(0.7)

        except (KeyboardInterrupt, SystemExit):
            cleanAndExit()
            
def weightInter():
    global interrupt
    print('stop na')
    #cleanAndExit()
    interrupt = 0

# ***********************************************************