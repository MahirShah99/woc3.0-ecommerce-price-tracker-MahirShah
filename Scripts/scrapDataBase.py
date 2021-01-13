import sqlite3
from datetime import datetime

def db_connect():
	conn = sqlite3.connect("scrapDB.db")
	return conn

def delete_row(field):
	conn = db_connect()
	try:
		conn.execute("DELETE FROM scrapTable where website=?", (field,))
		conn.commit()
	except:
		print("No Record")
	finally:
		conn.close()

def insert_into_table(link, desired_price, email, scrapTime, status, website):
	conn = db_connect()
	delete_row(website)
	conn.execute('''CREATE TABLE IF NOT EXISTS scrapTable
				(link VARCHAR(255) NOT NULL,
		         desired_price INT NOT NULL,
		         email VARCHAR(255) NOT NULL,
		         scrapTime DATETIME NOT NULL,
		         status BOOLEAN NOT NULL,
		         website VARCHAR(255) NOT NULL);''')

	conn.execute("INSERT INTO scrapTable (link, desired_price, email, scrapTime, status, website) VALUES(?,?,?,?,?,?)", (link, desired_price, email, scrapTime, status, website))
	conn.commit()
	conn.close()

def get_data(website):
	data = {}
	conn = sqlite3.connect("scrapDB.db")	
	cursor = conn.execute("SELECT * from scrapTable where website=?", (website,))
	
	for row in cursor:
		data['link'] = row[0]
		data['desired_price'] = row[1]
		data['email'] = row[2]
		data['scrapTime'] = row[3]
		data['status'] = row[4]
		data['website'] = row[5]

	conn.close()
	return data

def update_row(scrapTime, website):
	conn = db_connect()

	try:
		conn.execute("UPDATE scrapTable SET scrapTime=? WHERE website=?", (scrapTime, website))
		conn.commit()
	except:
		print("Cannot Update")
	finally:
		conn.close()