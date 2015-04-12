import Adafruit_CharLCD as LCD
import time

def Menu(lcd, items):
	len0 = 13
	len1 = 13
	#Create the arrow indicator for the menu.
	lcd.create_char(1, [8, 12, 10, 9, 10, 12, 8, 0])
	
	#if there is only 1 item in the  menu, add an empty string to display on the second line of the lcd.
	while len(items) < 2:
		items.append("")
	
	#If an empty list is passed in, make the first item an empty string instead of None.
	if items[0] == None:
		items[0] = ""
	#If a menu item is shorter then the max 13 characters, set the length to be less.
	if len(items[0]) < 13:
		len0 = len(items[0])
	if len(items[1]) < 13:
		len1 = len(items[1])		

	#Set the lcd color, clear the contents and then write the first 2 list items to the lcd, with the arrow indicator on the first item.
	lcd.set_color(0,1,0)
	lcd.clear()
	lcd.message("\x01 " + items[0][:len0] + "\n  " + items[1][:len1])
	
	selectionMade = False
	selection = 0
	
	#Create the buttons for the menu.  The names of the buttons are from  the Adafruit libraries.  The True/False values are set to that depending on which button you press you may or may not exit the menu.  Up and down scrolling does not exit the menu, but the other 3 buttons will.
	buttons = (	(LCD.SELECT, True),
			(LCD.LEFT, True),
			(LCD.UP, False),
			(LCD.DOWN, False),
			(LCD.RIGHT, True))
			
	while not selectionMade:
		for button in buttons:
			if lcd.is_pressed(button[0]):
				selectionMade = button[1] #Leave menu or not.
				if button[0] == LCD.LEFT: #Back out of the menu without a selection.
					selection = -2
				if button[0] == LCD.DOWN: #Select the next item down in the menu and redraw the contents of the lcd.
					if (selection < len(items)-1):
						selection = selection + 1
					print "Selection: " + str(selection)
					lcd.clear()
					lcd.message("  " + items[selection-1][:13] + "\n\x01 " + items[selection][:13])
				if button[0] == LCD.UP: #Select the previous item up in the menu, and redraw the contents of the lcd.
					if (selection > 0):
						selection = selection - 1
					print "Selection: " + str(selection)
					lcd.clear()
					lcd.message("\x01 " + items[selection][:13] + "\n  " + items[selection + 1][:13])

	
	return selection + 1
	
