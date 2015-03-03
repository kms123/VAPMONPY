import os
import datetime
import time
import csv
import Adafruit_CharLCD as LCD
import random

def NFCRead(lcd, doctor):

#Dummy data
	flow = random.randrange(0,10)
	print 'Flow: ' +str(flow)
	press = random.randrange(1,5)
#	doctor = "1234"

	os.system('cd "/home/pi/libnfc/libnfc-libnfc-1.7.0/examples"')

#	print "Scan NFC module"
	lcd.set_color(1,1,0)
	lcd.clear()
	lcd.message("Scan NFC Module")

	os.system('nfc-poll > /home/pi/RPiCode/nfc.txt') #Currently overwriting file every time. This file just used to save UID and then it is extracted and saved in the proper data file.
	with open("/home/pi/RPiCode/nfc.txt") as f:
		content = f.readlines()

	for item in content:
		if "UID" in item:
			code = item[item.index(':')+2:]
	ID = code.strip()
	UID = ID.replace(" ","")
	lcd.clear()
	lcd.message("Scan NFC Module\n" + UID)
	time.sleep(2)
#	print UID
	
	path = os.listdir('/home/pi/RPiCode/')
	if(path.count(doctor) == 0):
		os.mkdir(doctor)

	os.chdir('/home/pi/RPiCode/' + doctor)

	if not os.path.exists('data.csv'):
		open('data.csv', 'w').close()

	numlines = sum(1 for line in open('data.csv'))
#	print numlines

	with open('data.csv', 'a') as f:
		textwriter = csv.writer(f, dialect='excel')
		if(numlines == 0):
			textwriter.writerow(['doctorCode']+['patientNumber']+['date']+['flowRateValue']+['pressureValue'])

		textwriter.writerow([doctor]+[UID]+[datetime.date.today()]+[flow]+[press])
