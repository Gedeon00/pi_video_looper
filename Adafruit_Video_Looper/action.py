import RPi.GPIO as GPIO
import time

motor = 8
close_time = 3

GPIO.setmode(GPIO.BOARD)
GPIO.setup(motor, GPIO.OUT)

def curtain_motor(curtain_open: bool):

    if curtain_open == False:
        # open curtain
        GPIO.output(motor, GPIO.HIGH)
        time.sleep(close_time)
        GPIO.output(motor, GPIO.LOW)
        curtain_open = True
        return curtain_open

    else:
        # close curtain
        GPIO.output(motor, GPIO.HIGH)
        time.sleep(close_time)
        GPIO.output(motor, GPIO.LOW)
        curtain_open = False
        return curtain_open
