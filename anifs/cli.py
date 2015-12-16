import argparse

import anifs.add as add
import anifs.anidb as anidb

def create_add_parser(parser, parent_parser):
    add_parser = parser.add_parser('add', parents=[parent_parser])
    add.arguments(add_parser)
    return add_parser

def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='mode')

    anidb_parser = anidb.create_parser()
    create_add_parser(subparsers,anidb_parser)

    args = parser.parse_args()

    if args.mode == 'add':
       add.add_files(args)
    else:
       raise ValueError("Unhandled mode %s" % args.mode)

if __name__ == '__main__':
    main()

