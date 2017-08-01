#! /usr/bin/python
# coding=utf-8

import subprocess
import display
from Song import *


class Player:
    def __init__(self):
        self.menuMode = "song"  # song | playlist | volume
        self.songMode = "pause"  # play | pause
        self.current_playlist = 0
        self.current_song = Song()

    def start(self):
        # guardar ultima em um arquivo
        self.loadplaylist(0)

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
        self.current_playlist += 1

    def playlistprevious(self):
        self.current_playlist -= 1

    def songnext(self):
        runmpccommand("next")
        self.current_song = Song(status())

    def songprevious(self):
        runmpccommand("prev")
        self.current_song = Song(status())

    def playpause(self):
        if self.songMode == "play":
            self.pause()
        elif self.songMode == "pause":
            self.play()

    def play(self):
        self.songMode = "play"
        runmpccommand("play")
        self.current_song = Song(status())

    def pause(self):
        self.songMode = "pause"
        runmpccommand("pause")

    def volumeincrease(self):
        runmpccommand("volume +10")
        self.current_song.parse_from_status(status())

    def volumedecrease(self):
        runmpccommand("volume -10")
        self.current_song.parse_from_status(status())

    def loadplaylist(self, index):
        runmpccommand("clear")
        playlist_name = self.playlistname(index)
        runmpccommand("load", playlist_name)
        runmpccommand("play", "1")

    def playlistname(self, index):
        p1 = subprocess.Popen(["mpc", "lsplaylists"], stdout=subprocess.PIPE)
        p2 = subprocess.Popen(["sed", "-n", str(index + 1) + "p"],
                              stdin=p1.stdout,
                              stdout=subprocess.PIPE)
        p1.stdout.close()  # Allow p1 to receive a SIGPIPE if p2 exits.
        output, err = p2.communicate()
        return output

    def currentplaylist(self):
        return self.playlistname(self.current_playlist)


def status():
    return runmpccommand("status")


def runmpccommand(command, args=None):
    if args is None:
        args = []
    return subprocess.check_output(["mpc " + command, args], shell=True)
