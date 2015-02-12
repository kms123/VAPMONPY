import os
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

os.system('cd "/home/pi/libnfc/libnfc-libnfc-1.7.0/examples"')
print "Changed dir"
os.system('nfc-poll > /home/pi/RPiCode/nfc.txt') #Currently overwriting file every time. Use >> to append to file.

with open("nfc.txt") as f:
	content = f.readlines()

for item in content:
	if "UID" in item:
		code = item[item.index(':')+1:]

