import RPi.GPIO as GPIO
import time #for timing delays

def InitIO ():
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(9, GPIO.IN, pull_up_down=GPIO.PUD_UP) 
	
def CheckSwitch ():
	val1 = not GPIO.input(10)
	val2= not GPIO.input(23) 
	val3= not GPIO.input(4)
	val4= not GPIO.input(9) 
	print val1,val2,val3,val4
	
InitIO()
while (True):
	CheckSwitch()
	time.sleep(0.5)
