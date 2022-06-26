import RPi.GPIO as GPIO
import time

motor_open = 8
motor_close = 10

close_time = 3

GPIO.setmode(GPIO.BOARD)
GPIO.setup(motor, GPIO.OUT)

def open_curtain():
    # open curtain
    GPIO.output(motor_open, GPIO.HIGH)
    print("opening curtain")
    time.sleep(close_time)
    GPIO.output(motor_open, GPIO.LOW)

def close_curtain():
    # close curtain
    GPIO.output(motor_close, GPIO.HIGH)
    print("closing curtain")
    time.sleep(close_time)
    GPIO.output(motor_close, GPIO.LOW)
