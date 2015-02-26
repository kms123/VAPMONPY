import Adafruit_CharLCD as LCD
import time

def Menu(lcd, items):
	len0 = 13
	len1 = 13
	lcd.create_char(1, [8, 12, 10, 9, 10, 12, 8, 0])
	while len(items) < 2:
		items.append("")
	if items[0] == None:
		items[0] = ""
	if len(items[0]) < 13:
		len0 = len(items[0])
	if len(items[1]) < 13:
		len1 = len(items[1])		

	lcd.set_color(0,1,0)
	lcd.clear()
	lcd.message("\x01 " + items[0][:len0] + "\n  " + items[1][:len1])
	
	selectionMade = False
	selection = 0
	
	buttons = (	(LCD.SELECT, True),
			(LCD.LEFT, False),
			(LCD.UP, False),
			(LCD.DOWN, False),
			(LCD.RIGHT, False))
			
	while not selectionMade:
		for button in buttons:
			if lcd.is_pressed(button[0]):
				selectionMade = button[1]
				if button[0] == LCD.DOWN:
					if (selection < len(items)-1):
						selection = selection + 1
					print "Selection: " + str(selection)
					lcd.clear()
					lcd.message("  " + items[selection-1][:13] + "\n\x01 " + items[selection][:13])
				if button[0] == LCD.UP:
					if (selection > 0):
						selection = selection - 1
					print "Selection: " + str(selection)
					lcd.clear()
					lcd.message("\x01 " + items[selection][:13] + "\n  " + items[selection + 1][:13])

	
	return selection + 1
	
