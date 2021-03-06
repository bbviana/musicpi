#! /usr/bin/python
# coding=utf-8

import subprocess
from Song import *

# PAREI
# Song a partir de Status

class Player:
    def __init__(self, display):
        self.display = display
        self.menuMode = "playlist"  # playlist | song | volume
        self.current_song = Song()
        self.current_playlist_index = 0
        self.current_playlist_name = None
        self.volume = 0

    def loop(self):
        self.print_info()

    def print_info(self):
        if self.menuMode == "playlist":
            self.display.print_("PLAYLIST", self.current_playlist_name)
            return
        if self.menuMode == "song":
            self.display.print_on_line1(self.current_song.name)
            self.display.print_song_status(self.current_song)
            return
        if self.menuMode == "volume":
            self.display.print_("VOLUME", str(self.volume) + "%")
            return

    def start(self):
        # guardar ultima em um arquivo
        self.loadplaylist(0)

    # playlist > song > volume > playlist
    def menu(self):
        if self.menuMode == "playlist":
            self.menuMode = "song"
        if self.menuMode == "song":
            self.menuMode = "volume"
        if self.menuMode == "volume":
            self.menuMode = "playlist"

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
