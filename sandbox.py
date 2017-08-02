#! /usr/bin/python
# coding=utf-8

import re

string = """
Taylor Davis - Chrono Trigger Theme
[paused]  #1/121   0:06/2:12 (4%)
volume:100%   repeat: off   random: off   single: off   consume: off
"""

searchObj = string.strip().splitlines(True)[0].strip()
print searchObj

searchObj = re.search(r'\[(.*)\]', string, re.M | re.I)
print searchObj.group(1)

searchObj = re.search(r'(\d+)%', string, re.M | re.I)
print int(searchObj.group(1))

searchObj = re.search(r'volume:(\d+)%', string, re.M | re.I)
print int(searchObj.group(1))

b = "a"
print b == "a"
