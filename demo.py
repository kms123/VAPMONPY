import Adafruit_CharLCD as LCD
import time

from menu import Menu as Menu

def Demo(lcd):
	lcd.set_color(1,1,1)
	lcd.clear()
	lcd.message("    Computer\n  Engineering")
	time.sleep(2)
	
	semesters = ["Year 2 Sem 1", "Year 2 Sem 2", "Year 3 Sem 1", "Year 3 Sem 2", "Year 4 Sem 1", "Year 4 Sem 2"]
	year2_1 = ["CMPT 116", "EE 202", "EE 205", "EE 221", "EE 265", "MATH 223"]
	desc2_1 = ["Computing I", "Electric and\nMagnetic Fields and Circuits", "Safety and\nStewardship", "Analog\nElectronics", "Discrete Time\nSignals and Systems", "Calculus III"]
	year2_2 = ["CMPT 117", "EE 216", "EE 232", "EE 271", "EP 214", "MATH 224"]
	desc2_2 = ["Computing II", "Probability Stat\nistics and Numerical Methods", "Digital\nElectronics", "Materials and\nHeat Transport", "Analog Signals\nand Systems", "Calculus IV"]
	year3_1 = ["CME 331", "CME 341", "CME 342", "CMPT 214", "CMPT 270", "EE 362"]
	desc3_1 = ["Microprocessor\nBased Embedded Systems", "Logic Design\nUsing FPGAs", "VLSI Circuit\nDesign", "Programming\nPrinciples and Practice", "Developing Object\n-Oriented Systems", "Digital Signal\nProcessing"]
	year3_2 = ["CME 332", "CMPT 280", "EE 365", "GE 348", "RCM 300", "Science Elec"]
	desc3_2 = ["Real Time\nComputing", "Intermediate Data\nStructures and Algorithms", "Algorithms and\nCircuits with Finite Precision Arithmetics", "Engineering\nEconomics", "Effective\nProfessional Communication", "Science\nElective"]
	year4_1 = ["CME 433", "CME 435", "CME 495", "CMPT 332", "CMPT 350", "CMPT 370", "EE 456", "EE 461", "Senior Hum"]
	desc4_1 = ["Digital Systems\nArchitecture", "Verification of\nDigital Systems", "Capstone\nDesign Project", "Operating\nSystems Concepts", "Web Programming", "Intermediate\nSoftware Engineering", "Digital\nCommunication", "Digital Filter\nDesign", "Senoir\nHumanities"]
	year4_2 = ["CME 451", "CME 495", "CMPT 432", "CMPT 434", "EE 465", "GE 449", "Compl Studies"]
	desc4_2 = ["Transport\nNetworks", "Capstone\nDesign Project", "Advanced Operating\nSystems Concepts", "Computer\nNetworks", "Design of a DSP\nSystem", "Engineering\nin Society", "Complementary\nStudies Elective"]
	
	selection = 0
	level = 1
	course = 0
	
	while True:
		if level == 1:
			selection = Menu(lcd, semesters)
		
		if level == 2:
			if selection == 1:
				course = Menu(lcd, year2_1)
			elif selection == 2:
				course = Menu(lcd, year2_2)
			elif selection == 3:
				course = Menu(lcd, year3_1)
			elif selection == 4:
				course = Menu(lcd, year3_2)
			elif selection == 5:
				course = Menu(lcd, year4_1)
			elif selection == 6:
				course = Menu(lcd, year4_2)
			else:
				lcd.clear()
				lcd.message("OOPS...")
				
		if level == 3:
			lcd.set_color(1,1,0)
			if selection == 1:
				lcd.clear()
				lcd.message(desc2_1[course])
			elif selection == 2:
				lcd.clear()
				lcd.message(desc2_2[course])
			elif selection == 3:
				lcd.clear()
				lcd.message(desc3_1[course])
			elif selection == 4:
				lcd.clear()
				lcd.message(desc3_2[course])
			elif selection == 5:
				lcd.clear()
				lcd.message(desc4_1[course])
			elif selection == 6:
				lcd.clear()
				lcd.message(desc4_2[course])
			else:
				lcd.clear()
				lcd.message("OOPS...")	