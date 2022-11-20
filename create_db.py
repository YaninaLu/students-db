import sqlite3


def create_db(script_file, database_file):
    with open(script_file, "r") as f:
        sql_script = f.read()

    with sqlite3.connect(database_file) as conn:
        c = conn.cursor()
        c.executescript(sql_script)
