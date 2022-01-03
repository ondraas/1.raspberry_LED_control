import RPi.GPIO as GPIO           # import RPi.GPIO python module
import os                         # import OS module

def setupGPIO():
    GPIO.setmode(GPIO.BOARD)      # Use physical pin numbering
    GPIO.setwarnings(False)       # Turn off warnings

    GPIO.setup(18, GPIO.OUT)      # Set output pin 18


def ON_OFF():                     # Create function for controling ON/OFF LED
    
    while True:
        user_input = input("ON: ")
        if user_input is "1":
            GPIO.output(18, GPIO.HIGH)  # Set output pin 18
            print("ON")
        elif user_input is "0":
            GPIO.output(18, GPIO.LOW)   # Set output pin 18
            print("OFF")

        print()        
               


setupGPIO()

ON_OFF()

