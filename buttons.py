#! /usr/bin/python
# coding=utf-8

import RPi.GPIO as gpio
import time
import commands

# pin 16, GPIO23
BUTTON_MODE = 23
BUTTON_CONFIRM = 23
BUTTON_NEXT = 23
BUTTON_PREV = 23



def action_press_button_loop(gpio_pin):
    print "O botão no pino %d foi pressionado!" % gpio_pin
    print "Saindo..."


def action_press_button(gpio_pin):
    print "Tratando o botão no pino %d que foi pressionado!" % gpio_pin


""" Configurando GPIO """
# Configurando o modo dos pinos como BCM
gpio.setmode(gpio.BCM)

# Configurando como INPUT e modo pull-down interno
gpio.setup(BUTTON_MODE, gpio.IN, pull_up_down=gpio.PUD_DOWN)
gpio.setup(BUTTON_CONFIRM, gpio.IN, pull_up_down=gpio.PUD_DOWN)
gpio.setup(BUTTON_NEXT, gpio.IN, pull_up_down=gpio.PUD_DOWN)
gpio.setup(BUTTON_PREV, gpio.IN, pull_up_down=gpio.PUD_DOWN)

# Adicionando um evento na mudança RISING 0V[LOW] - > 3.3V[HIGH]
gpio.add_event_detect(BUTTON_MODE, gpio.RISING, callback=commands.menu)
gpio.add_event_detect(BUTTON_CONFIRM, gpio.RISING, callback=commands.volumeincrease)
gpio.add_event_detect(BUTTON_NEXT, gpio.RISING, callback=commands.next_)
gpio.add_event_detect(BUTTON_PREV, gpio.RISING, callback=commands.previous)

# Junto com o parametro callback podemos utilizar ainda o bouncetime
# na linha abaixo estamos dizendo para ignorar nos primeiro 300ms
# gpio.add_event_detect(PIN, gpio.RISING, callback=action_press_button, bouncetime=300)

# while True:
#     print "Polling..."
#
#     if gpio.event_detected(PIN):
#         action_press_button_loop(PIN)
#         break
#
#     time.sleep(1)

gpio.cleanup()
exit()
