import sqlite3

connection = sqlite3.connect("whether.sl3", 5)
cur = connection.cursor()
cur.execute("CREATE TABLE first_table (name TEXT);")
cur.execute("INSERT INTO first_table (name) "
            "VALUES ('Nick');")