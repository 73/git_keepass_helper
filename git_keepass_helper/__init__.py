import tkinter as tk
import tkinter.simpledialog
import pykeepass
import sys
from construct.core import ChecksumError

# A lot of credit go to: https://dev.to/pratham/custom-git-credential-helper-pfa
class KDB(object):

    def __init__(self, kdbx):
        self.kdbx = kdbx

    def ask_for_password(self):
        # TODO: ask nicer
        tk.Tk().withdraw()
        return tkinter.simpledialog.askstring("Unlock {0}".format(self.kdbx), "Password:", show='*')

    def get(self, info):
        print("Asking: {0}\n".format(self.kdbx), file=sys.stderr)
        password = self.ask_for_password()
        try:
            kdb = pykeepass.PyKeePass(self.kdbx, password=password)
            url = "{0}".format(info['host'])
            if 'username' not in info:
                entry = kdb.find_entries(url=url, first=True)
            else:
                entry = kdb.find_entries(url=url, username=info['username'], first=True)
            if entry is None:
                sys.exit("No key found for: {0}".format(info['host']))
            return entry
        except ChecksumError:
            print("Wrong password!\n", file=sys.stderr)
    def store(self):
       # logic to store username/password to auth file
       # its better to encrypt password if its in plain text
       pass
    def erase(self):
       # logic to delete auth file
       pass
