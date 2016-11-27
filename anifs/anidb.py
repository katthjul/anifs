import getpass
import os

import adba

class Connection:
    def __init__(self, user=None, password=None):
        self.user = user
        self.password = password
        if self.password is None:
            self.password = getpass.getpass()
        self.connection = None

    def __enter__(self):
        self.connection = adba.Connection()
        if not self.connection.authed():
            self.connection.auth(self.user, self.password)
        return self.connection

    def __exit__(self, exc_type, exc_value, traceback):
        self.connection.logout()

    def start_logging(self):
        self.logger = adba.StartLogging()

    def stop_logging(self):
        adba.StopLogging(self.logger)

def add_episode(connection, filePath, storage=None):
    ep = adba.Episode(connection, filePath=filePath,
                      paramsF=["mylist_id"],
                      paramsA=["romaji_name", "epno"])
    ep.load_data()
    name = os.path.basename(filePath)
    if ep.fid is None:
        print('Missing:', name)
    elif ep.mylist_id:
        ep.edit_to_mylist(state=1, storage=storage)
        print('Found: {0} {1} - {2}'.format(ep.romaji_name, str(ep.epno), name))
    else:
        ep.add_to_mylist(state=1, storage=storage)
        print('Added: {0} {1} - {2}'.format(ep.romaji_name, str(ep.epno), name))

