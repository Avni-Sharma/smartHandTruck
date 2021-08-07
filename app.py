from flask import Flask, render_template
import sqlite3
from init import app,db
from flask import render_template,redirect,url_for,flash,abort,request
from models import Customers
from forms import RegistrationForm,UpdateForm, DeleteForm

#app=Flask(__name__)

@app.route('/')
@app.route("/index")
def index():
    return render_template("index.html")

@app.route('/home')
def home():
    return render_template("index.html")


@app.route('/supplier')
def suppliers():
    con = sqlite3.connect('file.db')
    cursorObj = con.cursor()
    cursorObj.execute('SELECT * FROM Supplier;')
    rows = cursorObj.fetchall()
    con.close()
    return render_template("supplier.html", results=rows)


@app.route('/product')
def products():
    con = sqlite3.connect('file.db')
    cursorObj = con.cursor()
    cursorObj.execute('SELECT * FROM Product;')
    rows = cursorObj.fetchall()
    con.close()
    return render_template("product.html", results=rows)

@app.route('/employee')
def employee():
    con = sqlite3.connect('file.db')
    cursorObj = con.cursor()
    cursorObj.execute('SELECT * FROM Employee;')
    rows = cursorObj.fetchall()
    con.close()
    return render_template("employee.html", results=rows)

@app.route("/order")
def order():
    con = sqlite3.connect('file.db')
    cursorObj = con.cursor()
    cursorObj.execute('SELECT * FROM Product;')
    results = cursorObj.fetchall()
    cursorObj.execute('SELECT * FROM Employee;')
    employeelist=cursorObj.fetchall()
    con.close()

    return render_template("order.html", employeelist=employeelist, result=results)

@app.route('/submitorder', methods=['GET','POST'])
def submitorder():

    quantity=[]
    for i in range (1,13):
         q = request.form.get(f"q{i}")
         quantity.append(q)

    count = 0

    for i,num in enumerate(quantity):
        if num!='':
            quantity[i]=int(num)
            count+=1
        else:
            quantity[i]=0

    customer_id =  request.form.get("CustomerID")
    employee_id =  request.form.get("EmployeeID")
    sql_insert_orders = 'Insert into orders ("customer_id", "order_type", "sales_person") values (?,?,?)'
    order_type = "Pending"
    error = None
    orders_params = [customer_id, order_type, employee_id]
    total_qty = sum(quantity)

    con = sqlite3.connect('file.db')
    cursorObj = con.cursor()
    if count <= 5:
        if total_qty <= 10:

            # creating the order
            cursorObj.execute(sql_insert_orders , orders_params)
            order_id = cursorObj.lastrowid

            # Checking the inventory and update order_status variable
            for index, qty in enumerate(quantity):
                check_inventory_query='SELECT inventory from product where product_id=?'
                check_inv_params = [index+1]
                cursorObj.execute(check_inventory_query, check_inv_params)

                # [(10)]
                if qty > cursorObj.fetchall()[0][0]:
                    order_type = 'Failed'
                    break


            # inserting each product's order details only if you have the inventory.
            sql_orderdetails = 'Insert into orderdetail ("Product_ID", "Order_ID","Quantity") values (?,?,?)'
            if order_type != 'Failed':
                for index,qty in enumerate(quantity):
                    if qty > 0:
                        order_details_params= [index+1, order_id, qty]
                        cursorObj.execute(sql_orderdetails, order_details_params)

                        # Updating the each product inventory
                        cursorObj.execute('Update product set inventory=inventory-? where Product_ID = ?', [qty, index+1])

                order_type = 'Success'

            # Update orders table with the status.
            cursorObj.execute('Update orders set order_type=? where order_ID=?',[order_type,order_id])
            con.commit()
            con.close()

            if order_type == 'Success':
                con = sqlite3.connect('file.db')
                cursorObj = con.cursor()
                cursorObj.execute('SELECT * FROM OrderDetail;')
                orderdets = cursorObj.fetchall()
                con.close()
                return render_template('orderconfirm.html',orderdets=orderdets)
                # write a query to update the remianing inventory

            else:
                error = "Quantity ordered exceeds inventory. Please reduce the quantity"
        else:
            error = "Cannot exceed total quantity as 10"
    else:
        error = "Cannot exceed 5 different products"

    return render_template('failed.html', error=error)

        # return render_template('failure.html')






def database_cmd(command:str):
    con = sqlite3.connect('file.db')
    cursorObj = con.cursor()
    cursorObj.execute(command)
    rows = cursorObj.fetchall()
    con.close()
    return rows

@app.route('/customertable')
def customertable():

    customers=Customers.query.all()
    return render_template('customertable.html',customers=customers)


@app.route("/register",methods=['GET','POST'])
def register():

    form= RegistrationForm()

    if form.validate_on_submit():
        customer=Customers(FirstName=form.FirstName.data,LastName=form.LastName.data,Email=form.Email.data,Phone=form.Phone.data, Zip=form.Zip.data)

        db.session.add(customer)
        db.session.commit()
        return redirect(url_for('customertable'))

    return render_template("register.html",form=form)

@app.route('/updatecustomer',methods=['GET','POST'])
def updatecustomer():

    form=UpdateForm()

    if form.validate_on_submit():

        customer=Customers.query.filter_by(Email=form.Email.data).first()

        if customer is None:
            print("User Not Found, Hence Redirecting to Customers")
            return redirect(url_for('customertable'))
        else:
            customer.FirstName=form.FirstName.data
            customer.LastName=form.LastName.data
            customer.Phone=form.Phone.data
            customer.Zip=form.Zip.data

            db.session.add(customer)
            db.session.commit()
            print("Update Successful")
            return redirect(url_for('customertable'))

    return render_template('updatecustomers.html',form=form)


@app.route('/deletecustomer',methods=['GET','POST'])
def deletecustomer():

    form=DeleteForm()

    if form.validate_on_submit():

        customer=Customers.query.filter_by(Email=form.Email.data).first()

        if customer is None:
            return redirect(url_for('customertable'))
        else:

            db.session.delete(customer)
            db.session.commit()
            print("Delete Successful")
            return redirect(url_for('customertable'))

    return render_template('deletecustomers.html',form=form)




def getDictList_DB():
    con = sqlite3.connect('file.db')
    cursorObj = con.cursor()

    # rowSTRING2 = "["

    # cursorObj.execute('SELECT * FROM Suppliers;')
    # rows = cursorObj.fetchall()
    # for row in rows:
    #     newRow = []
    #     m = Supplier(row[0], row[1])
    #     rowSTRING2 += "{" + m.getDict() + "},"
    # rowSTRING2 = rowSTRING2[0:-1]
    # rowSTRING2 = rowSTRING2 + "]"
    # rowSTRING2 = eval(rowSTRING2)
    # return rowSTRING2

# if __name__=='__main__':
#      app.run()