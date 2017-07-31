#! /usr/bin/python
# coding=utf-8

import I2C_LCD_driver

lcdi2c = I2C_LCD_driver.lcd()


def print_on_display(line1, line2):
    lcdi2c.lcd_clear()
    lcdi2c.lcd_display_string(line1, 1, 0)
    lcdi2c.lcd_display_string(line2, 2, 0)
