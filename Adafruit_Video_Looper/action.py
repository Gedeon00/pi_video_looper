import RPi.GPIO as GPIO
import time

motor = 8
close_time = 3

GPIO.setmode(GPIO.BOARD)
GPIO.setup(motor, GPIO.OUT)

def open_curtain():
    # open curtain
    GPIO.output(motor, GPIO.HIGH)
    print("opening")
    time.sleep(close_time)
    GPIO.output(motor, GPIO.LOW)

def close_curtain():
    # close curtain
    GPIO.output(motor, GPIO.HIGH)
    print("closing")
    time.sleep(close_time)
    GPIO.output(motor, GPIO.LOW)
