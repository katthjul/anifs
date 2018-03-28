import argparse
import os
import shutil

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

def move_files(entries, destination):
    print('Moving {0} file(s) to directory {1}'.format(len(entries), destination))
    for entry in entries:
        shutil.move(entry.filePath, destination)
        entry.update_path(destination)

def run(args):
    connection = anidb.Connection(args.user, args.password)
    connection.start_logging()
    try:
        with connection as conn:
            entries = add_files(conn, args)
            export.export_entries(entries)
            if args.destination:
                move_files(entries, args.destination)
    except Exception as e:
       print('exception: ' + str(e))

