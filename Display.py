#! /usr/bin/python
# coding=utf-8

import I2C_LCD_driver

LCD_CMD_WRITE_LINE1 = 0x80
LCD_CMD_WRITE_LINE2 = 0xC0


class Display:
    def __init__(self):
        self.lcdi2c = I2C_LCD_driver.LCD()

    def print_(self, line1, line2):
        self.lcdi2c.lcd_clear()
        self.lcdi2c.lcd_display_string(line1, 1, 0)
        self.lcdi2c.lcd_display_string(line2, 2, 0)
    # PAREI
    def print_song_status(self):
        self.lcdi2c.lcd_load_custom_chars(play_pause_chars)
        self.lcdi2c.lcd_write(LCD_CMD_WRITE_LINE2)
        self.lcdi2c.lcd_write_char(0)


play_pause_chars = [
    # [0] PLAY
    [
        0b11000,
        0b01100,
        0b00110,
        0b00011,
        0b00011,
        0b00110,
        0b01100,
        0b11000
    ],

    # [1] PAUSE
    [
        0b11011,
        0b11011,
        0b11011,
        0b11011,
        0b11011,
        0b11011,
        0b11011,
        0b11011
    ]
]

progress_chars = [
    # [0] [
    [
        0b11111,
        0b10000,
        0b10000,
        0b10000,
        0b10000,
        0b10000,
        0b10000,
        0b11111
    ],

    # [1] [|___
    [
        0b11111,
        0b11000,
        0b11000,
        0b11000,
        0b11000,
        0b11000,
        0b11000,
        0b11111
    ],

    # [2] [||__
    [
        0b11111,
        0b11100,
        0b11100,
        0b11100,
        0b11100,
        0b11100,
        0b11100,
        0b11111
    ],

    # [3] [|||_
    [
        0b11111,
        0b11110,
        0b11110,
        0b11110,
        0b11110,
        0b11110,
        0b11110,
        0b11111
    ],

    # [4] [||||
    [
        0b11111,
        0b11111,
        0b11111,
        0b11111,
        0b11111,
        0b11111,
        0b11111,
        0b11111
    ],

    # [5] ____]
    [
        0b11111,
        0b00001,
        0b00001,
        0b00001,
        0b00001,
        0b00001,
        0b00001,
        0b11111
    ],

    # [6] |___]
    [
        0b11111,
        0b10001,
        0b10001,
        0b10001,
        0b10001,
        0b10001,
        0b10001,
        0b11111
    ],

    # [7] ||__]
    [
        0b11111,
        0b11001,
        0b11001,
        0b11001,
        0b11001,
        0b11001,
        0b11001,
        0b11111
    ],

    # [8] |||_]
    [
        0b11111,
        0b11101,
        0b11101,
        0b11101,
        0b11101,
        0b11101,
        0b11101,
        0b11111
    ],

    # [9] ||||]
    [
        0b11111,
        0b11111,
        0b11111,
        0b11111,
        0b11111,
        0b11111,
        0b11111,
        0b11111
    ]

]
