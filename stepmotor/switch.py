import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)



while True:
    x_axis = GPIO.input(4)

    y_axis = GPIO.input(17)

    z_axis = GPIO.input(18)
    print([x_axis,y_axis,z_axis])
