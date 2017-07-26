#!/usr/bin/env python

import subprocess

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
    print "playlistnext"


def playlistprevious():
    global currentPlaylist
    currentPlaylist -= 1
    print "playlistprevious"


def currentplaylist():
    p1 = subprocess.Popen(["mpc", "lsplaylists"], stdout=subprocess.PIPE)
    p2 = subprocess.Popen(["sed", "-n", str(currentPlaylist + 1) + "p"], stdin=p1.stdout, stdout=subprocess.PIPE)
    p1.stdout.close()  # Allow p1 to receive a SIGPIPE if p2 exits.
    output, err = p2.communicate()
    print output.strip()


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


def status():
    subprocess.call("mpc status", shell=True)


def console(msg):
    subprocess.call("echo " + msg, shell=True)


currentplaylist()
commands("playpause")
commands("menu")
commands("next")
currentplaylist()
commands("previous")
currentplaylist()
commands("menu")
commands("next")
commands("previous")
commands("playpause")
status()
