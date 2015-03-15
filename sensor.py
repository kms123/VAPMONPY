import time
import os
import RPi.GPIO as GPIO
import Adafruit_CharLCD as LCD
from presureaverage import PressureAverage

def readADC(adcnum, clockpin, mosipin, misopin, cspin):
	GPIO.output(cspin, True)
	GPIO.output(clockpin, False)
	GPIO.output(cspin, False)
	
	commandout = adcnum
	commandout |= 0x18
	commandout <<= 3
	
	for i in range(5):
		if(commandout & 0x80):
			GPIO.output(mosipin, True)
		else:
			GPIO.output(mosipin, False)
			
		commandout <<= 1
		GPIO.output(clockpin, True)
		GPIO.output(clockpin, False)
		
	adcout = 0
	
	for i in range(12):
		GPIO.output(clockpin, True)
		GPIO.output(clockpin, False)
		adcout <<= 1
		if(GPIO.input(misopin)):
			adcout |= 0x1
		
	GPIO.output(cspin, True)
	
	adcout >>= 1
	return adcout
	
def sensor(lcd):
	GPIO.setmode(GPIO.BCM)
	
	SPICLK = 11
	SPIMISO = 9
	SPIMOSI = 10
	SPICS = 8
	
	# set up the SPI interface pins
	GPIO.setup(SPIMOSI, GPIO.OUT)
	GPIO.setup(SPIMISO, GPIO.IN)
	GPIO.setup(SPICLK, GPIO.OUT)
	GPIO.setup(SPICS, GPIO.OUT)
	
	#print "Sensor()"
	sensorADC = 0
	lastRead = 0
	
	sensing = True
	data = []
	
	buttons = ((LCD.SELECT, True),
				(LCD.LEFT, False),
				(LCD.UP, True),
				(LCD.DOWN, True),
				(LCD.RIGHT, True))
	
	
	while sensing:
		
		sensor = readADC(sensorADC, SPICLK, SPIMOSI, SPIMISO, SPICS)

		lcd.clear()
		lcd.message(str(sensor))

		data.append(sensor)
		
		for button in buttons:
			if lcd.is_pressed(button[0]):
				sensing = button[1]
				
	
	average = PressureAverage(data)
	
	GPIO.cleanup()
	
	return average
