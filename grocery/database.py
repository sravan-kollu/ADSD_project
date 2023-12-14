import sqlite3

connection = sqlite3.connect("Grocery_store.db")
def get_customers(id=None):
    cursor = connection.cursor()

    if id is None:
        cursor.execute("SELECT * FROM customers")
    else:
        cursor.execute(f"SELECT * FROM customers WHERE cust_id={id}")

    rows = cursor.fetchall()
    customers = [{'cust_id': row[0], 'name': row[1], 'ph_no':row[2],'email': row[3], 'id': row[4]} for row in rows]

    return customers
def get_items(id=None):
    cursor = connection.cursor()
    if id == None:
        rows = cursor.execute("select * from store")
    else:
        rows = cursor.execute(f"select * from store where store_id={id}")
    rows = cursor.fetchall()
    rows = list(rows)
    store = [{'store_id': row[0], 'prod_name': row[1], 'price': row[2]} for row in rows]
    return store


def add_item(store_id,prod_name,price):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO store (store_id, prod_name, price) VALUES (?, ?, ?)", (store_id,prod_name,price))
    connection.commit()

def add_customers(cust_id,name,ph_no,email,id):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO customers (cust_id,name,ph_no,email,id) VALUES (?, ?, ?)", (cust_id,name,ph_no,email,id))
    connection.commit()

def delete_item(id):
    cursor = connection.cursor()
    cursor.execute(f"delete from store where store_id={id}")
    connection.commit()
def delete_customers(id):
    cursor = connection.cursor()
    cursor.execute(f"delete from customers where cust_id={id}")
    connection.commit()
def update_customers(cust_id, name, email, id):
    cursor = connection.cursor()
    cursor.execute(f"update customers set id={cust_id},name='{name}',email='{email}' where cust_id={id}")
    connection.commit()    
def update_item(store_id,prod_name,price):
    cursor = connection.cursor()
    cursor.execute(f"update store set productname='{prod_name}',price='{price}' where store_id={store_id}")
    connection.commit()
def search_store(store_id):
    cursor = connection.cursor()
    cursor.execute("SELECT customers.cust_id, customers.name,customers.ph_no, customers.email FROM store JOIN customers ON store.store_id = customers.id WHERE store.prod_name = '{prod_name}'")
    connection.commit()
    results = cursor.fetchall()
    return results