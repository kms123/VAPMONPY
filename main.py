import Adafruit_CharLCD as LCD
import time
import os

from keypad import KeypadRead as KeypadRead
from menu import Menu as Menu
from nfcRead import NFCRead
from transmit import Transmit
from demo import Demo

#initialization of the LCD
lcd = LCD.Adafruit_CharLCDPlate()
lcd.set_color(1,0,0)
lcd.message("     VAPMON")
time.sleep(1.5)

lcd.set_color(1,0,1)
lcd.clear()
lcd.message("Input Doctor #")

digit = ""
doctor = ""
print "Input doctor code"

while True:
	digit = KeypadRead()
	if digit == 'B':
		doctor = doctor[:-1]
	elif digit == '*':
		break
	else:
		doctor += digit
	lcd.clear()
	lcd.message("Input Doctor #\n" + doctor)
	print digit
	
print doctor

menuItems = ['Record', 'Transmit', 'Shutdown']
while True:
#	lcd.set_color(0,1,0)
	print "Main Menu"
	selection = Menu(lcd, menuItems)
	print selection

	if selection == 1:
		NFCRead(lcd, doctor)
	elif selection == 2:
		Transmit(lcd, doctor)
	elif selection == 3:
		lcd.set_color(0,0,0)
		lcd.clear()
		os.system('sudo shutdown -h now')
	else:
		pass
		
