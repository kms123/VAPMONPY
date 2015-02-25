import os
import csv
import time
import Adafruit_CharLCD as LCD

def Transmit(lcd, doctor):
	print "Transmit Function:"
	
	path = os.listdir('/home/pi/RPiCode/')
	if(path.count(doctor) == 0):
		lcd.clear()
		lcd.message("No data to\n transmit")
		time.sleep(5.0)
		return
	os.system('hcitool scan > bluezScan.txt')
	with open("bluezScan.txt") as f:
		content = f.readlines()
	print 'Content: ' + str(content)
	
	for item in content:
		if "Scanning" in item:
			content.remove(item)
	
	print content

	os.chdir('/home/pi/RPiCode/' + doctor)

	datalist = []
	with open('data.csv', 'rb') as f:
		reader = csv.reader(f, dialect='excel')
		for row in reader:
			datastring = ','.join(row)
			datalist.append(datastring)
	for item in datalist:
		print item
	
	print ','.join(datalist)
