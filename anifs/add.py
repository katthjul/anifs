import argparse
import os

import anifs.anidb as anidb

def add_files(conn, args):
    if conn.authed():
        for filePath in args.files:
            if os.path.isfile(filePath):
                anidb.add_episode(conn, filePath, args.storage)

def arguments(parser):
    parser.add_argument('-s','--storage')

def main():
    parser = anidb.create_parser(True)
    arguments(parser)

    args = parser.parse_args()
    connection = anidb.Connection(args.user, args.password)
    with connection as conn:
        add_files(conn, args)
    

if __name__ == '__main__':
    main()

