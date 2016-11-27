import argparse

import anifs.add as add
import anifs.anidb as anidb

def create_anidb_parser(add_help=False):
    anidb_parser = argparse.ArgumentParser(add_help = add_help)
    anidb_parser.add_argument('files', metavar='FILE', nargs='+',
                        help='file(s) to process')
    anidb_parser.add_argument('-u', '--user', required=True,
                        help='user at aniDB')
    anidb_parser.add_argument('-p', '--password',
                        help='password at aniDB')
    return anidb_parser


def create_add_parser(parser, parent_parser):
    add_parser = parser.add_parser('add', parents=[parent_parser])
    add_parser.add_argument('-s','--storage')
    return add_parser

def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='mode')

    anidb_parser = create_anidb_parser()
    create_add_parser(subparsers, anidb_parser)

    args = parser.parse_args()
    connection = anidb.Connection(args.user, args.password)
    connection.start_logging()
    try:
        with connection as conn:
            if args.mode == 'add':
               add.add_files(conn, args)
            else:
               raise ValueError("Unhandled mode %s" % args.mode)
    except Exception as e:
       print('exception: ' + str(e))
    connection.stop_logging()

if __name__ == '__main__':
    main()

