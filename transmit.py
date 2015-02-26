import os
import csv
import time
import Adafruit_CharLCD as LCD
from menu import Menu

def Transmit(lcd, doctor):
	print "Transmit Function:"
	lcd.clear()
	lcd.message("Transmit\nFunction")
	os.system('sudo hciconfig hci0 leadv')

	os.chdir('/home/pi/RPiCode/')

	path = os.listdir('/home/pi/RPiCode/')
	if(path.count(doctor) == 0):
		lcd.clear()
		lcd.set_color(1,0,0)
		lcd.message("No data to\n transmit")
		time.sleep(5.0)
		return

	lcd.clear()
	lcd.message("Scanning for\n Devices")
	os.system('hcitool scan > bluezScan.txt')
	with open("bluezScan.txt") as f:
		content = f.readlines()
#	print 'Content: ' + str(content)
	
	for item in content:
		if "Scanning" in item:
			content.remove(item)

	namelist = []
	addresslist = []
	for item in content:
		idstring = item.split("\t")
		addresslist.append(idstring[1])
		namelist.append(idstring[2])

	
	print "namelist: " + str(namelist)
	print "addresslist: " + str(addresslist)
	selection = Menu(lcd, namelist)

	os.chdir('/home/pi/RPiCode/' + doctor)

	datalist = []
	with open('data.csv', 'rb') as f:
		reader = csv.reader(f, dialect='excel')
		for row in reader:
			datastring = ','.join(row)
			datalist.append(datastring)

#	for item in datalist:
#		print item
	
	print '\n'.join(datalist)
