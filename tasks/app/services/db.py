from __future__ import print_function
import os
import sys
import sqlite3
from functools import wraps

SqlError = sqlite3.Error

def is_connected(f):
    @wraps(f)
    def inner(self, *args, **kwargs):
        if self.connection is None:
            print("Database not initialised")
        else:
            return f(self, *args, **kwargs)
    return inner

class BaseStorage:
    def __init__(self, database):
        self.__db = database
        self.connection = None
        self.connected = False
        self.cursor = None
        self.initialize()

    def initialize(self):
        self.connect()
        self.setup()

    def setup(self):
        """Override this method for initial db setup"""
        raise NotImplementedError

    def connect(self):
        """Connects to the SQLite3 database."""
        self.connection = sqlite3.connect(self.__db)
        self.cursor = self.connection.cursor()
        self.connected = True
        self.statement = ''

    @is_connected
    def close(self): 
        """Closes the SQLite3 database."""
        self.commit()
        self.connection.close()
        self.connected = False

    @is_connected
    def commit(self): 
        self.connection.commit()

    @is_connected
    def executescript(self, script):
        cursor = self.cursor
        cursor.executescript(script)
        self.commit()

    @is_connected
    def execute(self, script, arg_tuple):
        cursor = self.cursor
        cursor.execute(script, arg_tuple)
        self.commit()
