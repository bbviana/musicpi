#! /usr/bin/python
# coding=utf-8

import subprocess
from models import *

statusStr = subprocess.check_output("mpc status", shell=True)
status = Status(statusStr)

print status.songName
print status.songProgress
print status.volume
