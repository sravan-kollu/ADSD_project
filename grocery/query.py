import sqlite3

connection = sqlite3.connect("Grocery_store.db")

cursor = connection.cursor()

store = cursor.execute("Select * from store")
print(store.fetchall())
customers = cursor.execute("Select * from customers")
print(customers.fetchall())