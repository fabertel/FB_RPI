import RPi.GPIO as GPIO
import time
 
#initialisiere GPIO
PIN_A = 7
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN_A, GPIO.OUT)
print "Programm wird mit STRG+C beendet"
done = False
state = True
try:
	while not done:
	GPIO.output(PIN_A, state)

	if state:
	state = False
	else:
	state = True
	time.sleep(0.2)
	GPIO.cleanup()
except KeyboardInterrupt:
 GPIO.cleanup()