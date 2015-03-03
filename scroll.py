import Adafruit_CharLCD as LCD
import time

def Scroll(lcd, text):
	output = text + "   "
	length  = len(output)
	buttonPressed = False
	i = 0
	j = 16
	
	buttons = ((LCD.SELECT, False),
		(LCD.LEFT, False),
		(LCD.UP, False),
		(LCD.DOWN, False),
		(LCD.RIGHT, True))
	lcd.clear()

	while not buttonPressed:
		time.sleep(.3)

		if j == length:
			j = 0

		if i == length:
			i = 0

		if j < i:
			lcd.clear()
			lcd.message(output[i:-1] + output[0:j+1])
					
		else:
			lcd.clear()
			lcd.message(output[i:j])

		i += 1
		j += 1

		for button in buttons:
			if lcd.is_pressed(button[0]):
				buttonPressed = button[1]		
