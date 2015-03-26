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
#	os.system('sudo hciconfig hci0 leadv')

	os.chdir('/home/pi/RPiCode/')

	path = os.listdir('/home/pi/RPiCode/')
	if(path.count(doctor) == 0):
		lcd.clear()
		lcd.set_color(1,0,0)
		lcd.message("No data to\ntransmit")
		time.sleep(5.0)
		return
#	if(path.count('datain.txt') > 0):
#		os.system('rm datain.txt')

#	os.system('cat /dev/ttyUSB0 > /home/pi/RPiCode/datain.txt &')

#	while(path.count('datain.txt') == 0):
#		pass
	
#	with open("datain.txt") as f:
#		content = f.readlines()
#	print 'Content: ' + str(content)
			
#	lcd.clear()
#	lcd.message("Scanning for\nDevices")
#	os.system('hcitool scan > bluezScan.txt')
#	with open("bluezScan.txt") as f:
#		content = f.readlines()
	
#	for item in content:
#		if "Scanning" in item:
#			content.remove(item)

#	namelist = []
#	addresslist = []
#	for item in content:
#		idstring = item.split("\t")
#		addresslist.append(idstring[1])
#		namelist.append(idstring[2])

#	server_sock=BluetoothSocket(RFCOMM)
#	server_sock.bind(("",PORT_ANY))
#	server_sock.listen(1)	
#	port = server_sock.getsockname()[1]
#	print "Listening on port %d" %port

#	seruuid = "50B470F9-BB75-4CEF-9EEE-D254D7B35AF0"
#	charuuid = "091A682D-CCCD-4565-AB5C-737BDD806CF2"
#	find_service(None, seruuid, None)
#	advertise_service(server_sock, "RPi-0", seruuid, [SERIAL_PORT_CLASS, AUDIO_SOURCE_CLASS])

#	print "namelist: " + str(namelist)
#	print "addresslist: " + str(addresslist)
#	selection = Menu(lcd, namelist)

	os.chdir('/home/pi/RPiCode/' + doctor)

	datalist = []
	with open('data.csv', 'rb') as f:
		reader = csv.reader(f, dialect='excel')
		for row in reader:
			datastring = ','.join(row)
			datalist.append(datastring.strip())


#	for item in datalist:
#		print item
	
	dataout =  '\n'.join(datalist)
#	print dataout
	eof = "DONELIKEDINNER"

#	with open('/dev/ttyUSB0', 'a') as f:
#		for item in datalist:
#			f.write(item)
#			print "Item " + item
#			time.sleep(4)
	
	for item in datalist:
		with open('/dev/ttyUSB0', 'w') as f:
			f.write(item + ',\n')
			print item
		time.sleep(0.5)

	time.sleep(5)
	print "Done Sleeping..."

	with open('/dev/ttyUSB0', 'a') as f:
		f.write(eof)
	
#	transmitting = True
#	idx = 0
#	lastidx = len(dataout) - 1
#	lcd.clear()
#	lcd.message("Transmitting...")
#	print "Entering transmission loop."
#	while transmitting:
#		client_sock, client_info = server_sock.accept()
#		print "Accepted connection from " + client_info

#		try:
#			iosdoctor = client_sock.recv(1024)
#			if iosdoctor != doctor:
#				lcd.set_color(1,0,0)
#				lcd.clear()
#				lcd.message("Doctor codes\ndon't match")
#				time.sleep(1)
			
#			client_sock.send(dataout[idx:idx+17])
#			if (idx + 17  >= lastidx):
#				transmitting = False
			
#			idx = idx + 18
#		except IOError:
#			pass
#
#		except KeyboardInterrupt:
#			client_sock.close()
#			server_sock.close()
#			print "*** Transmission Interrupted ***"
#			break

					
	lcd.clear()
	lcd.message("Transmission Complete")
#	client_sock.close()
#	server_sock.close()
