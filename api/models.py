from peewee import *
from datetime import date
import random
import string

db = SqliteDatabase('hacks.db')

def getid(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

class User(Model):
    id = CharField(primary_key=True)
    name = CharField()
    email = CharField(unique=True)
    pass_hash = CharField()
    is_seller = BooleanField()
    class Meta:
        database = db

class Shop(Model):
    id = CharField(primary_key=True)
    city = CharField()
    name = CharField()
    owner = ForeignKeyField(User, backref='shop')
    class Meta:
        database = db

class Product(Model):
    id = CharField(primary_key=True)
    name = CharField()
    price = IntegerField()
    shop = ForeignKeyField(Shop, backref='products')
    class Meta:
        database = db

db.connect()
db.create_tables([User, Shop, Product])