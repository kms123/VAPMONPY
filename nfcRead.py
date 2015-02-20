import os
import RPi.GPIO as GPIO
import datetime
import csv

from keypad import KeypadRead as KeypadRead

#Dummy data
flow = 5
press = 1.3

print "Input doctor code"
digitOne = KeypadRead()
print digitOne
digitTwo = KeypadRead()
print digitTwo
digitThree = KeypadRead()
print digitThree
digitFour = KeypadRead()
print digitFour

doctor = digitOne + digitTwo + digitThree + digitFour
print doctor

os.system('cd "/home/pi/libnfc/libnfc-libnfc-1.7.0/examples"')
print "Scan NFC module"
os.system('nfc-poll > /home/pi/RPiCode/nfc.txt') #Currently overwriting file every time. This file just used to save UID and then it is extracted and saved in the proper data file.

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
