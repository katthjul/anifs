import argparse
import os

import anifs.anidb as anidb

def add_files(args):
    try:
        connection = anidb.Connection(args.user, args.password)
        with connection as conn:
            for filePath in args.files:
                if os.path.isfile(filePath):
                    anidb.add_episode(conn, filePath, args.storage)
    except Exception,e:
       print('exception: ' + str(e))

def arguments(parser):
    parser.add_argument('-s','--storage')

def main():
    parser = anidb.create_parser(True)
    arguments(parser)

    args = parser.parse_args()
    add_files(args)
    

if __name__ == '__main__':
    main()

