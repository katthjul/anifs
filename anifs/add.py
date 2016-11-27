import argparse
import os

import anifs.anidb as anidb

def add_files(conn, args):
    if conn.authed():
        for filePath in args.files:
            if os.path.isfile(filePath):
                anidb.add_episode(conn, filePath, args.storage)

def execute(args):
    connection = anidb.Connection(args.user, args.password)
    connection.start_logging()
    try:
        with connection as conn:
            add_files(conn, args)
    except Exception as e:
       print('exception: ' + str(e))

