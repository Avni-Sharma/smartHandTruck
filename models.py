from init import db

class Customers(db.Model):

    __tablename__='Customers'

    Customer_ID=db.Column(db.Integer,primary_key=True)
    FirstName=db.Column(db.String(64))
    LastName=db.Column(db.String(64))
    Email=db.Column(db.String(64),unique=True,index=True)
    Phone=db.Column(db.String(64))
    Zip=db.Column(db.Integer)


    def __init__(self,FirstName,LastName,Email,Phone,Zip):

        self.FirstName=FirstName
        self.LastName=LastName
        self.Email=Email
        self.Phone=Phone
        self.Zip=Zip
