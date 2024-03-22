import sqlite3
from contextlib import contextmanager

database = 'C:/Projects_goit/c_systems/goit-cs-hw-03/goit-cs-hw-03-01/my_base.sqlite'


@contextmanager
def create_connection(my_base):
    """ create a database connection to a SQLite database """
    conn = sqlite3.connect(my_base)
    yield conn
    conn.rollback()
    conn.close()
