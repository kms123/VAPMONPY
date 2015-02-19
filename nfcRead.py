import os
import RPi.GPIO as GPIO
import datetime
import csv

GPIO.setmode(GPIO.BOARD)

#Dummy data
doctor = 1234
flow = 5
press = 1.3

os.system('cd "/home/pi/libnfc/libnfc-libnfc-1.7.0/examples"')
print "Scan NFC module"
os.system('nfc-poll > /home/pi/RPiCode/nfc.txt') #Currently overwriting file every time. Use >> to append to file.

with open("nfc.txt") as f:
	content = f.readlines()

for item in content:
	if "UID" in item:
		code = item[item.index(':')+2:]
ID = code.strip()
UID = ID.replace(" ","")
print UID

path = os.listdir('/home/pi/RPiCode/')
if(path.count(UID) == 0):
	os.mkdir(UID)

os.chdir('/home/pi/RPiCode/' + UID)

if not os.path.exists('test.csv'):
	open('test.csv', 'w').close()

numlines = sum(1 for line in open('test.csv'))
print numlines

with open('test.csv', 'a') as f:
	textwriter = csv.writer(f, dialect='excel')
	if(numlines == 0):
		textwriter.writerow(['doctorCode']+['patientNumber']+['date']+['flowRateValue']+['pressureValue'])

	textwriter.writerow([doctor]+[UID]+[datetime.date.today()]+[flow]+[press])
