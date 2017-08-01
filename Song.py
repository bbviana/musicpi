class Song:
    name = ""
    progress = ""
    volume = ""

    def __init__(self, status=None):
        if status is not None:
            self.parse_from_status(status)

    def parse_from_status(self, status):
        lines = status.splitlines(True)
        for line in lines:
            if line.startswith("["):
                self.progress = line
            elif line.startswith("volume"):
                self.volume = line.split()[0]
            else:
                self.name = line
