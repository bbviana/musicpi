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
        previous()
    elif command == "next":
       next_()
    elif command == "playpause":
        if songMode == "play":
            pause()
        elif songMode == "pause":
            play()
    elif command == "currentPlaylist":
        currentplaylist()
    elif command == "status":
        status()
    console("--")


def menu():
    global menuMode
    if menuMode == "song":
        menuMode = "playlist"
    elif menuMode == "playlist":
        menuMode = "song"

    console('menu: ' + menuMode)


def previous():
    if menuMode == "playlist":
        playlistprevious()
    elif menuMode == "song":
        songprevious()


def next_():
    if menuMode == "playlist":
        playlistnext()
    elif menuMode == "song":
        songnext()


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


commands("currentplaylist")
commands("playpause")
commands("menu")
commands("next")
commands("currentplaylist")
commands("previous")
commands("currentplaylist")
commands("menu")
commands("next")
commands("previous")
commands("playpause")
commands("status")
