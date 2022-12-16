import sqlite3
import pathlib

this_dir = str(pathlib.Path(__file__).parent.resolve())
def get_db_connection():
    try:
        connection = sqlite3.connect(this_dir + '/sagirov.db')
    except:
        raise SystemError
    return connection

def create_users_table():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nickname TEXT UNIQUE,
        first_name TEXT NULL,
        last_name TEXT NULL, 
        email TEXT NULL, 
        phone TEXT NULL,
        birth_date TEXT NULL,
        sent INTEGER DEFAULT 0 NULL,
        sent_date TEXT NULL,
        all_done INTEGER DEFAULT 0 NULL,
        done_date TEXT NULL,
        chat_id TEXT NULL
        )""")
