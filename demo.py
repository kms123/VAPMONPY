import Adafruit_CharLCD as LCD
import time

from menu import Menu as Menu
from scroll import Scroll as Scroll

def Demo(lcd):
	lcd.set_color(1,1,1)
	lcd.clear()
	lcd.message("    Computer\n  Engineering")
	time.sleep(3)
	
	semesters = ["Year 2 Sem 1", "Year 2 Sem 2", "Year 3 Sem 1", "Year 3 Sem 2", "Year 4 Sem 1", "Year 4 Sem 2"]
	year2_1 = ["CMPT 116", "EE 202", "EE 205", "EE 221", "EE 265", "MATH 223"]
	desc2_1 = ["Computing I", "Electric and Magnetic Fields and Circuits", "Safety and Stewardship", "Analog Electronics", "Discrete Time Signals and Systems", "Calculus III"]
	year2_2 = ["CMPT 117", "EE 216", "EE 232", "EE 271", "EP 214", "MATH 224"]
	desc2_2 = ["Computing II", "Probability Statistics and Numerical Methods", "Digital Electronics", "Materials and Heat Transport", "Analog Signals and Systems", "Calculus IV"]
	year3_1 = ["CME 331", "CME 341", "CME 342", "CMPT 214", "CMPT 270", "EE 362"]
	desc3_1 = ["Microprocessor Based Embedded Systems", "Logic Design Using FPGAs", "VLSI Circuit Design", "Programming Principles and Practice", "Developing Object-Oriented Systems", "Digital Signal Processing"]
	year3_2 = ["CME 332", "CMPT 280", "EE 365", "GE 348", "RCM 300", "Science Elec"]
	desc3_2 = ["Real Time Computing", "Intermediate Data Structures and Algorithms", "Algorithms and Circuits with Finite Precision Arithmetics", "Engineering Economics", "Effective Professional Communication", "Science Elective"]
	year4_1 = ["CME 433", "CME 435", "CME 495", "CMPT 332", "CMPT 350", "CMPT 370", "EE 456", "EE 461", "Senior Hum"]
	desc4_1 = ["Digital Systems Architecture", "Verification of Digital Systems", "Capstone Design Project", "Operating Systems Concepts", "Web Programming", "Intermediate Software Engineering", "Digital Communication", "Digital Filter Design", "Senoir Humanities"]
	year4_2 = ["CME 451", "CME 495", "CMPT 432", "CMPT 434", "EE 465", "GE 449", "Compl Studies"]
	desc4_2 = ["Transport Networks", "Capstone Design Project", "Advanced Operating Systems Concepts", "Computer Networks", "Design of a DSP System", "Engineering in Society", "Complementary Studies Elective"]
	
	selection = 0
	level = 1
	course = 0
	
	buttons = ((LCD.SELECT, False),
			(LCD.LEFT, True),
			(LCD.UP, False),
			(LCD.DOWN, False),
			(LCD.RIGHT, False))
	while True:
		selectionMade = False
#		print "Level: " + str(level)

		if level == 1:
			selection = Menu(lcd, semesters)
			level += 1		

		elif level == 2:
			level += 1
			if selection == 1:
				course = Menu(lcd, year2_1) - 1
			elif selection == 2:
				course = Menu(lcd, year2_2) - 1
			elif selection == 3:
				course = Menu(lcd, year3_1) - 1
			elif selection == 4:
				course = Menu(lcd, year3_2) - 1
			elif selection == 5:
				course = Menu(lcd, year4_1) - 1
			elif selection == 6:
				course = Menu(lcd, year4_2) - 1
			else:
				lcd.clear()
				lcd.message("OOPS...")
				
		elif level == 3:
			lcd.set_color(1,1,0)
			
			if course == -2:
				level -= 2
			else:
				if selection == 1:
					lcd.clear()
#					lcd.message(desc2_1[course])
					Scroll(lcd, desc2_1[course])
				elif selection == 2:
					lcd.clear()
#					lcd.message(desc2_2[course])
					Scroll(lcd, desc2_2[course])
				elif selection == 3:
					lcd.clear()
#					lcd.message(desc3_1[course])
					Scroll(lcd, desc3_1[course])
				elif selection == 4:
					lcd.clear()
#					lcd.message(desc3_2[course])
					Scroll(lcd, desc3_2[course])
				elif selection == 5:
					lcd.clear()
#					lcd.message(desc4_1[course])
					Scroll(lcd, desc4_1[course])
				elif selection == 6:
					lcd.clear()
#					lcd.message(desc4_2[course])
					Scroll(lcd, desc4_2[course])
				else:
					lcd.clear()
					lcd.message("OOPS...")	
	
#				while not selectionMade:
#					for button in buttons:
#						if lcd.is_pressed(button[0]):
#							selectionMade = button[1]
#							if button[0] == LCD.LEFT:
				level = 2
		else:
			lcd.clear()
			lcd.set_color(1,0,0)
