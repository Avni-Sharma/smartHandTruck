# A List of SQL Commands for the Case #
#---------------------------------------------------------------


################################################################
#                         QUESTIONS
################################################################

# How do we reference a table in a database on SQLite?

################################################################
#                         EMPLOYEES
################################################################ 

# RETRIEVE EMPLOYEE LIST
#---------------------------------------------------------------
# activated when "Employee/Staff" button clicked on website 
def getEmpList_DB():
    con = sqlite3.connect('file.db') # should this be a table within a database?
    cursorObj = con.cursor()

    rowSTRING2 = "["

    cursorObj.execute('SELECT * FROM Employees;')
    rows = cursorObj.fetchall()
    for row in rows:
        newRow = []
        e = Employee(row[0], row[1])
        rowSTRING2 += "{" + e.getDict() + "},"
    rowSTRING2 = rowSTRING2[0:-1]
    rowSTRING2 = rowSTRING2 + "]"
    rowSTRING2 = eval(rowSTRING2)
    return rowSTRING2

# ADD EMPLOYEE 
#---------------------------------------------------------------
def addEmployee_DB(Emp_ID, Emp_Name, Position):
    # create a database connection 
    database = "file.db" 
    conn = None 
    conn = sqlite3.connect(database)
    # SQL command to be run 
    sql = 'INSERT INTO Employees (Emp_ID, Emp_Name, Position) values (?,?,?)'
    cur = conn.cursor()
    cur.execute(sql, (Emp_ID, Emp_Name, Position))
    conn.commit()
    
# DELETE EMPLOYEE
#---------------------------------------------------------------
def delEmployee_DB(Emp_ID):
    # create a database connection 
    database ="file.db"
    conn = None 
    conn = sqlite3.connect(database)
    # SQL command to be run 
    sql = 'DELETE FROM Employees WHERE Emp_ID =?'
    cur = conn.cursor()
    cur.execute(sql, (Emp_ID,))
    conn.commit()

# UPDATE EMPLOYEE
#---------------------------------------------------------------


################################################################
#                         PRODUCTS
################################################################

# ADD PRODUCT

# DELETE PRODUCT

# UPDATE PRODUCT INFO


