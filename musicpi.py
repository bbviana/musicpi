#! /usr/bin/python
# coding=utf-8

import RPi.GPIO as GPIO
import buttons
from Player import *

buttons.setup_buttons()

player = Player()

# PAREI
try:
    while True:
        print "a"
except KeyboardInterrupt:
    GPIO.cleanup()

GPIO.cleanup()
exit()
