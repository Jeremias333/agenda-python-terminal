import sqlite3

con = sqlite3.connect("./database.db")
cursor = con.cursor()

sql_create_contacts = """
	CREATE TABLE contacts (
	    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	    name VARCHAR NOT NULL,
	    phone VARCHAR NOT NULL
	);""" #EXECUTADO

sql_first_insert = """ 
	INSERT INTO contacts(name, phone)
	VALUES ('Jeremias', '+55 81 98553-1720');
"""
#con.commit()

sql_select_all = """ 
	SELECT * FROM contacts;
"""

sql_drop_contacts = """DROP TABLE contacts"""

cursor.execute(sql_select_all)
print(cursor.fetchall())
for linha in cursor.fetchall():
	print(linha)

con.close