import RPi.GPIO as GPIO           # import RPi.GPIO python module
import os
from time import sleep            # Sleep function import

def setupGPIO():
    GPIO.setmode(GPIO.BOARD)      # Use physical pin numbering
    GPIO.setwarnings(False)       # Turn off warnings

    GPIO.setup(18, GPIO.OUT)      # Set output pin 18

def BLINK():                      # Create function for blinking LED every 5 seconds
    while True:
        user_input2 = input("SET: ")
        if user_input2 is "B":
            GPIO.output(18, GPIO.HIGH) # LED ON
            sleep(5)                   # 5 sec sleep
            GPIO.output(18, GPIO.LOW)   # LED OFF
            sleep(5)                   # 5 sec sleep

        print()  

setupGPIO

BLINK