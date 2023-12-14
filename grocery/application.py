from bottle import Bottle,template, redirect, request,static_file
import database
app = Bottle()
@app.route('/static/<filename:path>')
def serve_static(filename):
    return static_file(filename, root='')
@app.route("/")
def get_list():
    rows = database.get_items()
    n=database.get_customers()
    return template("list", store=rows,customers=n)
@app.post('/search')
def search():
    search_query = request.forms.get('search_query', '')
    results=database.search_store(search_query)
    return template('search_results', results=results, search_query=search_query)
@app.route("/add")
def get_add():
    return template("add_item.tpl")

@app.post("/add")
def post_add():
    store_id = request.forms.get("store_id")
    prod_name=request.forms.get("prod_name")
    price=request.forms.get("price")
    database.add_item(store_id,prod_name,price)
    redirect("/")
@app.route("/update/<id>")
def get_update(id):
    rows = database.get_items(id)
    if len(rows) != 1:
        redirect("/")
    store_id = rows[0]['store_id']
    prod_name = rows[0]['prod_name']
    price = rows[0]['price']

    return template("update_item.tpl",store_id=store_id,prod_name=prod_name,price=price)

@app.post("/update")
def post_update():
    store_id = request.forms.get("store_id")
    prod_name=request.forms.get("prod_name")
    price =request.forms.get("price")
    database.update_item(store_id,prod_name,price)
    redirect("/")
@app.route("/delete/<id>")
def get_delete(id):
    database.delete_item(id)
    redirect("/")
@app.route("/addb")
def get_addb():
    return template("add_bor.tpl")
@app.post("/addb")
def post_add():
   
    name = request.forms.get("name")
    email=request.forms.get("email")
    ph_no=request.forms.get("ph_no")
    id=request.forms.get("id")
    database.add_bor(name,email,ph_no,id)
    redirect("/")

@app.route("/deletebor/<id>")
def get_delete(id):
    database.delete_customers(id)
    redirect("/")
@app.route("/updateb/<id>")
def get_updatebor(id):
    b = database.update_customers(id)
    if len(b) != 1:
        redirect("/list")
    name = b[0]['name']
    email = b[0]['email']
    ph_no = b[0]['ph_no']
    id    = b[0]['id']

    return template("update_bor.tpl", cust_id=id,name=name,email=email,ph_no=ph_no)

@app.post("/updateb")
def post_updatebor():
    id = request.forms.get("id")
    cust_id=int(id)
    name = request.forms.get("name")
    email=request.forms.get("email")
    ph_no=request.forms.get("ph_no")
    database.update_customers(cust_id,name,email,ph_no)
    redirect("/")
if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)