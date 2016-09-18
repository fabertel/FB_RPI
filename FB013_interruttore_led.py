import RPi.GPIO as GPIO ## Import GPIO Library
import time ## Import 'time' library.  Allows us to use 'sleep'

GPIO.setmode(GPIO.BCM) ## Use BOARD pin numbering
GPIO.setup(4, GPIO.OUT) ## Setup GPIO pin 7 to OUT
GPIO.setup(17, GPIO.IN) ## Setup GPIO pin 7 to OUT

## Define function named Blink()
def Blink(numTimes, speed):
    for i in range(0,numTimes): ## Run loop numTimes
		print "Iteration " + str(i+1) ##Print current loop
		GPIO.output(4, True) ## Turn on GPIO pin 7
		time.sleep(speed) ## Wait
		GPIO.output(4, False) ## Switch off GPIO pin 7
		time.sleep(speed) ## Wait
    print "Done" ## When loop is complete, print "Done"
    GPIO.cleanup()

Blink(int(2),float(.4))
        