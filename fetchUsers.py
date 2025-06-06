import sqlite3


DB_PATH = 'dbs/login.db'

def fetchUsers():
    with sqlite3.connect(DB_PATH) as db:
        cur = db.cursor()
        cur.execute('SELECT * FROM users')
        rows = cur.fetchall()
        users = dict(rows)
    return users

def insertUser(username, password):
    with sqlite3.connect(DB_PATH) as db:
        cur = db.cursor()
        cur.execute('INSERT INTO users VALUES(?, ?)', (username, password))
        db.commit()
