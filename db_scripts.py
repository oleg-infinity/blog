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

def getUser():
    open()
    cursor.execute('''SELECT * FROM user''')
    user = cursor.fetchone()
    close()
    return user