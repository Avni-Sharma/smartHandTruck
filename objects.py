#Add def to what we need later on 

class Customer:
    def __init__(self, Customer_ID, FirstName, LastName, ZipCode, TelephoneNumber, Email, Category):
        self.__CustomerID = Customer_ID
        self.__FirstName = FirstName
        self.__LastName = LastName
        self.__ZipCode = ZipCode
        self.__TelephoneNumber = TelephoneNumber
        self.__Email = Email
        self.__Category = Category
        
    def getName(self):
        #Returns customer's full name 
        return self.__FirstName + ' ' + self.__LastName
        
    def getCID(self):
        #Returns customer's ID 
        return Customer_ID

class Product:
    def __init__(self, Product_ID, Product_Name, Color, Price):
        self.__ProductID = Product_ID
        self.__ProductName = Product_Name
        self.__Color = Color
        self.__Price = Price
        
class Employee:
    def __init__(self, Employee_ID, FirstName, LastName, Position, HrRate, HireDate):
        self.__EmployeeID = Employee_ID
        self.__FirstName = FirstName
        self.__LastName = LastName
        self.__Position = Position
        self.__HrRate = HrRate
        self.__HireDate = HireDate

class Supplier:
    def __inity__(self, SupplierID, SupplierName, ZipCode, Telephone, Email):
        self.__SupplierID = SupplierID
        self.__SupplierName = SupplierName
        self.__ZipCode = ZipCode
        self.__Telephone = Telephone
        self.__Email = Email


        
        