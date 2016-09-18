
## Define function named Blink()
def Beeep(lenght,pin):
	import RPi.GPIO as GPIO ## Import GPIO Library
	import time ## Import 'time' library.  Allows us to use 'sleep'
	GPIO.setmode(GPIO.BOARD) ## Use BOARD pin numbering
	GPIO.setup(pin, GPIO.OUT) ## Setup GPIO pin 7 to OUT
	GPIO.output(pin, True) ## Turn on GPIO pin 7
	time.sleep(lenght) ## Wait
	GPIO.output(pin, False) ## Switch off GPIO pin 7
#	GPIO.cleanup()

pin = 7 
lenght = 0.4
Beeep(float(lenght),int(pin))
        