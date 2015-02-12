import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(12, GPIO.OUT)
print "After setup."
#while True:
GPIO.output(12, 1)
time.sleep(5)
	
GPIO.output(12, 0)
time.sleep(2)

GPIO.output(12, 1)
time.sleep(5)

GPIO.cleanup()