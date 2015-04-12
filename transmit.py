import os
import csv
import time
import Adafruit_CharLCD as LCD
from menu import Menu
from bluetooth import *

def Transmit(lcd, doctor):
	print "Transmit Function:"
	lcd.clear()
	lcd.message("Transmit\nFunction")

	os.chdir('/home/pi/RPiCode/')

	path = os.listdir('/home/pi/RPiCode/')
	if(path.count(doctor) == 0):
		lcd.clear()
		lcd.set_color(1,0,0)
		lcd.message("No data to\ntransmit")
		time.sleep(5.0)
		return

	os.chdir('/home/pi/RPiCode/' + doctor)

	datalist = []
	with open('data.csv', 'rb') as f:
		reader = csv.reader(f, dialect='excel')
		for row in reader:
			datastring = ','.join(row)
			datalist.append(datastring.strip())

	eof = "DONELIKEDINNER"
	
	for item in datalist:
		with open('/dev/ttyUSB0', 'w') as f:
			f.write(item + ',\n')
			print item
		time.sleep(0.5)

	time.sleep(5)
	#print "Done Sleeping..."

	with open('/dev/ttyUSB0', 'a') as f:
		f.write(eof)


	lcd.clear()
	lcd.message("Transmission Complete")
