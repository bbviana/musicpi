#! /usr/bin/python
# coding=utf-8

import RPi.GPIO as gpio

BUTTON_MODE = 26
BUTTON_CONFIRM = 19
BUTTON_NEXT = 13
BUTTON_PREV = 6

def setup_buttons():
    gpio.setmode(gpio.BCM)

    gpio.setup(BUTTON_MODE, gpio.IN, pull_up_down=gpio.PUD_UP)
    gpio.setup(BUTTON_CONFIRM, gpio.IN, pull_up_down=gpio.PUD_UP)
    gpio.setup(BUTTON_NEXT, gpio.IN, pull_up_down=gpio.PUD_UP)
    gpio.setup(BUTTON_PREV, gpio.IN, pull_up_down=gpio.PUD_UP)
