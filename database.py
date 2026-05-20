import sqlite3

def get_db():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    # Add your new table between lines 15 & 16.
    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS pieces (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            piecename TEXT,
            work TEXT,
            owner TEXT,
            FOREIGN KEY (owner) REFERENCES users (username)
        )
    """)
    conn.commit()
    conn.close()