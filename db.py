import pandas
import pyodbc
import sqlite3


class Connection:
    def __init__(self):
        self.conn = None


conn = Connection()


def connect_access(path):
    conn.conn = pyodbc.connect("Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=" + path + ";")


def connect_sqlite(path):
    conn.conn = sqlite3.connect(path)


def query(sql):
    return pandas.read_sql(sql, conn.conn)
