import argparse
import os

import anifs.anidb as anidb

def add_files(conn, args):
    if conn.authed():
        for filePath in args.files:
            if os.path.isfile(filePath):
                anidb.add_episode(conn, filePath, args.storage)

