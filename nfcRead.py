import os
import datetime
import time
import csv
import Adafruit_CharLCD as LCD
import random
from sensor import sensor
from keypad import KeypadRead
from menu import Menu

def NFCRead(lcd, doctor):

#Dummy data
	flow = "" #random.randrange(0,10)
	#print 'Flow: ' + str(flow)
	press = 0
#	doctor = "1234"

	os.system('cd "/home/pi/libnfc/libnfc-libnfc-1.7.0/examples"')

#	print "Scan NFC module"
	lcd.set_color(1,1,0)
	lcd.clear()
	lcd.message("Scan NFC Module")
	#print "Scan NFC Module"

	os.system('nfc-poll > /home/pi/RPiCode/nfc.txt') #Overwrites file every time. This file just used to save UID and then it is extracted and saved in the proper data file.
	with open("/home/pi/RPiCode/nfc.txt") as f:
		content = f.readlines()

	for item in content:
		if "UID" in item:
			code = item[item.index(':')+2:]
	ID = code.strip()
	UID = ID.replace(" ","")
	lcd.clear()
	lcd.message("Scan NFC Module\n" + UID)
	#print UID
	time.sleep(2)
	
	lcd.clear()
	lcd.message("Enter flow rate:")
	print "Enter flow rate: "
	while True:
		digit = KeypadRead()
		if digit == 'B':
			flow = flow[:-1]
		elif digit == '*':
			break
		else:
			flow += digit
		lcd.clear()
		lcd.message("Enter flow rate:\n" + flow)
		print flow

	flowunits = ["ml/s", "ml/min"]
	print "Pick units"
	units = Menu(lcd, flowunits)
	lcd.set_color(1,1,0)

	if units == 2:
		flow = int(float(flow)/60) 
		
	print "Flow: " + str(flow)
	
	path = os.listdir('/home/pi/RPiCode/')
	if(path.count(doctor) == 0):
		os.mkdir(doctor)

	os.chdir('/home/pi/RPiCode/' + doctor)

	if not os.path.exists('data.csv'):
		open('data.csv', 'w').close()

	numlines = sum(1 for line in open('data.csv'))
#	print numlines
	
	press = sensor(lcd)
	
	with open('data.csv', 'a') as f:
		textwriter = csv.writer(f, dialect='excel')
		if(numlines == 0):
			textwriter.writerow(['doctorCode']+['patientNumber']+['date']+['flowRateValue']+['pressureValue'])

		textwriter.writerow([doctor]+[UID]+[datetime.date.today()]+[flow]+[press])
