#!/usr/bin/python
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|-|S|p|y|.|c|o|.|u|k|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#
# pir_2.py
# Measure the holding time of a PIR module
# Author : Matt Hawkins
# Date   : 20/02/2013

import time
import datetime
import RPi.GPIO as GPIO
import os
import time
import subprocess

GPIO.setmode(GPIO.BCM)
GPIO_PIR = 7
GPIO_BLINK = 22
GPIO.setup(GPIO_BLINK, GPIO.OUT) 
GPIO.setup(GPIO_PIR,GPIO.IN)    
Current_State  = 0
Previous_State = 0
photo_counter = 0    # Photo counter
        
def Blinkfast(speed,PIN,outputtt):
	GPIO.output(PIN, True) 
	#time.sleep(speed) ## Wait
	#print(outputtt)
	GPIO.output(PIN, False) 

def Savetofile(filenamee):
	file = open("FB_Log2.txt", "a")
	geppo = 'Motion@ '+ datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S') + '\n'
	file.write(geppo)
	file.close()

def makeaphoto(photo_counter):
	filename = 'photonew_' + str(photo_counter) + '.jpg'
	cmd = 'raspistill -o ' + filename + ' -t 1 -ev 0 -w 640 -h 480'
	print (filename)
	pid = subprocess.call(cmd, shell=True)

print "PIR Module Holding Time Test (CTRL-C to exit)"

try:

  print "Waiting for PIR to settle ..."

  # Loop until PIR output is 0
  while GPIO.input(GPIO_PIR)==1:
    Current_State  = 0

  print "Ready"

  # Loop until users quits with CTRL-C
  while True :

    # Read PIR state
    Current_State = GPIO.input(GPIO_PIR)

    if Current_State==1 and Previous_State==0: # PIR is triggered
		GPIO.output(GPIO_BLINK, True) 
		photo_counter = photo_counter + 1
		makeaphoto(photo_counter)
		start_time=time.time()
		print 'Motion detected'  + str(int(round(time.time() * 1000))) 
		Previous_State=1   # Record previous state
    elif Current_State==0 and Previous_State==1: # PIR has returned to ready state
		GPIO.output(GPIO_BLINK, False) 
		stop_time=time.time()
		print "Ready",
		elapsed_time=(stop_time-start_time)
		print " (Elapsed time : " + str(elapsed_time) + " secs)"
		Previous_State=0

except KeyboardInterrupt:
  print "  Quit"
  # Reset GPIO settings
  GPIO.cleanup()