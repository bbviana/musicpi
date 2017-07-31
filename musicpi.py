#! /usr/bin/python
# coding=utf-8

import RPi.GPIO as GPIO
import buttons
import commands
import display

buttons.setup_buttons()

try:
    while True:
        print "a"
except KeyboardInterrupt:
    GPIO.cleanup()

GPIO.cleanup()
exit()
