import json
import os
import time

class Entry:
    def __init__(self, filePath, episode):
        self.filePath = os.path.abspath(filePath)
        dirName, fileName = os.path.split(self.filePath)
        self.fileName = fileName
        self.dirName = dirName
        self.ed2k = episode.ed2k
        self.size = episode.size
        self.aid = episode.aid
        self.epno = episode.epno
        self.anime = episode.romaji_name

    def update_path(self, dirName):
        self.dirName = os.path.abspath(dirName)
        self.filePath = os.path.join(self.dirName, self.fileName)

def as_json(o):
    return o.__dict__

def export_entries(entries):
    with open('anifs-export_%d.json' % time.time(), 'w') as outfile:
        json.dump(entries, outfile, default=as_json, ensure_ascii=False)

