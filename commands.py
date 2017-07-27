#!/usr/bin/env python

import subprocess
import display

menuMode = "song"  # song | playlist | volume
songMode = "pause"  # play | pause
currentPlaylist = 0


# song > volume > playlist > song ...
def menu():
    global menuMode
    if menuMode == "song":
        menuMode = "volume"
    elif menuMode == "volume":
        menuMode = "playlist"
    elif menuMode == "playlist":
        menuMode = "song"

    console('menu: ' + menuMode)


def confirm():
    global menuMode
    if menuMode == "playlist":
        play()
        menuMode = "song"
    else:
        playpause()


def previous():
    if menuMode == "playlist":
        playlistprevious()
    elif menuMode == "song":
        songprevious()
    elif menuMode == "volume":
        volumedecrease()


def next_():
    if menuMode == "playlist":
        playlistnext()
    elif menuMode == "song":
        songnext()
    elif menuMode == "volume":
        volumeincrease()


def playlistnext():
    global currentPlaylist
    currentPlaylist += 1


def playlistprevious():
    global currentPlaylist
    currentPlaylist -= 1


def songnext():
    runmpccommand("next")


def songprevious():
    runmpccommand("prev")


def playpause():
    if songMode == "play":
        pause()
    elif songMode == "pause":
        play()


def play():
    global songMode
    songMode = "play"
    runmpccommand("play")


def pause():
    global songMode
    songMode = "pause"
    runmpccommand("pause")


def volumeincrease():
    runmpccommand("volume +10")


def volumedecrease():
    runmpccommand("volume -10")


def currentplaylist():
    p1 = subprocess.Popen(["mpc", "lsplaylists"], stdout=subprocess.PIPE)
    p2 = subprocess.Popen(["sed", "-n", str(currentPlaylist + 1) + "p"], stdin=p1.stdout, stdout=subprocess.PIPE)
    p1.stdout.close()  # Allow p1 to receive a SIGPIPE if p2 exits.
    output, err = p2.communicate()
    console(output.strip())


def status():
    runmpccommand("status")


def runmpccommand(command):
    subprocess.call("mpc " + command, shell=True)


def console(msg):
    subprocess.call("echo " + msg, shell=True)


