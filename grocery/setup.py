import sqlite3

connection = sqlite3.connect("Grocery_store.db")

cursor = connection.cursor()

try:
    cursor.execute("drop table store")
    cursor.execute("drop table customers")
except:
    pass

cursor.execute("create table store(store_id integer primary key,prod_name text,price integer)")
cursor.execute("create table customers(cust_id integer primary key,name text,ph_no integer,email text,id integer,foreign key(id) references customers(store_id))")
cursor.execute("""INSERT INTO store VALUES(1,"Shampoo",20) """)
cursor.execute("""INSERT INTO customers VALUES(1,'sravan',1234557,'sravan123@gmail.com',1) """)
connection.commit()
connection.close()