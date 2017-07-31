#! /usr/bin/python
# coding=utf-8

import subprocess
import display
from Song import *


class Player:

    def __init__(self):
        self.menuMode = "song"  # song | playlist | volume
        self.songMode = "pause"  # play | pause
        self.currentPlaylist = 0
        self.currentSong = None

    def start(self):
        # PAREI
        return ""

    @property
    def currentsong(self):
        return self.currentSong

    @currentsong.setter
    def currentsong(self, value):
        self.currentSong = Song(value)

    # song > volume > playlist > song ...
    def menu(self):
        if self.menuMode == "song":
            self.menuMode = "volume"
        elif self.menuMode == "volume":
            self.menuMode = "playlist"
        elif self.menuMode == "playlist":
            self.menuMode = "song"

        display.print_on_display('Menu', self.menuMode)

    def confirm(self):
        if self.menuMode == "playlist":
            self.menuMode = "song"
            self.play()
        else:
            self.playpause()

    def previous(self):
        if self.menuMode == "playlist":
            self.playlistprevious()
        elif self.menuMode == "song":
            self.songprevious()
        elif self.menuMode == "volume":
            self.volumedecrease()

    def next_(self):
        if self.menuMode == "playlist":
            self.playlistnext()
        elif self.menuMode == "song":
            self.songnext()
        elif self.menuMode == "volume":
            self.volumeincrease()

    def playlistnext(self):
        self.currentPlaylist += 1

    def playlistprevious(self):
        self.currentPlaylist -= 1

    def songnext(self):
        runmpccommand("next")

    def songprevious(self):
        runmpccommand("prev")

    def playpause(self):
        if self.songMode == "play":
            self.pause()
        elif self.songMode == "pause":
            self.play()

    def play(self):
        self.songMode = "play"
        runmpccommand("play")

    def pause(self):
        self.songMode = "pause"
        runmpccommand("pause")

    def volumeincrease(self):
        runmpccommand("volume +10")

    def volumedecrease(self):
        runmpccommand("volume -10")

    def loadplaylist(self, index):
        playlist_name = self.playlist(index)
        runmpccommand("load", playlist_name)

    def playlist(self, index):
        p1 = subprocess.Popen(["mpc", "lsplaylists"], stdout=subprocess.PIPE)
        p2 = subprocess.Popen(["sed", "-n", str(index + 1) + "p"],
                          stdin = p1.stdout,
                          stdout = subprocess.PIPE)
        p1.stdout.close()  # Allow p1 to receive a SIGPIPE if p2 exits.
        output, err = p2.communicate()
        return output

    def currentplaylist(self):
        return self.playlist(self.currentPlaylist)


def status():
    runmpccommand("status")


def runmpccommand(command, args = None):
    if args is None:
        args = []
    subprocess.call(["mpc " + command, args], shell=True)