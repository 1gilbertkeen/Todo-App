import sqlite3

conn = sqlite3.connect('gildb.db')
c = conn.cursor()

conn2 = sqlite3.connect('gildb.db')
c2 = conn2.cursor()