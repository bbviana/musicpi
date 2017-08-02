import re


class Status:
    def __init__(self, status_str):
        self.songName = status_str.splitlines(True)[0].strip()

        result = re.search(r'\[(.*)\]', status_str, re.M | re.I).group(1)
        self.isPlaying = True if result == "playng" else False

        result = re.search(r'(\d+)%', status_str, re.M | re.I).group(1)
        self.songProgress = int(result)

        result = re.search(r'volume:(\d+)%', status_str, re.M | re.I)
        self.volume = int(result)



