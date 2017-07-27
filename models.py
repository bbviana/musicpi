class Status:
    songName = ""
    songProgress = ""
    volume = ""

    def __init__(self, statusstr):
        lines = statusstr.splitlines(True)
        for line in lines:
            if line.startswith("["):
                self.songProgress = line
            elif line.startswith("volume"):
                self.volume = line.split()[0]
            else:
                self.songName = line

