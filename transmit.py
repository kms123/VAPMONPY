import os
import csv
import time
import Adafruit_CharLCD as LCD
from menu import Menu
from bluetooth import *

def Transmit(lcd, doctor):
#	print "Transmit Function:"
	lcd.clear()
	lcd.message("Transmit\nFunction")
	os.system('sudo hciconfig hci0 leadv')

	os.chdir('/home/pi/RPiCode/')

	path = os.listdir('/home/pi/RPiCode/')
	if(path.count(doctor) == 0):
		lcd.clear()
		lcd.set_color(1,0,0)
		lcd.message("No data to\ntransmit")
		time.sleep(5.0)
		return

	lcd.clear()
	lcd.message("Scanning for\nDevices")
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

	server_sock=BluetoothSocket(RFCOMM)
	server_sock.bind(("",PORT_ANY))
	server_sock.listen(1)	
	port = server_sock.getsockname()[1]
	print "Listening on port %d" %port

	uuid = "2345ABCD"

	advertise_service(server_sock, "RPi-0", uuid)
	
#	print "namelist: " + str(namelist)
#	print "addresslist: " + str(addresslist)
#	selection = Menu(lcd, namelist)

	os.chdir('/home/pi/RPiCode/' + doctor)

	datalist = []
	with open('data.csv', 'rb') as f:
		reader = csv.reader(f, dialect='excel')
		for row in reader:
			datastring = ','.join(row)
			datalist.append(datastring)


#	for item in datalist:
#		print item
	
	dataout =  '\n'.join(datalist)

	transmitting = True
	idx = 0
	lastidx = len(dataout) - 1
	print "Entering transmission loop."
	while transmitting:
		client_sock, client_info = server_sock.accept()
		print "Accepted connection from " + client_info

		try:
			iosdoctor = client_sock.recv(1024)
			if iosdoctor != doctor:
				lcd.set_color(1,0,0)
				lcd.clear()
				lcd.message("Doctor codes\ndon't match")
				time.sleep(1)
			
			client_sock.send(dataout[idx:idx+17])
			if (idx + 17  >= lastidx):
				transmitting = False
			
			idx = idx + 18
		except IOError:
			pass

		except KeyboardInterrupt:
			client_sock.close()
			server_sock.close()
			print "*** Transmission Interrupted ***"
			break
			
	lcd.clear()
	lcd.message("Transmission Complete")
	client_sock.close()
	server_sock.close()
