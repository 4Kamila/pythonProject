import sqlite3

connection = sqlite3.connect("D:\itstep_DB.sl3", 5)
cur = connection.cursor()
# cur.execute("CREATE TABLE first_table (name TEXT);")
# cur.execute("INSERT INTO first_table (name) "
#             "VALUES ('Nick');")
# cur.execute("INSERT INTO first_table (name) VALUES ('Ann');")
# cur.execute("INSERT INTO first_table (name) VALUES ('Kats');")
# cur.execute("INSERT INTO first_table (name) VALUES ('John');")
# cur.execute("SELECT rowid, name FROM first_table;")
# cur.execute("UPDATE first_table SET name='Kate' WHERE rowid=4;")
# cur.execute("DELETE FROM first_table WHERE rowid=5;")
cur.execute("DROP TABLE first_table;")
# connection.commit()
# cur.execute("SELECT rowid, name FROM first_table")
connection.commit()
q
# print(connection)
# print(cur)
connection.close()