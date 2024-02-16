import sqlite3

connection = None
cursor = None


def open():
    global connection, cursor
    connection =sqlite3.connect("blog.db")
    cursor = connection.cursor()


def close():
    cursor.close()
    connection.close()