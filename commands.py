#!/usr/bin/env python

import os

menuMode = "song"  # song | playlist
songMode = "pause"  # play | pause
currentPlaylist = 0


def commands(command):
    global menuMode
    if command == "menu":
        menu()
    elif command == "volumeincrease":
        volumeincrease()
    elif command == "volumedecrease":
        volumedecrease()
    elif command == "previous":
        if menuMode == "playlist":
            playlistprevious()
        elif menuMode == "song":
            songprevious()
    elif command == "next":
        if menuMode == "playlist":
            playlistnext()
        elif menuMode == "song":
            songnext()
    elif command == "playpause":
        if songMode == "play":
            pause()
        elif songMode == "pause":
            play()


def menu():
    global menuMode
    if menuMode == "song":
        menuMode = "playlist"
    elif menuMode == "playlist":
        menuMode = "song"

    console('menu: ' + menuMode)


def playlistnext():
    global currentPlaylist
    currentPlaylist += 1


def playlistprevious():
    global currentPlaylist
    currentPlaylist -= 1
    print "playlistprevious"

# PAREI
def currentplaylist():
    os.system("mpc lsplaylists | sed -n '1p'")


def songnext():
    print "songnext"


def songprevious():
    print "songprevious"


def play():
    global songMode
    songMode = "play"
    print "play"


def pause():
    global songMode
    songMode = "pause"
    print "pause"


def volumeincrease():
    print "volume +"


def volumedecrease():
    print "volume -"


def console(msg):
    os.system("echo " + msg)


commands("playpause")
commands("menu")
commands("next")
commands("previous")
commands("menu")
commands("next")
commands("previous")
commands("playpause")
currentPlaylist()