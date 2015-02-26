import Adafruit_CharLCD as LCD
import time

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

print "Input doctor code"
digitOne = KeypadRead()
lcd.clear()
lcd.message("Input Doctor #\n" + digitOne)
print digitOne
digitTwo = KeypadRead()
lcd.clear()
lcd.message("Input Doctor #\n" + digitOne + digitTwo)
print digitTwo
digitThree = KeypadRead()
lcd.clear()
lcd.message("Input Doctor #\n" + digitOne + digitTwo + digitThree)
print digitThree
digitFour = KeypadRead()
lcd.clear()
lcd.message("Input Doctor #\n" + digitOne + digitTwo + digitThree + digitFour)
print digitFour

doctor = digitOne + digitTwo + digitThree + digitFour
print doctor

menuItems = ['Record', 'Transmit']
while True:
	lcd.set_color(0,1,0)
	selection = Menu(lcd, menuItems)
	print selection

	if selection == 1:
		NFCRead(lcd, doctor)
	else:
		Transmit(lcd, doctor)
		
