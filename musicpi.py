#! /usr/bin/python
# coding=utf-8

import RPi.GPIO as GPIO
import buttons
from Player import *
from Display import *

display = Display()
player = Player(display)
buttons.setup_buttons(player)

try:
    player.start()

    while True:
        print "a"
except KeyboardInterrupt:
    GPIO.cleanup()

GPIO.cleanup()
exit()
