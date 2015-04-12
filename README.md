# VAPMONPY
Python code for the project.

_____________________________________________________________________
startup.sh : This is a bash script that executes the python project at the startup of the RaspberryPi.
_____________________________________________________________________
main.py : Main program for the project.  Execute main.py to start the program.  The lcd is initialised using the code from Adafruit.  This lcd is then passed into all other functions that need to write to the screen.  Main reads in the doctor code from the keypad, then displays the main menu selections.  Based on the return value from the menu, the proper sub routine (NFCread, Transmit or shutdown) is called.

_____________________________________________________________________
keypad.py : Standard active-low implementation for a 4x4 keypad.  Uses the internal pull-up resistors on the RaspberryPi.  In order to use the python gpio commands the following need to be installed on the Pi:

sudo apt-get install python-dev
sudo apt-get install python-rpi.gpio

The python-dev library is required for a lot of different things used in this project.  The gpio is used for the keypad, and reading the sensor.

_____________________________________________________________________
menu.py : Takes in a list of strings and the lcd, and displays a selection menu containing the list items on the lcd.  The up and down buttons on the lcd allow scrolling through the menu items, and either the select or right buttons makes a menu selection.  Returns an integer representing the selection.  The return value is the same as the position of the menu item in the list (1st item returns 1, second item returns 2...).  If the left button is pressed the return value is -1, allowing for returning back to higher levels of a menu if they are nested.

_____________________________________________________________________
nfcRead.py : This file is executed when the 'Record' option is chosen from the main menu.  THe first thing it does is read in a patient code form the NFC module.  In order to use the NFC module from Adafruit and the libnfc code, UART must be freed on the Pi.  This is done via sudo raspi-config, selecting option 7 (serial), then selecting No.

Next, the libnfc code must be downloaded and installed. We followed the tutorial from Adafruit: https://learn.adafruit.com/adafruit-nfc-rfid-on-raspberry-pi/building-libnfc

The libnfc includes functions to read from the NFC module.  The output from nfc-poll is saved in the file nfc.txt, and the specufic UID number is pulled out.

The user then enters the flow rate, and selects either ml/s or ml/min.

The sensor function is called and the number is saved into the .csv file, using the python-native csv writing functions.

_____________________________________________________________________
sensor.py : This file is used to interface with the ADC chip to read in from the analog sensor.  This connects to the MCP3008 SDC chip using a bit banged SPI interface.  The readings from the sensor are saved in a list, then an average of the pressures over the data collection is taken and returned.

_____________________________________________________________________
pressureaverage.py : This takes an average of the top 85% of the values of the data recorded from the sensor.  This is to eliminate the beginning and end of the dataset when the sensor will be reading near zero before the flow starts and after it ends.

_____________________________________________________________________
transmit.py : This file is called when the transmit function is selected from the main menu.  This function writes the csv file associated with the current doctor code to the UART file in the RaspberryPi OS.  The bluetooth module is connected to the UART in the RaspberryPi, and transmits each line of data that is written to the UART file.  The data transmission is not encrypted or secure in any way while it is being transmitted.  Before the transmit function is entered on the RaspberryPi, the iPhone app must be listening to the correct device.