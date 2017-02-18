import argparse
import os

import anifs.anidb as anidb
import anifs.export as export

def add_files(conn, args):
    entries = []
    if conn.authed():
        for filePath in args.files:
            if os.path.isfile(filePath):
                entry = anidb.add_episode(conn, filePath, args.storage)
                if entry:
                   entries.append(entry)
    return entries

def run(args):
    connection = anidb.Connection(args.user, args.password)
    connection.start_logging()
    try:
        with connection as conn:
            entries = add_files(conn, args)
            export.export_entries(entries)
    except Exception as e:
       print('exception: ' + str(e))

