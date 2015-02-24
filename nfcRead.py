import os
import RPi.GPIO as GPIO
import datetime
import csv

from keypad import KeypadRead as KeypadRead

#Dummy data
flow = 5
press = 1.3
doctor = 1234

# print "Input doctor code"
# digitOne = KeypadRead()
# print digitOne
# digitTwo = KeypadRead()
# print digitTwo
# digitThree = KeypadRead()
# print digitThree
# digitFour = KeypadRead()
# print digitFour

# doctor = digitOne + digitTwo + digitThree + digitFour
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
if(path.count(doctor) == 0):
	os.mkdir(doctor)

os.chdir('/home/pi/RPiCode/' + doctor)

if not os.path.exists('data.csv'):
	open('data.csv', 'w').close()

numlines = sum(1 for line in open('data.csv'))
print numlines

with open('data.csv', 'a') as f:
	textwriter = csv.writer(f, dialect='excel')
	if(numlines == 0):
		textwriter.writerow(['doctorCode']+['patientNumber']+['date']+['flowRateValue']+['pressureValue'])

	textwriter.writerow([doctor]+[UID]+[datetime.date.today()]+[flow]+[press])
