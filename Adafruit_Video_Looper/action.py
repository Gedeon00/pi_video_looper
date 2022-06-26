import RPi.GPIO as GPIO
import time

motor = 15
cycles = 0

GPIO.setmode(GPIO.BOARD)
GPIO.setup(motor, GPIO.OUT)

def curtain_motor(curtain_open: bool):

    if curtain_open == False:
        GPIO.output(motor, GPIO.HIGH)
        time.sleep(3)
        GPIO.output(motor, GPIO.LOW)

        curtain_open == True
        cycles = 0

    else:
        cycles += 1

    if cycles > 3:
        curtain_open = False

    return curtain_open
