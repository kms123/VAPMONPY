import os
import RPi.GPIO as GPIO

def KeypadRead():
	GPIO.setmode(GPIO.BCM)

	GPIO.setup(4, GPIO.IN, pull_up_down = GPIO.PUD_UP)
	GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)

	GPIO.setup(18, GPIO.OUT)
	GPIO.setup(23, GPIO.OUT)
	GPIO.setup(24, GPIO.OUT)
	GPIO.setup(25, GPIO.OUT)

	keyPressed = 'X'
	GPIO.output(18, 1)
	GPIO.output(23, 1)
	GPIO.output(24, 1)
	GPIO.output(25, 1)

	while(keyPressed == 'X'):
		GPIO.output(18, 0)
		if(GPIO.input(4) == 0):
			keyPressed = '1'
			while(GPIO.input(4) == 0):
				pass
		if(GPIO.input(17) == 0):
			keyPressed = '4'
			while(GPIO.input(17) == 0):
				pass
		if(GPIO.input(27) == 0):
			keyPressed = '7'
			while(GPIO.input(27) == 0):
				pass
		if(GPIO.input(22) == 0):
			keyPressed = '*'
			while(GPIO.input(22) == 0):
				pass

		GPIO.output(18, 1)
		GPIO.output(23, 0)

		if(GPIO.input(4) == 0):
			keyPressed = '2'
			while(GPIO.input(4) == 0):
				pass
		if(GPIO.input(17) == 0):
			keyPressed = '5'
			while(GPIO.input(17) == 0):
				pass
		if(GPIO.input(27) == 0):
			keyPressed = '8'
			while(GPIO.input(27) == 0):
				pass
		if(GPIO.input(22) == 0):
			keyPressed = '0'
			while(GPIO.input(22) == 0):
				pass

		GPIO.output(23, 1)
		GPIO.output(24, 0)

		if(GPIO.input(4) == 0):
			keyPressed = '3'
			while(GPIO.input(4) == 0):
				pass
		if(GPIO.input(17) == 0):
			keyPressed = '6'
			while(GPIO.input(17) == 0):
				pass
		if(GPIO.input(27) == 0):
			keyPressed = '9'
			while(GPIO.input(27) == 0):
				pass
		if(GPIO.input(22) == 0):
			keyPressed = "#"
			while(GPIO.input(22) == 0):
				pass

		GPIO.output(24, 1)
		GPIO.output(25, 0)

		if(GPIO.input(4) == 0):
			keyPressed = 'A'
			while(GPIO.input(4) == 0):
				pass
		if(GPIO.input(17) == 0):
			keyPressed = 'B'
			while(GPIO.input(17) == 0):
				pass
		if(GPIO.input(27) == 0):
			keyPressed = 'C'
			while(GPIO.input(27) == 0):
				pass
		if(GPIO.input(22) == 0):
			keyPressed = 'D'
			while(GPIO.input(22) == 0):
				pass

		GPIO.output(25, 1)

	GPIO.cleanup()

	return keyPressed
