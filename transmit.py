import os
import csv

def Transmit(doctor):
	print "Transmit Function:"
	
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
