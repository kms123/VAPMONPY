import Adafruit_CharLCD as LCD
import time
import os

from keypad import KeypadRead as KeypadRead
from menu import Menu as Menu
from nfcRead import NFCRead
from transmit import Transmit

#initialization of the LCD
lcd = LCD.Adafruit_CharLCDPlate()
lcd.set_color(1,1,1)
lcd.message("     VAPMON")
time.sleep(1.5)

lcd.set_color(1,0,1)
lcd.clear()
lcd.message("Input Doctor #")

digit = ""
doctor = ""
while True:
	#print "Input doctor code"
	digit = KeypadRead()
	if digit == 'B':
		doctor = doctor[:-1]
	elif digit == '*':
		break
	else:
		doctor += digit
	lcd.clear()
	lcd.message("Input Doctor #\n" + doctor)
	#print digitOne
	
print doctor

menuItems = ['Record', 'Transmit', 'Shutdown']
while True:
#	lcd.set_color(0,1,0)
	selection = Menu(lcd, menuItems)
#	print selection

	if selection == 1:
		NFCRead(lcd, doctor)
	elif selection == 2:
		Transmit(lcd, doctor)
	else:
		lcd.set_color(0,0,0)
		lcd.clear()
		os.system('sudo shutdown -h now')
		
