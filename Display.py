#! /usr/bin/python
# coding=utf-8

import I2C_LCD_driver
import chars

MOVE_TO_LINE1 = 0x80
MOVE_TO_LINE2 = 0xC0


class Display:
    def __init__(self):
        self.lcdi2c = I2C_LCD_driver.LCD()

    def print_(self, line1, line2):
        self.lcdi2c.lcd_clear()
        self.lcdi2c.lcd_display_string(line1, 1, 0)
        self.lcdi2c.lcd_display_string(line2, 2, 0)

    def print_on_line1(self, line1):
        self.lcdi2c.lcd_clear()
        self.lcdi2c.lcd_display_string(line1, 1, 0)

    def print_song_status(self, song):
        self.lcdi2c.lcd_load_custom_chars(self.status_chars(song.playing) + self.progress_chars(song.progress))
        self.lcdi2c.lcd_write(MOVE_TO_LINE2)
        # pos 0
        self.lcdi2c.lcd_write_char(0)

        # pos 1: espaço

        self.lcdi2c.lcd_write(MOVE_TO_LINE2 + 2)

        # pos 2
        self.lcdi2c.lcd_write_char(1)
        # pos 3
        self.lcdi2c.lcd_write_char(2)

    def status_chars(self, playing):
        return chars.play if playing else chars.pause

    def progress_chars(self, progress):
        if progress <= 11:
            # [____ ____]
            return [chars.progressLeft0, chars.progressRight0]
        if progress <= 22:
            # [|___ ____]
            return [chars.progressLeft1, chars.progressRight0]
        if progress <= 33:
            # [||__ ____]
            return [chars.progressLeft2, chars.progressRight0]
        if progress <= 44:
            # [|||_ ____]
            return [chars.progressLeft3, chars.progressRight0]
        if progress <= 55:
            # [|||| ____]
            return [chars.progressLeftFull, chars.progressRight0]
        if progress <= 66:
            # [|||| |___]
            return [chars.progressLeftFull, chars.progressRight1]
        if progress <= 77:
            # [|||| ||__]
            return [chars.progressLeftFull, chars.progressRight2]
        if progress <= 88:
            # [|||| |||_]
            return [chars.progressLeftFull, chars.progressRight3]

        # 89 - 100
        # [|||| ||||]
        return [chars.progressLeftFull, chars.progressRightFull]