import Adafruit_CharLCD as LCD
import time

def Menu(lcd):
	lcd.create_char(1, [8, 12, 10, 9, 10, 12, 8, 0])

	lcd.clear()
	lcd.message("MENU")
	time.sleep(3.0)
	lcd.clear()
	lcd.message("\x01 Record\n  Transmit")
	time.sleep(7.0)
	
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
					selection = 2
					lcd.clear()
					lcd.message("  Record\n\x01 Transmit")
				if button[0] == LCD.UP:
					selection = 1
					lcd.clear()
					lcd.message("\x01 Record\n  Transmit")

	
	return selection
	
