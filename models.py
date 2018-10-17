from peewee import (CharField,
                    SqliteDatabase,
                    Model,
                    TextField,
                    DateTimeField,
                    IntegrityError,
                    IntegerField,
                    OperationalError
                    )

db = SqliteDatabase("farmers.db")

farmers = [
    {'id':1,'username':'faryda', 
    'password':'farida01', 'email':'farida@joe.com',
    'phone':'070999999', },
    {'id':2, 'username':'faryda', 
    'password':'farida01', 'email':'farida@joe.com',
    'phone':'070999999', }, 
    
]


class Farmer(Model):

  username = CharField(max_length=200)
  password = CharField(max_length=200)
  email = CharField(max_length=50,unique=True)
  phone = IntegerField(default=10)
 
 


  class Meta:
        database = db


def initialize():
    try:
        Farmer.create_table()
    except OperationalError:
        pass
    for farmer in farmers:
      try:
        Farmer.create(
            username=farmer.get('username'),
             password=farmer.get('password'),
            email=farmer.get('email'),
            phone=farmer.get('phone'),
            
           
            
            )
      except IntegrityError:
        pass
    
