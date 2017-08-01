#! /usr/bin/python
# coding=utf-8

import RPi.GPIO as GPIO

BUTTON_MODE = 26
BUTTON_CONFIRM = 19
BUTTON_NEXT = 13
BUTTON_PREV = 6


def setup_buttons(player):
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(BUTTON_MODE, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(BUTTON_CONFIRM, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(BUTTON_NEXT, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(BUTTON_PREV, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    GPIO.add_event_detect(BUTTON_MODE, GPIO.FALLING, callback=player.menu)
    GPIO.add_event_detect(BUTTON_CONFIRM, GPIO.FALLING, callback=player.confirm)
    GPIO.add_event_detect(BUTTON_NEXT, GPIO.FALLING, callback=player.next_)
    GPIO.add_event_detect(BUTTON_PREV, GPIO.FALLING, callback=player.previous)