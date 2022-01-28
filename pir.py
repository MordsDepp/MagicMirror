#!/usr/bin/python

import sys
import time
import RPi.GPIO as io
import subprocess

io.setmode(io.BOARD)		#setup IO Pins in board mode
TIMEOUT = 30			#seconds to screen blank
BOOTDELAY = 40			#programm delay to ensure correct boot
PIR_PIN = 22			#PIR signal
STATE = 0
PREV_STATE = 1

io.setup(PIR_PIN, io.IN)

def main():
	time.sleep(BOOTDELAY)
	
	while True:
		STATE = io.input(PIR_PIN)
		
		if STATE==1 and PREV_STATE==0:
			turn_on()
			PREV_STATE = 1
			time.sleep(TIMEOUT)
			
		
		elif STATE==0 and PREV_STATE==1:
			turn_off()
			PREV_STATE = 0
			
	time.sleep(.1)

def turn_on():
	subprocess.call(["xscreensaver-command", "-deactivate"])

def turn_off():
	subprocess.call(["xscreensaver-command", "-activate"])

try:
	main()

except KeyboardInterrupt:
	print("Exit")