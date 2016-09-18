import RPi.GPIO as GPIO ## Import GPIO Library
import time ## Import 'time' library.  Allows us to use 'sleep'
GPIO.setmode(GPIO.BOARD) ## Use BOARD pin numbering
GPIO.setup(7, GPIO.OUT) ## Setup GPIO pin 7 to OUT
GPIO.output(7, True) ## Turn on GPIO pin 7
time.sleep(.4) ## Wait
GPIO.output(7, False) ## Switch off GPIO pin 7
GPIO.cleanup()

