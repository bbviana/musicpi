#! /usr/bin/python
# coding=utf-8

import RPi.GPIO as GPIO
import buttons
from Player import *


player = Player()
buttons.setup_buttons(player)

# PAREI
try:
    player.start()

    while True:
        print "a"
except KeyboardInterrupt:
    GPIO.cleanup()

GPIO.cleanup()
exit()
