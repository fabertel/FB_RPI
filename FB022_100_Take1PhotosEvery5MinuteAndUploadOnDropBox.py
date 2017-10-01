#!/usr/bin/python
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|-|S|p|y|.|c|o|.|u|k|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#
# Project URL :
# http://www.raspberrypi-spy.co.uk/?p=1862
#2016-09-18 .. aggiunto data in filename e upload in dropbox 
#v1 loop
#v1.3 - 2017/10/01
#	added library con visualizzazione per sleep 
#	removed photo from PI memory 
#	added stand and rotated photo
#takes 100 foto una ogni 5minuti : 5 ore 

import os
import time
import subprocess
import datetime
import FB_LIB_01_Sleep_counter_pregress as sl2


vversion = 'v1.3'
photo_counter = 0    # Photo counter
print('+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+')
print "Starting photo" + vversion

while (photo_counter < 100):

	timestamp = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d_%H%M%S') 
	photo_counter = photo_counter + 1
	filename = 'photo_' + str(timestamp) + '.jpg'
	makeaphoto = 'raspistill -o ' + filename + ' -w 640 -h 480 -rot 180 -t 1';
	pid = subprocess.call(makeaphoto, shell=True) 
	#subprocess.call(makeaphoto, shell=True) 
	print('+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+')
	print "1 Foto effettuata" + str(photo_counter) + '  ' + filename
	print '2 Uploading' + str(photo_counter) + '  ' + filename
	Uploader = "/home/pi/Dropbox-Uploader/dropbox_uploader.sh "
	SourcePath = "/home/pi/FB/"
	UploadPath = "/RPI_test2/"
	ScriptUpload = Uploader+"upload "+SourcePath+filename+" "+UploadPath
	ScriptUpload = Uploader+"upload "+SourcePath+"latest.jpg "+UploadPath
	print (ScriptUpload)
	subprocess.call(ScriptUpload, shell=True)
	os.remove(filename) 
	print '3 Deleted : ' + str(photo_counter) + '  ' + filename
	sl2.sleep2(10)
	print('+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+')
	

#os.system("/home/pi/Dropbox-Uploader/dropbox_uploader.sh upload FB_Log.txt /RPI_test2/");

print('+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+')
print('END')