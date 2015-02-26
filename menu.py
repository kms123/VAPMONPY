import Adafruit_CharLCD as LCD
import time

def Menu(lcd, items):
	lcd.create_char(1, [8, 12, 10, 9, 10, 12, 8, 0])

	lcd.clear()
	lcd.message("MENU")
	time.sleep(3.0)
	lcd.clear()
	lcd.message("\x01 "items[0]"\n  "items[1])
	
	selectionMade = False
	selection = 1
	
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
					selection = selection + 1
					lcd.clear()
					lcd.message("  " + items[0] + "\n\x01 " + items[1])
				if button[0] == LCD.UP:
					selection = selection - 1
					lcd.clear()
					lcd.message("\x01 " + items[selection]"\n  " + items[selectin + 1])

	
	return selection
	
