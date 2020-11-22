import sqlite3 
import os
def show_all():

	conn = sqlite3.connect('customer.db')
	c = conn.cursor()
	if os.path.exists('customer.db')==False:

		c.execute("""CREATE TABLE customers(
				first_name text,
				last_name text,
				email text
			) """)

		many_customer = [
						('John', 'Elder', 'john@codemy.com'),
						('sunny', 'Smith', 'tim@codemy.com'),
						('Mary', 'Brown', 'mary@codemy.com'),
						('west', 'brown', 'west@brown.com'),
						('steph', 'kuewa', 'steph@kuewa.com'),
						('Dan', 'Pas', 'dan@codemy.com')
					]

		c.executemany("INSERT INTO customers VALUES (?,?,?)", many_customer)
		conn.commit()
	c.execute("SELECT rowid, * FROM customers")
	conn.commit()
	lst = c.fetchall()
	for x in lst:
		print(x)
	#c.execute("DROP TABLE customers")
	#conn.commit()

	conn.close()
	#os.remove('customer.db')
if os.path.exists('customer.db')==False:
	show_all()

#add a new record to a database
def add_one(first,last,email):
	conn = sqlite3.connect('customer.db')
	c = conn.cursor()
	c.execute("INSERT INTO customers VALUES (?,?,?)",(first,last,email))
	conn.commit()
	conn.close()

def delete_one(id):
	conn = sqlite3.connect('customer.db')
	c = conn.cursor()
	c.execute("DELETE FROM customers WHERE rowid = (?)",id)
	conn.commit()
	conn.close()

def add_many(lst):
	conn = sqlite3.connect('customer.db')
	c = conn.cursor()
	c.executemany("INSERT INTO customers VALUES (?,?,?)",(lst))
	conn.commit()
	conn.close()

def email_lookup(email):
	conn = sqlite3.connect('customer.db')
	c = conn.cursor()
	c.execute("SELECT rowid, * from customers WHERE email = (?)",(email,))
	items = c.fetchall()
	for x in items:
		print(x)
	conn.close()