import argparse
import getpass
import os

import adba

class Connection:
    def __init__(self, user=None, password=None):
        self.user = user
        self.password = password
        if self.password is None:
            self.password = getpass.getpass()

    def __enter__(self):
        self.connection = adba.Connection(keepAlive=True)
        self.connection.auth(self.user,self.password)
        return self.connection

    def __exit__(self, exc_type, exc_value, traceback):
        if self.connection.authed():
            self.connection.logout(True)
        else:
            self.connection.cut()

def add_episode(connection, filePath, storage=None):
    ep = adba.Episode(connection, filePath=filePath,
                      paramsF=["mylist_id"],
                      paramsA=["romaji_name", "epno"])
    ep.load_data()
    name = os.path.basename(filePath)
    if ep.fid is None:
        print 'Missing:', name
    elif ep.mylist_id:
        print 'Found: %s %s - %s' % (ep.romaji_name, str(ep.epno), name)
        connection.mylistadd(lid=ep.mylist_id, edit=1, state=1, storage=storage)
    else:
        print 'Added: %s %s - %s' % (ep.romaji_name, str(ep.epno), name)
        connection.mylistadd(size=ep.size, ed2k=ep.ed2k, state=1, storage=storage)

def create_parser(show_help_option=False):
    anidb_parser = argparse.ArgumentParser(add_help=show_help_option)
    anidb_parser.add_argument('files', metavar='FILE', nargs='+',
                        help='file to process')
    anidb_parser.add_argument('-u', '--user', required=True,
                        help='user at aniDB')
    anidb_parser.add_argument('-p', '--password',
                        help='password at aniDB')
    return anidb_parser
