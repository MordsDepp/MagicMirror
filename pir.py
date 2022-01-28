#!/usr/bin/python3

import sys
import time
import RPi.GPIO as io
import subprocess

io.setmode(io.BOARD)		#setup IO Pins in board mode
TIMEOUT = 30			#seconds to screen blank
BOOTDELAY = 40			#programm delay to ensure correct boot
PIR_PIN = 22			#PIR signal

io.setup(PIR_PIN, io.IN)

def main():
	
	time.sleep(BOOTDELAY)
	
	while True:
		if io.input(PIR_PIN):
			turn_on()
			time.sleep(TIMEOUT)
		
		else:
			turn_off()
	time.sleep(.1)

def turn_on():
	subprocess.call(["xscreensaver-command", "-deactivate"])

def turn_off():
	subprocess.call(["xscreensaver-command", "-activate"])

try:
	main()

except KeyboardInterrupt:
	print("Exit")
